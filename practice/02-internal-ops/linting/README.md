# Linting

**Automated enforcement of the repo's content conventions.** Two independent checkers cover different failure classes. Run both before opening a PR.

Parent: [02-internal-ops/](../) · Rules they enforce: [voice-guide.md](../../../publishing/02-tools/voice-guide.md) and [CLAUDE.md](../../../CLAUDE.md)

## The two checkers

| Checker | Catches | Needs installing |
|---|---|---|
| `check_playbook.py` | Broken relative links, malformed LaTeX delimiters | No. Python 3, no dependencies. |
| Vale + the `ILG` style | Banned vocabulary, emojis, punctuation density, retired terms | Yes. See below. |

### check_playbook.py

Walks every `.md` file outside `.git`, `.claude`, `node_modules`, and `.gemini`. Reports two error classes and exits non-zero if either fires.

```bash
python3 practice/02-internal-ops/linting/check_playbook.py
```

1. **LaTeX integrity.** Unclosed inline or block math delimiters, and delimiters nested inside each other. The script knows the difference between math and a dollar sign, so currency amounts and template placeholders are not treated as opening a math block.
2. **Link validity.** Every relative link resolves to a file that exists. Web URLs, `mailto:`, and `#` anchors are skipped.

> [!NOTE]
> The script scans raw text and does not skip fenced code blocks. A math delimiter or a relative link inside an example will be validated as though it were real. Describe such examples in prose, or point them at a path that actually resolves from the file you are editing.

### Vale

```bash
brew install vale
vale .
```

Configuration lives in [`.vale.ini`](../../../.vale.ini) at the repo root, which points `StylesPath` here and applies the `ILG` style to all `*.md`. `MinAlertLevel` is `warning`, so warnings surface alongside errors.

## The ILG style rules

| Rule | Level | Enforces |
|---|---|---|
<!-- vale ILG.AntiHype = NO -->
| [`AntiHype.yml`](./styles/ILG/AntiHype.yml) | error | The banned-word list (*synergy*, *revolutionize*, *disruptive*, *cutting-edge*, *seamlessly*, *unlock potential*). Case-insensitive. |
| [`NoEmoji.yml`](./styles/ILG/NoEmoji.yml) | error | No emoji anywhere, across nine Unicode ranges including the variation selector. |
| [`Punctuation.yml`](./styles/ILG/Punctuation.yml) | warning | At most 3 em dashes plus semicolons combined. Applies to prose written for publication. |
| [`PunctuationReference.yml`](./styles/ILG/PunctuationReference.yml) | warning | At most 30, for reference and operational material. The repo-wide default. |
| [`RetiredTerms.yml`](./styles/ILG/RetiredTerms.yml) | error | Vocabulary the framework has replaced. Reports the current term to use. |
<!-- vale ILG.AntiHype = YES -->

