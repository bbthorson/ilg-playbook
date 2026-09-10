#!/usr/bin/env python3
"""Executable forms of the equations the ILG playbook states in LaTeX.

The playbook keeps roughly a dozen formulas in prose. Nothing verified that a
worked example still matched its formula, that weights still summed to 1, or
that a figure still depicted the equation it illustrated. This module is the
single implementation those documents are checked against, the way
RetiredTerms.yml is the single record renames are checked against.

**The documents are the specification.** Where a document and this module
disagree, the document wins and the module is the bug. Every function names its
canonical home in its docstring, and test_ilg_models.py asserts that each worked
example in those documents reproduces here.

CALIBRATION STATUS
------------------
Nothing in this module is fitted. Every parameter default is a reasoned
starting value carried over from the documents, and the documents say so
themselves: 03-mathematical-models.md states the functional forms are
"specified, not fitted" and exist "to structure judgment, not to forecast."

- a = 2.25 is anchored by analogy to prospect theory's loss aversion
  coefficient. It is not a measurement, and 03-mathematical-models.md section
  1.6 is explicit that a is not the same quantity as lambda. Section 1.7 fixes
  its units: a, c and y are all fractions of annual contract value, so a = 2.25
  means the uncertainty term is worth 2.25 annual contract values at a fully
  open gap. Stating the units does not make the number an estimate.
- beta = 1.35 is chosen inside a motivated range. Only the fact that beta > 1
  carries literature support; the value does not.
- The Friction Efficiency Index weights have no empirical basis at all.
- The seller-surplus forms have no parameter anchored in published literature.

Outputs rank deals against each other. They do not predict a cycle length, a
close date, or a probability. Do not quote any number this module produces as
an empirical estimate.

No dependencies, standard library only, matching the two checkers in
practice/02-internal-ops/linting/.
"""

import collections
import math

# --------------------------------------------------------------------------
# Parameter defaults.
#
# Provenance for each of these is in the parameter reference tables of
# theory/01-foundation/03-mathematical-models.md section 5 and
# practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md.
# Read those columns before quoting any value outside this repository.
# --------------------------------------------------------------------------

A_RISK_AVERSION = 2.25       # anchored by analogy, not fitted; ACV units
DOMINANCE_THRESHOLD = 0.50   # chosen; share at which one component dominates
ALPHA_COORDINATION = 1.0     # normalizing convention
BETA_COMMITTEE = 1.35        # chosen within [1.2, 2.0]
GAMMA_TECHNICAL_OVERLAP = 0.20   # chosen field refinement
W_TECH, W_PROCESS = 0.6, 0.4     # chosen, sum to 1
PHI_TECH, PHI_PROCESS = 1.2, 1.1  # chosen
MU_RETURN_UNCERTAINTY = 1.0  # normalizing convention
NU_VENDOR_DOUBT = 2.0        # chosen
KAPPA_PROOF_DECAY = 0.5      # chosen
GAMMA_RESPONSIVENESS = 0.5   # chosen

# Raw Bilateral Asymmetry Scorecard range, from
# practice/02-internal-ops/04-incentives-asymmetry-scorecard.md part 3.
RAW_GAP_MIN, RAW_GAP_MAX = 2.0, 10.0

# Process Calculator step 2 band edges, from
# practice/01-field-assets/process-calculator.md.
COST_SCORE_MIN, COST_SCORE_MAX = 4, 20
TURNKEY_MAX = 9        # 4 to 9 inclusive
STRUCTURAL_MIN = 10    # 10 to 20 inclusive

# Friction Efficiency Index composite weights, in FAR / BCV / RMS / SVI order.
FEI_WEIGHTS = (0.35, 0.25, 0.25, 0.15)
BCV_REF_DEFAULT = 0.5  # convention until twenty closed Structural deals exist


# ==========================================================================
# theory/01-foundation/03-mathematical-models.md section 1.5
# Normalizing the gap before substitution.
# ==========================================================================

class NormalizedGap(float):
    """A Bilateral Asymmetry Gap already mapped onto the [0, 1] scale.

    This type exists to make a documented past bug unrepresentable. The
    Asymmetry Scorecard emits a raw score on [2, 10]. Neither cost equation
    accepts that range: section 1.5 notes that substituting a raw 10 would
    inflate base friction elevenfold, "which no observed deal supports," and
    that confusing the two scales "produces cost estimates off by an order of
    magnitude."

    Because a bare float cannot say which scale it is on, effective_cost and
    reduced_cost accept only this type. Reach it one of two ways:

    - normalize_gap(raw) for a score straight off the scorecard, or
    - NormalizedGap(x) when you already hold a normalized value and are
      asserting that deliberately.

    Values above 1 are permitted rather than clamped. Section 1.5 states the
    normalized gap may exceed 1 when asymmetry rebuilds past the instrument's
    ceiling under the Decay Clock, since the scorecard measures a point in time
    and cannot observe drift beyond its own range.
    """

    __slots__ = ()

    def __new__(cls, value):
        value = float(value)
        if value < 0.0:
            raise ValueError(
                "a normalized gap cannot be negative; 0 is complete "
                "informational symmetry (section 2.1)"
            )
        if math.isnan(value) or math.isinf(value):
            raise ValueError("a normalized gap must be finite")
        return super().__new__(cls, value)

    def __repr__(self):
        return "NormalizedGap({:g})".format(float(self))


def normalize_gap(raw_gap):
    """Map a raw scorecard gap on [2, 10] onto [0, 1]. Section 1.5.

        gap_hat = (raw - 2) / 8

    Keeps the structural multiplier (1 + gap) inside [1, 2] and the reduced
    form's quadratic term bounded by a. Use the raw score for the scorecard's
    own field triage bands; use this value in either cost equation.
    """
    raw_gap = float(raw_gap)
    if not RAW_GAP_MIN <= raw_gap <= RAW_GAP_MAX:
        raise ValueError(
            "raw gap {:g} is outside the scorecard range [{:g}, {:g}]; the "
            "scorecard sums two halves each on [1, 5]".format(
                raw_gap, RAW_GAP_MIN, RAW_GAP_MAX)
        )
    return NormalizedGap((raw_gap - RAW_GAP_MIN) / (RAW_GAP_MAX - RAW_GAP_MIN))


def _require_normalized(gap, caller):
    if not isinstance(gap, NormalizedGap):
        raise TypeError(
            "{} requires a NormalizedGap, not a bare {}. The Asymmetry "
            "Scorecard emits a raw score on [2, 10] and neither cost equation "
            "accepts that range. Call normalize_gap(raw) first, or wrap an "
            "already-normalized value in NormalizedGap(). See "
            "03-mathematical-models.md section 1.5.".format(
                caller, type(gap).__name__)
        )
    return float(gap)


# ==========================================================================
# theory/01-foundation/03-mathematical-models.md section 1
# The two representations of transaction cost.
# ==========================================================================

def effective_cost(f_search, f_consensus, f_implementation, gap):
    """Structural form, section 1.1.

        F_effective = (F_search + F_consensus + F_implementation) * (1 + gap)

    Diagnostic. Use this to find which component is binding on a specific deal
    and therefore which artifact to deploy. `gap` must be a NormalizedGap.
    """
    gap = _require_normalized(gap, "effective_cost")
    for name, value in (("f_search", f_search),
                        ("f_consensus", f_consensus),
                        ("f_implementation", f_implementation)):
        if value < 0:
            raise ValueError("{} cannot be negative".format(name))
    base = f_search + f_consensus + f_implementation
    return base * (1.0 + gap)


COMPONENTS = ("search", "consensus", "implementation")

FrictionVector = collections.namedtuple(
    "FrictionVector", "base effective direction magnitude gap dominant")


def _check_components(f_search, f_consensus, f_implementation):
    values = (f_search, f_consensus, f_implementation)
    for name, value in zip(COMPONENTS, values):
        if value < 0:
            raise ValueError("f_{} cannot be negative".format(name))
    return values


def effective_cost_per_component(f_search, f_consensus, f_implementation,
                                 gap_search, gap_consensus,
                                 gap_implementation):
    """Structural form since Constitution v17.0, section 1.1.

        F_effective = sum_k F_k * (1 + gap_k)

    Each component is amplified by the asymmetry inside its own pair of
    parties, and the three pairs differ: search is the buyer against the
    market, consensus is the buyer's stakeholders against each other, and only
    implementation is buyer against seller. Section 2.4 gives the instruments.

    Every gap must be a NormalizedGap. effective_cost() below is the same
    quantity written with the single multiplier the three factor into.
    """
    values = _check_components(f_search, f_consensus, f_implementation)
    gaps = (_require_normalized(gap_search, "effective_cost_per_component"),
            _require_normalized(gap_consensus, "effective_cost_per_component"),
            _require_normalized(gap_implementation,
                                "effective_cost_per_component"))
    return sum(f * (1.0 + g) for f, g in zip(values, gaps))


def weighted_mean_gap(f_search, f_consensus, f_implementation,
                      gap_search, gap_consensus, gap_implementation):
    """The scalar the three component gaps factor into, section 1.1.

        gap_A = sum_k F_k gap_k / sum_k F_k

    The identity effective_cost_per_component(...) == effective_cost(..., this)
    is exact, not an approximation. The scalar the framework carried before
    v17.0 is the friction-weighted mean of the three, which is why no result
    that consumed it broke when the split happened.

    Undefined when base friction is zero: a deal with no cost has no
    composition, and returning 0 there would assert symmetry that was never
    measured.
    """
    values = _check_components(f_search, f_consensus, f_implementation)
    gaps = (_require_normalized(gap_search, "weighted_mean_gap"),
            _require_normalized(gap_consensus, "weighted_mean_gap"),
            _require_normalized(gap_implementation, "weighted_mean_gap"))
    base = sum(values)
    if base == 0:
        raise ValueError(
            "base friction is zero, so the friction-weighted mean gap is "
            "undefined; a deal with no cost has no composition")
    return NormalizedGap(sum(f * g for f, g in zip(values, gaps)) / base)


def component_gap(n_items, n_evidenced):
    """A one-sided component gap, section 2.4.

        gap_k = 1 - evidenced / in_scope

    Used for the search and consensus components, whose pairs have no seller
    side and whose instruments emit counts rather than ratings. The result
    lands on [0, 1] with a true zero, so it needs no rescaling.

    An instrument that put no items in scope leaves the gap undefined rather
    than zero. Nothing evidenced out of nothing counted is not symmetry.
    """
    n_items, n_evidenced = int(n_items), int(n_evidenced)
    if n_items < 0 or n_evidenced < 0:
        raise ValueError("counts cannot be negative")
    if n_evidenced > n_items:
        raise ValueError(
            "{} items carry evidence but only {} are in scope".format(
                n_evidenced, n_items))
    if n_items == 0:
        raise ValueError(
            "no items in scope, so this component's gap is undefined; "
            "section 2.4 refuses to read that as symmetry")
    return NormalizedGap(1.0 - float(n_evidenced) / n_items)


def friction_vector(f_search, f_consensus, f_implementation,
                    gap_search, gap_consensus, gap_implementation):
    """Both of Axiom I's quantities, computed together. 06-friction-vector.md.

    Level is the L1 norm of BASE friction. It is the asset specificity Axiom I
    bounds, a property of the deal rather than of what anyone currently knows
    about it, so discovery does not move it.

    Direction is the share of EFFECTIVE cost each component carries. It moves
    with the work, which is the whole point of amplifying per component: under
    one multiplier the proportions were fixed and no amount of discovery could
    change which motion a deal needed.

    `dominant` names the component holding at least DOMINANCE_THRESHOLD of
    effective cost, or "mixed" when none does. The threshold is chosen.
    """
    values = _check_components(f_search, f_consensus, f_implementation)
    gaps = (gap_search, gap_consensus, gap_implementation)
    base = sum(values)
    if base == 0:
        raise ValueError(
            "base friction is zero, so the vector has no direction")
    effective = effective_cost_per_component(*(values + gaps))
    direction = tuple(f * (1.0 + _require_normalized(g, "friction_vector"))
                      / effective for f, g in zip(values, gaps))
    dominant = "mixed"
    for name, share in zip(COMPONENTS, direction):
        if share >= DOMINANCE_THRESHOLD:
            dominant = name
    return FrictionVector(
        base=values, effective=effective, direction=direction,
        magnitude=base, gap=weighted_mean_gap(*(values + gaps)),
        dominant=dominant)


def reduced_cost(gap, a=A_RISK_AVERSION, c=0.0):
    """Reduced form, section 1.2.

        y = a * gap^2 + c

    Argumentative rather than diagnostic. It shows why discounting fails:
    because cost grows faster than linearly in uncertainty, cutting the
    constant term c cannot offset a large gap. It produces a number, not a
    diagnosis, so section 1.4's operating rule says do not use it to choose an
    intervention.

    `a` is anchored by analogy to prospect theory's lambda and is not fitted.
    Section 1.7 fixes the units: y, c and a are fractions of annual contract
    value. The default c=0 therefore means a deal with no direct cost, not a
    deal whose cost is unstated.

    `gap` must be a NormalizedGap.
    """
    gap = _require_normalized(gap, "reduced_cost")
    return a * gap ** 2 + c