This file quotes retired terms and banned words in order to document them, so it fences the relevant blocks with the mechanism described under [naming a retired term on purpose](#naming-a-retired-term-on-purpose). Read the raw source to see the fences.

### Why RetiredTerms exists

The link checker validates hrefs. It cannot see the prose around them. In August 2026 the repo carried 40 references to retired vocabulary, and every one of them sat inside a *correctly resolving* link:

<!-- vale ILG.RetiredTerms = NO -->
```markdown
[ILG Constitution - Axiom II (Law of Friction)](../../../theory/01-foundation/00-ilg-constitution.md)
```

The href was right. The name had been retired two Constitution versions earlier. Same pattern for directory numbering: link text said `04-internal-ops/` while the href pointed at the real `02-internal-ops/`. Both classes are invisible to a link checker and to a reader who trusts the link. `RetiredTerms.yml` is the rule that sees them.
<!-- vale ILG.RetiredTerms = YES -->

Neither class shows up in a `git diff` review either, because each one was correct when it was written.

### Adding a retired term

Whenever you rename an axiom, retire an equation variable, or renumber a directory, add a row to `swap:` in [`RetiredTerms.yml`](./styles/ILG/RetiredTerms.yml) **in the same commit as the rename**. That is the whole maintenance ritual.

<!-- vale ILG.RetiredTerms = NO -->
```yaml
swap:
  Law of Friction: Law of Uncertainty Inflation
```
<!-- vale ILG.RetiredTerms = YES -->

Keys are regexes and the match is case-sensitive. The `message` template fills `%s` with the retired term and then the replacement, so the fix is in the error output and nobody has to go looking for it.

### Building the list from history, not from the working tree

A rule built by scanning the current repo only catches drift that happens to still be visible. Names purged before the rule existed leave no trace in the tree, and they come back the moment someone reopens an old branch. Mine the history instead:

```bash
git log -p --all --format="" -- '*.md' | grep -oE 'Law of [A-Z][a-zA-Z]*( [A-Z][a-zA-Z]*)*' | sort | uniq -c | sort -rn
```

Adapt the pattern to whatever is being renamed. Read every hit before adding it, because the pattern will also catch legitimate prose. "Law of Conservation" appears in a published style reference as Tesler's Law and is not a retired axiom, so it stays out of the rule.

### Naming a retired term on purpose

Version-history notes sometimes need to name the old term. Fence the passage:

```markdown
<!-- vale ILG.RetiredTerms = NO -->
Renamed in v12 from the previous axiom name.
<!-- vale ILG.RetiredTerms = YES -->
```

The same form works for any rule in the table, for example `<!-- vale ILG.AntiHype = NO -->`.

Prefer this over deleting the row. An unenforced rule catches nothing.

## Current state of the repo

As of 2026-08-13, both checkers pass on all 89 files. A clean run is now the baseline, so any new hit is a real one:

| Rule | State |
|---|---|
| `RetiredTerms` | Clean. Zero hits repo-wide. |
| `NoEmoji` | Clean. |
| `AntiHype` | Clean, with three documented suppressions. See below. |
| `Punctuation` / `PunctuationReference` | Clean. The Constitution is the ceiling at 29 of 30. |

### The three AntiHype suppressions

Two are self-referential: [`CLAUDE.md`](../../../CLAUDE.md) and [`voice-guide.md`](../../../publishing/02-tools/voice-guide.md) have to print the banned-word list in order to document it, so both are fenced. This README's own rule table is fenced for the same reason.

The third is a scope exclusion in `.vale.ini` for `publishing/02-tools/style-references/`. Those files are published posts kept verbatim as a record of what went out, and two of them predate the anti-hype list. Editing published text to satisfy a later rule would make this repo disagree with what readers can actually see. The rule still applies in `publishing/03-drafts/`, which is the last point where a banned word can be removed before it ships.

The cost of that exclusion is real: a future post moved into `style-references/` carries its hype language in unchecked. The check that matters happens while the piece is still a draft.

### Why there are two punctuation rules

Vale's `occurrence` rule counts absolute instances and cannot be parameterized per directory, so a 480-line Constitution was held to the same budget as a 20-line LinkedIn post. Measuring the repo showed the limit of 3 was calibrated for short-form posts, where it still works: those files sit at a median of 3. It had simply been applied to everything.

Reference and operational material now carries a budget of 30 and is the repo-wide default. Prose written for publication opts back into 3, in `.vale.ini`:

- `publishing/02-tools/style-references/`
- `publishing/03-drafts/`

The limit of 30 was chosen so that all of `theory/` passes (the Constitution is the ceiling at 29) while genuine outliers still report. A limit set so nothing ever fires is not a relaxed rule, it is a deleted one.

**Do not raise either limit further to silence a warning.** Both encode house style. If a document legitimately needs more, that is a conversation about the document.

## Known limitations

- **`check_playbook.py` carries two hardcoded absolute paths**, a `file:///Users/brad-htd/Code/ilg-playbook` prefix strip and a `/Users/brad-htd/.gemini/antigravity` allowance. Links using either form will behave differently on another machine. Prefer relative links, which are portable and which the checker resolves correctly everywhere.
- **Neither checker is enforced in CI.** Both run locally on demand. Nothing blocks a merge today. `check_playbook.py` exits non-zero on failure, so it is ready to wire into a pre-commit hook or an action whenever you want that.
- **`Punctuation.yml` counts per file, not per section.** A long document at the limit will flag on the next legitimate em dash. Restructure into periods rather than raising the limit.
- **Neither checker validates claims against the Constitution.** They catch stale vocabulary, not stale reasoning. A description can use every current term and still describe a superseded version of an axiom, which is what happened to the root README's axiom list. That still needs a human reading both files side by side.