def base_friction(gap, b, c):
    """Base friction as a function of the gap, section 1.3.

        F_base(gap) = c + b * gap

    The assumption the structural form leaves implicit. An uncertain buyer does
    not pay a surcharge on a fixed quantity of work; the uncertainty changes how
    much work exists.
    """
    gap = _require_normalized(gap, "base_friction")
    return c + b * gap


def effective_cost_expanded(gap, b, c):
    """The three-parameter expression the reduced form approximates, section 1.3.

        F_effective = (c + b*gap)(1 + gap) = b*gap^2 + (b + c)*gap + c

    The reduced form is this with the middle term dropped and a identified with
    b. Section 1.4 is explicit that dropping the linear term is not justified by
    that term being small: over the normalized operating range it is comparable
    to the quadratic term and sometimes larger. What survives, and what the
    Three Sales Levers argument depends on, is convexity.
    """
    gap_f = _require_normalized(gap, "effective_cost_expanded")
    return base_friction(gap, b, c) * (1.0 + gap_f)


# ==========================================================================
# theory/01-foundation/03-mathematical-models.md section 2
# The Bilateral Asymmetry Gap.
# ==========================================================================

def asymmetry_gap(i_seller, i_buyer):
    """Section 2.1.

        gap = I_seller + I_buyer

    A sum, not a difference. A deal where both sides are equally blind is not
    symmetric in any useful sense; it is maximally uninformed on both sides.
    The Asymmetry Scorecard carries a note recording that an earlier version
    computed a difference and scored exactly that deal as forecastable.

    Returns a raw quantity on whatever scale the two halves were measured on.
    Pass it through normalize_gap before either cost equation.
    """
    if i_seller < 0 or i_buyer < 0:
        raise ValueError("neither half of the gap can be negative")
    return i_seller + i_buyer


def seller_ignorance(u_tech, u_process, w_tech=W_TECH, w_process=W_PROCESS,
                     phi_tech=PHI_TECH, phi_process=PHI_PROCESS):
    """Section 2.2.

        I_seller = w_t * U_tech^phi_t + w_p * U_process^phi_p

    What the seller has not yet mapped about the buyer's architecture and
    operations, with both inputs on [0, 10]. Because both exponents are at
    least 1 the function is convex: unmapped technical complexity generates
    accelerating discovery risk rather than proportional discovery risk. The
    Blueprint targets this term.

    Note this is NOT the same quantity as the Asymmetry Scorecard's I_seller,
    which is the mean of four dimensions each scored 1 to 5 and therefore lands
    on [1, 5]. This form ranges to about 14.6 on its stated inputs. See the
    discrepancy note in models/README.md.
    """
    for name, value in (("u_tech", u_tech), ("u_process", u_process)):
        if not 0.0 <= value <= 10.0:
            raise ValueError("{} must lie on [0, 10]".format(name))
    if abs((w_tech + w_process) - 1.0) > 1e-9:
        raise ValueError("w_tech and w_process must sum to 1")
    if phi_tech < 1 or phi_process < 1:
        raise ValueError("acceleration exponents must be at least 1")
    return w_tech * u_tech ** phi_tech + w_process * u_process ** phi_process


def buyer_uncertainty(cv_roi, k_vendor, mu=MU_RETURN_UNCERTAINTY,
                      nu=NU_VENDOR_DOUBT, kappa=KAPPA_PROOF_DECAY):
    """Section 2.3.

        I_buyer = mu * (sigma_ROI / R_bar) + nu * exp(-kappa * K_vendor)

    Doubt about return variance and vendor capability. Proof reduces doubt with
    diminishing returns, and as proof accumulates the term approaches a floor
    of mu * cv_roi set by return variance alone.

    That floor is the model's most useful field implication: no quantity of
    costly signaling drives buyer uncertainty to zero while the return itself
    remains volatile. Past a point the seller stops investing in proof and
    starts working on the variance of the projected return. The Red Team
    targets K_vendor; the MIP targets sigma_ROI by bounding downside through
    staged gates.
    """
    if cv_roi < 0:
        raise ValueError("a coefficient of variation cannot be negative")
    if not 0.0 <= k_vendor <= 10.0:
        raise ValueError("k_vendor must lie on [0, 10]")
    if mu <= 0 or nu <= 0 or kappa <= 0:
        raise ValueError("mu, nu and kappa must all be positive")
    return mu * cv_roi + nu * math.exp(-kappa * k_vendor)


def buyer_uncertainty_floor(cv_roi, mu=MU_RETURN_UNCERTAINTY):
    """The limit of buyer_uncertainty as vendor proof grows without bound."""
    if cv_roi < 0:
        raise ValueError("a coefficient of variation cannot be negative")
    return mu * cv_roi


# ==========================================================================
# theory/01-foundation/03-mathematical-models.md section 3
# practice/01-field-assets/consensus-friction-calculator.md
# Consensus friction.
# ==========================================================================

def incentive_variance(scores):
    """Section 3.2, and the calculator's input 2.

        I_bar = mean(I_i)      Var = mean((I_i - I_bar)^2)

    Population variance, not the sample form. Each I_i is the stakeholder's
    utility from the initiative on [-1, 1], scored from the objectives they are
    measured on rather than the position they stated in a room containing the
    others. Stated positions converge under social pressure and measured
    objectives do not, so scoring from the meeting understates this term, and
    it understates it most in the polarized committees where it matters most.

    Bounded above by 1 because the scores are bounded on [-1, 1]. A computed
    value above 1 indicates an arithmetic error, not an unusually divided
    committee.
    """
    scores = list(scores)
    if not scores:
        raise ValueError("a committee needs at least one stakeholder")
    for s in scores:
        if not -1.0 <= s <= 1.0:
            raise ValueError(
                "stakeholder alignment {:g} is outside [-1, 1]".format(s))
    mean = sum(scores) / len(scores)
    return sum((s - mean) ** 2 for s in scores) / len(scores)


def consensus_friction(n, var_i, alpha=ALPHA_COORDINATION,
                       beta=BETA_COMMITTEE):
    """Two-term core form, section 3.1.

        F_consensus = alpha * N^beta * (1 + Var(I_i))

    N counts stakeholders holding veto power or direct evaluation
    responsibility. Title does not matter; veto power does. beta > 1 reflects
    communication channels growing as N(N-1)/2 rather than as N, so adding the
    sixth stakeholder costs more than adding the second.

    When every stakeholder holds identical alignment the variance term
    vanishes and friction reduces to the structural floor alpha * N^beta. Size
    alone imposes cost even under perfect agreement.

    Section 3.4 calls this two-term form "what the axioms require."
    """
    if n < 1:
        raise ValueError("committee size must be at least 1")
    if not 0.0 <= var_i <= 1.0:
        raise ValueError(
            "incentive variance {:g} is outside [0, 1]; a value above 1 "
            "indicates an arithmetic error".format(var_i))
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    if beta < 1.2 or beta > 2.0:
        raise ValueError("beta is documented on [1.2, 2.0]")
    return alpha * n ** beta * (1.0 + var_i)


def consensus_friction_field(n, var_i, technical_overlap,
                             alpha=ALPHA_COORDINATION, beta=BETA_COMMITTEE,
                             gamma_to=GAMMA_TECHNICAL_OVERLAP):
    """Three-term field form, section 3.4 and the calculator's main equation.

        F_consensus = alpha * N^beta * (1 + Var) * (1 + gamma_TO * TO)

    TO on [1, 5] scores architectural alignment among technical evaluators.
    The term exists because incentive variance under-captures a specific and
    common failure: two architects can both want the project to succeed, score
    identically on incentive alignment, and still deadlock on hosting model.
    Treating technical philosophy conflict as incentive conflict causes the
    model to score fractured engineering organizations as low-friction.

    Section 3.4 is explicit that this is a field refinement rather than core
    theory. The two-term form above is what the axioms require.
    """
    if not 1.0 <= technical_overlap <= 5.0:
        raise ValueError("technical overlap is scored on [1, 5]")
    if gamma_to < 0:
        raise ValueError("gamma_TO cannot be negative")
    core = consensus_friction(n, var_i, alpha=alpha, beta=beta)
    return core * (1.0 + gamma_to * technical_overlap)


def consensus_band(f_consensus):
    """Risk band from the calculator's table: low, medium or high."""
    if f_consensus < 0:
        raise ValueError("consensus friction cannot be negative")
    if f_consensus < 10.0:
        return "low"
    if f_consensus <= 25.0:
        return "medium"
    return "high"


def consensus_sensitivity_to_variance(n, alpha=ALPHA_COORDINATION,
                                      beta=BETA_COMMITTEE):
    """Section 3.3.

        d F_consensus / d Var = alpha * N^beta

    The return on reducing misalignment scales with N^beta. In a committee of
    three, aligning incentives produces a modest gain. In a committee of ten it
    produces the largest single reduction available to the seller, which is the
    quantitative case for running the Red Team on large committees
    specifically, and why the calculator escalates to executive sponsorship
    above a threshold rather than recommending more meetings.
    """
    if n < 1:
        raise ValueError("committee size must be at least 1")
    return alpha * n ** beta


# ==========================================================================
# theory/01-foundation/03-mathematical-models.md section 4
# Urgency decay.
# ==========================================================================

def decay_rate(lambda_inertia, e_external, gamma_r=GAMMA_RESPONSIVENESS):
    """Section 4.2.

        delta = lambda_inertia / (1 + gamma_r * E_external)

    With no external catalyst, decay runs at the full rate of organizational
    inertia. With an overwhelming catalyst it approaches zero and perceived
    value holds.

    The seller cannot change the buyer's inertia. The seller can find, name and
    quantify an external catalyst the buyer has not yet connected to this
    decision, which is the only term here a seller can move, and why the
    Blueprint asks for the economic event by name.

    gamma_r is the responsiveness factor and is distinct from gamma in the
    asymmetry drift equation. The glossary keeps them separate by subscript.
    """
    if not 0.1 <= lambda_inertia <= 2.0:
        raise ValueError("organizational inertia is documented on [0.1, 2.0]")
    if not 0.0 <= e_external <= 10.0:
        raise ValueError("external catalyst magnitude is documented on [0, 10]")
    if not 0.1 <= gamma_r <= 1.0:
        raise ValueError("responsiveness is documented on [0.1, 1.0]")
    return lambda_inertia / (1.0 + gamma_r * e_external)


def value_decay(v0, delta, t):
    """Section 4.1, and Axiom I's time dynamics.

        V_effective(t) = V_0 * exp(-delta * t)

    v0 is peak perceived value at the triggering event and t is elapsed months.
    As V decays the buyer's relative preference shifts back toward the next
    best alternative, including building it themselves.
    """
    if delta < 0:
        raise ValueError("the decay rate cannot be negative")
    if t < 0:
        raise ValueError("elapsed time cannot be negative")
    return v0 * math.exp(-delta * t)


def asymmetry_drift(gap0, gamma, t):
    """The Constitution's asymmetry drift, and section 1.5's note on it.

        gap_hat(t) = gap_hat(0) + gamma * t

    Pre-close this is the Axiom II half of the Decay Clock: information goes
    stale, raising the multiplier on friction. Post-close, section 7.2 of
    05-seller-surplus-model.md reads the same equation as the erosion of an
    incumbent's information advantage, where gamma runs on staff turnover,
    workflow change, and systems the seller never saw installed. Net Revenue
    Retention is that document's phrase for this equation run past signature.

    Returns a NormalizedGap, which may exceed 1: the scorecard measures a point
    in time and cannot observe drift beyond its own range.
    """
    gap0 = _require_normalized(gap0, "asymmetry_drift")
    if gamma < 0:
        raise ValueError(
            "gamma cannot be negative; absent maintenance the gap rebuilds, "
            "and C_sustain holds gamma down rather than reversing it")
    if t < 0:
        raise ValueError("elapsed time cannot be negative")
    return NormalizedGap(gap0 + gamma * t)


def deal_surplus(v_effective, v_next_best, f_effective):
    """The Surplus equation, Constitution part III.

        S = (V_effective(t) - V_next_best) - F_effective

    Must exceed 0 for the deal to close. The first bracket is
    OC_switching, the opportunity cost of staying with the status quo.
    """
    return (v_effective - v_next_best) - f_effective


# ==========================================================================
# practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md
# Retrospective execution metrics. Every threshold, weight and coefficient on
# that page is a reasoned starting value; none is fitted to booked deal data.
# ==========================================================================

def friction_allocation_ratio(h_pre, h_post):
    """FAR, section 1.

        FAR = H_pre / (H_pre + H_post)

    The share of total implementation effort spent before signature. Reference
    band 0.60 to 0.75. Below 0.60 the organization is discovering the buyer's
    environment after committing to a delivery date. Above 0.75, either a
    Turnkey deal received ILG treatment or pre-sale work is being performed
    that the buyer never asked for.

    FAR is blind to scale. An engagement spending 10 pre-sale and 5 post-sale
    hours scores identically to one spending 1,000 and 500, so always report it
    alongside the total. A high FAR on a trivial hour count means the deal was
    small, not that the motion was well run.
    """
    if h_pre < 0 or h_post < 0:
        raise ValueError("logged hours cannot be negative")
    total = h_pre + h_post
    if total == 0:
        raise ValueError(
            "FAR is undefined with no logged hours; the ratio only becomes "
            "meaningful once total effort is proportional to the deal's asset "
            "specificity")
    return h_pre / total


def far_in_band(far):
    """Whether FAR sits inside the reference band of 0.60 to 0.75.

    Section 6.4 records that the band itself is untested: it should be
    regressed against realized 90-day launch success, and removed rather than
    defended if no plateau appears.
    """
    return 0.60 <= far <= 0.75


def buyer_commitment_velocity(s_dept, d_prov, n):
    """BCV, section 2.

        BCV = S_dept / ((D_prov + 1) * N^0.5)

    How quickly the buyer mobilizes internal resources once asked. S_dept
    counts departments that supplied a named participant, D_prov is calendar
    days from request to first delivered artifact or confirmed attendee, and N
    is total committee size.

    The N^0.5 denominator is a correction rather than decoration. The canvas
    form was S_dept / (D_prov + 1), which rewards engaging more departments and
    so inverts Axiom II: the consensus model treats stakeholder count as a cost
    driver. Uncorrected, an organization could raise its score by dragging more
    people into rooms, which the Consensus Friction Calculator correctly scores
    as worse.

    The +1 guards against division by zero on same-day response. It is a
    convention, not a modelled quantity.
    """
    if s_dept < 0:
        raise ValueError("department count cannot be negative")
    if d_prov < 0:
        raise ValueError("provisioning days cannot be negative")
    if n < 1:
        raise ValueError("committee size must be at least 1")
    return s_dept / ((d_prov + 1.0) * math.sqrt(n))


def risk_mitigation_score(n_identified, n_unresolved):
    """RMS, section 3.

        RMS = 1 - N_unresolved / N_identified

    The share of discovered edge cases closed before signature.

    This form corrects an arithmetic error the document records. The canvas
    version read N_edge / (N_edge + N_unresolved), which double-counts, because
    unresolved cases are a subset of identified cases and so appear in both
    numerator and denominator. A Red Team that identified ten edge cases and
    resolved none scored 10/20 = 0.50 under that form, reporting half the risk
    mitigated when in fact none was. This form returns 0.

    RMS rewards shallow discovery and must never be read alone. A workshop
    surfacing two edge cases and closing both scores 1.00; one surfacing forty
    and closing thirty-five scores 0.875. The lazier workshop wins. Report
    n_identified next to the score every time and treat a low count as the
    finding: below roughly eight on a genuine Structural deal the workshop did
    not do its job, and the score carries no information however high it is.
    """
    if n_identified < 0 or n_unresolved < 0:
        raise ValueError("edge case counts cannot be negative")
    if n_unresolved > n_identified:
        raise ValueError(
            "unresolved edge cases are a subset of identified ones, so "
            "{} unresolved of {} identified is impossible".format(
                n_unresolved, n_identified))
    if n_identified == 0:
        raise ValueError(
            "RMS is undefined when nothing was identified; a Red Team that "
            "surfaced no edge cases is the finding, not a score of 1.0")
    return 1.0 - n_unresolved / n_identified


MIN_CREDIBLE_EDGE_CASES = 8


def rms_is_credible(n_identified):
    """Whether the edge-case count clears the shallow-Red-Team heuristic."""
    return n_identified >= MIN_CREDIBLE_EDGE_CASES


def scope_variance_index(t_actual, t_scoped, c_orders):
    """SVI, section 4. Lower is better.

        SVI = |T_actual - T_scoped| / T_scoped + 0.25 * C_orders

    The absolute value penalizes early delivery as heavily as late delivery,
    which is deliberate: finishing in half the scoped time means the estimate
    was wrong, and a wrong estimate on the optimistic side produces the same
    buyer-facing credibility loss as one on the pessimistic side.

    The 0.25 coefficient on change orders is chosen with no source. It encodes
    a judgment that one change order is worth about as much scope instability
    as a 25 percent schedule miss.
    """
    if t_scoped <= 0:
        raise ValueError("scoped duration must be positive")
    if t_actual < 0:
        raise ValueError("actual duration cannot be negative")
    if c_orders < 0:
        raise ValueError("change order count cannot be negative")
    return abs(t_actual - t_scoped) / t_scoped + 0.25 * c_orders


def normalize_bcv(bcv, bcv_ref=BCV_REF_DEFAULT):
    """Section 5. BCV_hat = min(BCV / BCV_ref, 1).

    BCV_ref is the trailing median across your last twenty closed Structural
    deals. Until twenty exist, the default of 0.5 applies and every reported
    figure is marked provisional.
    """
    if bcv < 0:
        raise ValueError("BCV cannot be negative")
    if bcv_ref <= 0:
        raise ValueError("the BCV reference must be positive")
    return min(bcv / bcv_ref, 1.0)


def normalize_svi(svi):
    """Section 5. SVI_hat = min(SVI, 1).

    SVI caps at 1 because a 100 percent schedule overrun is already a total
    scoping failure, and allowing the term to run higher would let one
    catastrophic project dominate a cohort average.
    """
    if svi < 0:
        raise ValueError("SVI cannot be negative")
    return min(svi, 1.0)


def friction_efficiency_index(far, bcv, rms, svi, bcv_ref=BCV_REF_DEFAULT):
    """The composite, section 5.

        FEI = 100 * (0.35*FAR + 0.25*BCV_hat + 0.25*RMS + 0.15*(1 - SVI_hat))

    The weights sum to 1.00 by construction, so the index is bounded on
    [0, 100] once both normalizations are applied. They have no empirical
    basis: the parameter reference states the split is chosen.

    Read the four components before the composite. Any weighted index can hide
    an offsetting pair, and the common one here is a high FAR carrying a low
    RMS, which produces a respectable score on top of an expensive, shallow
    process. The composite tracks one organization's direction over time. The
    components tell you where to intervene.
    """
    if not 0.0 <= far <= 1.0:
        raise ValueError("FAR is a ratio on [0, 1]")
    if not 0.0 <= rms <= 1.0:
        raise ValueError("RMS is bounded on [0, 1]")
    w_far, w_bcv, w_rms, w_svi = FEI_WEIGHTS
    return 100.0 * (
        w_far * far
        + w_bcv * normalize_bcv(bcv, bcv_ref)
        + w_rms * rms
        + w_svi * (1.0 - normalize_svi(svi))
    )


def fei_band(fei):
    """Reading from the composite table: front-loaded, mixed or late."""
    if not 0.0 <= fei <= 100.0:
        raise ValueError("FEI is bounded on [0, 100]")
    if fei > 75.0:
        return "front-loaded"
    if fei >= 50.0:
        return "mixed"
    return "late"


# ==========================================================================
# practice/01-field-assets/milestone-valuation-model.md
# ==========================================================================

def residual_uncertainty(x0, mus):
    """The uncertainty decay chain.

        x_m = x_0 * product over k=1..m of (1 - mu_k)

    Each mu_k applies to what remains rather than to the original gap, which is
    why the reference table's residual compounds downward rather than stepping
    linearly. x_0 is the normalized IMPLEMENTATION gap from the Asymmetry
    Scorecard, not the deal-level weighted mean: the gates resolve
    implementation uncertainty specifically.

    A gate written so loosely that no outcome fails it resolves no uncertainty,
    so its mu is effectively zero regardless of what the plan claims.
    """
    x0_f = _require_normalized(x0, "residual_uncertainty")
    x = x0_f
    for i, mu in enumerate(mus, start=1):
        if not 0.0 <= mu <= 1.0:
            raise ValueError(
                "stage {} resolves a fraction of remaining uncertainty, so "
                "mu must lie on [0, 1], not {:g}".format(i, mu))
        x *= (1.0 - mu)
    return NormalizedGap(x)


def residual_schedule(x0, mus):
    """Residual uncertainty entering each stage, as a list.

    Element 0 is x_0 itself, element m is the residual after stage m has
    cleared. Reproduces the reference stage structure table.
    """
    x0_f = _require_normalized(x0, "residual_schedule")
    out = [NormalizedGap(x0_f)]
    running = x0_f
    for i, mu in enumerate(mus, start=1):
        if not 0.0 <= mu <= 1.0:
            raise ValueError(
                "stage {} mu must lie on [0, 1], not {:g}".format(i, mu))
        running *= (1.0 - mu)
        out.append(NormalizedGap(running))
    return out


def stage_surplus(p_m, v_gross_m, x_m, c_m, a=A_RISK_AVERSION):
    """The stage equation.

        S_m = p_m * [V_gross,m - (a * x_m^2 + c_m)]

    p_m comes from your own delivery history in comparable environments,
    V_gross,m is the incremental value the buyer realizes on completing the
    stage, x_m is residual uncertainty entering it, and c_m is the payment
    allocated to it. The bracket is the reduced-form cost of section 1.2 with
    the stage's own payment as the constant term.

    UNITS. v_gross_m, c_m and a are all fractions of annual contract value, per
    03-mathematical-models.md section 1.7. Passing a payment as 25 rather than
    0.25 does not scale the answer, it reverses it. The uncertainty term drops
    to five percent of the first gate's payment where it should be five times
    that payment, and the model then recommends demanding everything at
    signature. Nothing here can detect the error, because both readings are
    arithmetically valid.

    `a` is anchored at 2.25 by analogy and is not fitted.
    """
    if not 0.0 <= p_m <= 1.0:
        raise ValueError("a stage probability must lie on [0, 1]")
    x_m = _require_normalized(x_m, "stage_surplus")
    return p_m * (v_gross_m - (a * x_m ** 2 + c_m))


# ==========================================================================
# theory/01-foundation/05-seller-surplus-model.md
# Nothing in this section is fitted, and section 6 says so in stronger terms
# than 03-mathematical-models.md: this model has no parameter anchored in
# published literature at all.
# ==========================================================================

def seller_surplus(p_close, v_contract, c_deliver, c_invest):
    """Section 2.

        S_seller = p_close * (V_contract - C_deliver) - C_invest

    The asymmetry sits in the last two terms. C_deliver is contingent, incurred
    only against revenue. C_invest is not: it leaves the building before anyone
    signs, and it leaves whether p_close resolves to one or to zero.

    Both parties face a boundary and both must clear it. The Constitution's
    S > 0 governs whether the buyer will transact. This one governs whether the
    seller should want them to. A deal sitting comfortably inside the buyer's
    potential well can sit outside the seller's, and the seller who closes it
    has done accretive work for the customer and dilutive work for their own
    firm.

    p_close is not directly observable. Section 6 is explicit that producing a
    number and calling it a probability is not a use this model supports.
    """
    if not 0.0 <= p_close <= 1.0:
        raise ValueError("p_close is a probability on [0, 1]")
    if c_invest < 0:
        raise ValueError("pre-signature investment cannot be negative")
    return p_close * (v_contract - c_deliver) - c_invest


def quasi_rent(c_invest, r_redeploy):
    """Section 3.

        Q = C_invest - R_redeploy

    C_invest overstates the exposure. The correct measure is the appropriable
    quasi-rent, where R_redeploy is the value of that work redeployed
    elsewhere: reusable connectors, a reference architecture, domain knowledge
    that transfers to the next deal in the segment.

    Q is what a buyer can extract by threatening to walk after the engineering
    is spent, and it is the number that belongs in a risk review. Two
    engagements consuming identical hours carry different exposure when one
    produces a connector the seller ships to every subsequent customer and the
    other produces a mapping to a schema that exists in exactly one hospital.

    R_redeploy has no scoring method anywhere in this repository. It is a
    caller-supplied input on purpose: inventing a rubric here would put a
    number into a risk review that no document backs. It is listed as an open
    question in section 8 of that document and in models/README.md.
    """
    if c_invest < 0:
        raise ValueError("pre-signature investment cannot be negative")
    if r_redeploy < 0:
        raise ValueError("redeployable value cannot be negative")
    if r_redeploy > c_invest:
        raise ValueError(
            "redeployable value cannot exceed the investment that produced "
            "it; Q is what remains unprotected, and it floors at zero")
    return c_invest - r_redeploy


def marginal_investment_rule(dp_close_dc_invest, v_contract, c_deliver):
    """Section 4, evaluated.

        (d p_close / d C_invest) * (V_contract - C_deliver) > 1

    Spend the next increment while a unit of pre-signature engineering raises
    the close probability enough that the expected gross margin gain exceeds
    the unit spent. Stop when it does not.

    **This function cannot be evaluated from anything in this repository.**
    The derivative is not observable and no record of scored deals exists. The
    caller must supply it, and supplying a guess produces a guess. Prefer
    required_marginal_close_gain below, which is the direction section 6
    actually endorses.
    """
    return dp_close_dc_invest * (v_contract - c_deliver) > 1.0


def required_marginal_close_gain(v_contract, c_deliver):
    """Section 4, inverted into the question a manager can actually ask.

        d p_close / d C_invest > 1 / (V_contract - C_deliver)

    Section 6 names this as the model's real use: "a manager can use section 4
    to ask what would have to be true about d p_close / d C_invest for this
    spend to make sense, and can compare that answer against experience."

    Returns the threshold the derivative must clear, in close-probability per
    unit of currency invested. It asserts nothing about whether a given deal
    clears it, which is the point. Producing a number and calling it a
    probability is what section 6 rules out.
    """
    margin = v_contract - c_deliver
    if margin <= 0:
        raise ValueError(
            "gross margin is not positive, so no pre-signature investment "
            "can satisfy the marginal rule at any derivative")
    return 1.0 / margin


def repeated_seller_surplus(r, v, c_deliver, c_sustain, rho, c_invest):
    """Section 7, the repeated game.

        S_seller = sum over t of r_t (V_t - C_deliver,t - C_sustain,t)
                   / (1+rho)^t   -   C_invest

    Subscription businesses do not have single transactions. r_t is the
    probability the relationship is live in period t, with r_1 equal to
    p_close. C_sustain is the ongoing relationship investment that holds the
    asymmetry drift rate gamma down, and section 7.2 argues it is not overhead:
    it is what defends the incumbent's information advantage, which is the
    durable asset rather than lock-in.

    The single-shot form of section 2 is this expression with T = 1 and
    C_sustain = 0. test_ilg_models.py asserts that identity.

    rho is a policy choice rather than a measurement, and r_t is no better
    observed than p_close.
    """
    lengths = {len(r), len(v), len(c_deliver), len(c_sustain)}
    if len(lengths) != 1:
        raise ValueError(
            "r, v, c_deliver and c_sustain must cover the same periods")
    if rho < 0:
        raise ValueError("the discount rate cannot be negative")
    if c_invest < 0:
        raise ValueError("pre-signature investment cannot be negative")
    total = 0.0
    for t, (r_t, v_t, cd_t, cs_t) in enumerate(
            zip(r, v, c_deliver, c_sustain), start=1):
        if not 0.0 <= r_t <= 1.0:
            raise ValueError(
                "the survival probability in period {} is not on "
                "[0, 1]".format(t))
        total += r_t * (v_t - cd_t - cs_t) / (1.0 + rho) ** t
    return total - c_invest


def cooperation_threshold(temptation, reward, punishment):
    """Axiom III's cooperation condition.

        delta_discount > (T - R) / (T - P)

    Returns the threshold the party's discount factor must exceed. Section 7.1
    of the seller model uses it to argue that lock-in is a liability: raising
    the buyer's switching cost raises the seller's temptation payoff T, which
    raises this threshold, so the arrangement becomes harder to sustain exactly
    as the seller's position strengthens.
    """
    if not punishment < reward < temptation:
        raise ValueError(
            "the payoff structure requires P < R < T for the condition to "
            "describe a prisoner's dilemma")
    return (temptation - reward) / (temptation - punishment)


# ==========================================================================
# practice/01-field-assets/process-calculator.md (v4.2)
#
# Routing is modelled as the document writes it, which is not a threshold on
# the summed score. Two gates run before divergence and can short-circuit to
# PLG; market stage is an independent axis; and the divergence score is
# deliberately never added to the step 2 total, because summing magnitude and
# fit would let a large aligned deal and a small misaligned deal produce the
# same number, which is the specific confusion step 2b exists to prevent.
# ==========================================================================

SLG = "SLG"
PLG = "PLG"
ILG = "ILG"
SLG_WITH_ILG_ELEMENTS = "SLG with ILG elements creeping in"
CHAOS_TRAP = "Chaos Trap"

NASCENT, TRANSITIONAL, MATURE = "nascent", "transitional", "mature"

# Gate A answers: must the product fit a workflow the buyer has already
# encoded? Two of the three answers skip the divergence score entirely.
GATE_A_GREENFIELD = "greenfield"          # no encoded workflow exists
GATE_A_PRODUCT_ABSORBS = "product-absorbs"  # buyer encodes it inside the product
GATE_A_ENCODED = "encoded"                # continue to gate B

TriageResult = collections.namedtuple(
    "TriageResult",
    "motion cost_score deal_class market_stage divergence_scored flags reason")


def market_stage(yes_count):
    """Step 1. Score the market, not the deal.

    Three yes/no signals: a recognized category name, the buyer naming three or
    more vendors, and published playbooks or analyst coverage.

    Absence of competition often signals nascent rather than mature, because
    the buyer cannot name three vendors when the category itself does not exist
    yet. The document calls that the most common misclassification.
    """
    if yes_count not in (0, 1, 2, 3):
        raise ValueError("the market stage diagnostic has three yes/no signals")
    if yes_count <= 1:
        return NASCENT
    if yes_count == 2:
        return TRANSITIONAL
    return MATURE


def cost_score(integration_depth, workflow_change_scope,
               consensus_complexity, retention_horizon):
    """Step 2. Four factors scored 1 to 5, summed to 4 to 20.

    Integration depth and workflow change scope target F_implementation,
    consensus complexity targets F_consensus, and retention horizon targets
    sustained F_implementation.

    These four measure how large the installation is. None of them measures how
    far the buyer's existing workflow sits from the one the product was built
    around, which is what step 2b scores separately.
    """
    factors = {
        "integration_depth": integration_depth,
        "workflow_change_scope": workflow_change_scope,
        "consensus_complexity": consensus_complexity,
        "retention_horizon": retention_horizon,
    }
    for name, value in factors.items():
        if value not in (1, 2, 3, 4, 5):
            raise ValueError("{} is scored 1 to 5, not {!r}".format(name, value))
    return sum(factors.values())


def deal_class(score):
    """Turnkey or Structural, from the step 2 total.

    4 to 9 is a Turnkey deal; 10 to 20 is a Structural deal. The glossary fixes
    k_threshold at 10.

    This is the Axiom I level claim and it answers how much apparatus the deal
    can carry. It does not select the motion: composition does that, and no
    equation settles it. Do not read the summed score as a motion selector.
    """
    if not COST_SCORE_MIN <= score <= COST_SCORE_MAX:
        raise ValueError(
            "the step 2 total runs {} to {}".format(COST_SCORE_MIN,
                                                    COST_SCORE_MAX))
    return "Turnkey" if score <= TURNKEY_MAX else "Structural"


def triage(workflow_maturity, market_yes_count,
           integration_depth, workflow_change_scope, consensus_complexity,
           retention_horizon, gate_a=GATE_A_ENCODED, gate_b_trialable=None,
           divergence=None, pilot_requested=False,
           product_automates_process=True):
    """Run the whole calculator and return a TriageResult.

    Order of operations, which the document fixes and which matters:

    0. The workflow maturity gate runs "before scoring anything." A level 1
       undefined workflow is a Chaos Trap when the product automates the
       process, and the route is to stop rather than to score.
    1. The pilot override then applies at any market stage: a buyer who asks
       for a pilot is signalling they perceive Structural-level risk regardless
       of how the seller scored the deal.
    2. Market stage. Nascent skips step 2 entirely, because the cost diagnostic
       does not apply until the buyer's problem is framed.
    3. The step 2 total, then the two gates, then divergence.

    Divergence is scored only when gate A answers "encoded" and gate B answers
    no. It is never added to the step 2 total.
    """
    flags = []

    # --- Step 0: workflow maturity gate --------------------------------
    if workflow_maturity not in (1, 2, 3):
        raise ValueError("workflow maturity is scored 1, 2 or 3")
    if workflow_maturity == 1:
        if product_automates_process:
            return TriageResult(
                motion=CHAOS_TRAP, cost_score=None, deal_class=None,
                market_stage=None, divergence_scored=False,
                flags=("chaos-trap",),
                reason="Step 0: no written process exists and the product "
                       "automates the process. Redirect to consulting or a "
                       "paid workshop to define the SOP first.")
        flags.append("undefined-workflow-product-supplies-medium")
    elif workflow_maturity == 2:
        flags.append("emergent-workflow-blueprint-must-reconstruct")

    # --- Step 3 override: pilot or proof of concept ---------------------
    if pilot_requested:
        return TriageResult(
            motion=ILG, cost_score=COST_SCORE_MAX,
            deal_class=deal_class(COST_SCORE_MAX),
            market_stage=market_stage(market_yes_count),
            divergence_scored=False,
            flags=tuple(flags + ["pilot-override"]),
            reason="Override rule: the prospect asked for a pilot or proof of "
                   "concept, which auto-scores 20 at any market stage. Pilots "
                   "are governed by the Red Team Protocol.")

    stage = market_stage(market_yes_count)

    # --- Step 1: nascent markets skip step 2 ----------------------------
    if stage == NASCENT:
        return TriageResult(
            motion=SLG, cost_score=None, deal_class=None, market_stage=stage,
            divergence_scored=False, flags=tuple(flags),
            reason="Step 1: the category is not yet legible, so the cost "
                   "diagnostic does not apply. A high cost score in a nascent "
                   "market does not mean ILG; educational friction dominates.")

    # --- Step 2: the cost diagnostic ------------------------------------
    score = cost_score(integration_depth, workflow_change_scope,
                       consensus_complexity, retention_horizon)
    klass = deal_class(score)

    if stage == TRANSITIONAL:
        if score >= 15:
            motion, reason = ILG, (
                "Step 3: transitional market at 15 to 20. Deal stakes are high "
                "enough to force ILG even before category maturity.")
        else:
            motion, reason = SLG_WITH_ILG_ELEMENTS, (
                "Step 3: transitional market at 4 to 14. The market is "
                "maturing in your favour, so weight the result toward ILG.")
        return TriageResult(
            motion=motion, cost_score=score, deal_class=klass,
            market_stage=stage, divergence_scored=False, flags=tuple(flags),
            reason=reason)

    # --- Mature markets: gates, then divergence -------------------------
    if gate_a not in (GATE_A_GREENFIELD, GATE_A_PRODUCT_ABSORBS,
                      GATE_A_ENCODED):
        raise ValueError("gate A answers greenfield, product-absorbs or encoded")

    gate_a_passed = gate_a in (GATE_A_GREENFIELD, GATE_A_PRODUCT_ABSORBS)
    gate_b_passed = bool(gate_b_trialable) and not gate_a_passed
    gates_passed = gate_a_passed or gate_b_passed
    divergence_governs = not gates_passed

    if divergence_governs:
        if gate_b_trialable is None:
            raise ValueError(
                "gate A answered 'encoded', so gate B must be answered before "
                "divergence can be scored")
        if divergence not in (1, 2, 3, 4, 5):
            raise ValueError(
                "both gates failed, so divergence governs and must be scored "
                "1 to 5")

    if score >= STRUCTURAL_MIN:
        if divergence_governs and divergence <= 2:
            flags.append("possible-over-frictioning")
        return TriageResult(
            motion=ILG, cost_score=score, deal_class=klass, market_stage=stage,
            divergence_scored=divergence_governs, flags=tuple(flags),
            reason="Step 3: mature market at 10 to 20." + (
                " Large but aligned: flag at manager review to confirm the "
                "full artifact chain earns its cost."
                if "possible-over-frictioning" in flags else ""))

    # Score 4 to 9 in a mature market.
    if gate_a_passed:
        return TriageResult(
            motion=PLG, cost_score=score, deal_class=klass, market_stage=stage,
            divergence_scored=False, flags=tuple(flags),
            reason="Step 2b gate A: there is no encoded workflow to misfit "
                   "against, so divergence has no reference point. Route on "
                   "magnitude and market stage alone.")
    if gate_b_passed:
        return TriageResult(
            motion=PLG, cost_score=score, deal_class=klass, market_stage=stage,
            divergence_scored=False, flags=tuple(flags),
            reason="Step 2b gate B: the buyer can measure the gap themselves "
                   "and reverse the decision, so they will find the misfit "
                   "faster than the seller can prove its absence. Track churn "
                   "rather than implementation risk.")
    if divergence >= 4:
        return TriageResult(
            motion=ILG, cost_score=score, deal_class=klass, market_stage=stage,
            divergence_scored=True,
            flags=tuple(flags + ["hidden-structural"]),
            reason="Hidden Structural deal: the installation is small, so "
                   "every magnitude factor scores low, and the workflow "
                   "underneath it matches nothing the product assumes. This is "
                   "the under-frictioned failure mode the cost score alone "
                   "cannot see.")
    return TriageResult(
        motion=PLG, cost_score=score, deal_class=klass, market_stage=stage,
        divergence_scored=True, flags=tuple(flags),
        reason="Step 3: mature market at 4 to 9, gates failed, divergence 1 "
               "to 3. The buyer follows the category's usual shape.")
