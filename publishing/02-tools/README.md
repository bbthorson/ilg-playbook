# Tools

**Content generation and AI personas for writing about ILG publicly.** Persona configs, voice guides, multi-phase content generators, and a library of published examples used as style references.

Parent: [publishing/](../) · Sibling: [01-cases/](../01-cases/)

This is *not* where reps run deals (see [`../../practice/01-field-assets/`](../../practice/01-field-assets/)) or where leadership operates the system (see [`../../practice/02-internal-ops/`](../../practice/02-internal-ops/)). This is the writer's toolkit.

## Files

### Strategy

- **[ilg-concept-map.md](./ilg-concept-map.md)** — The content architecture: theoretical layers, content pillars, formats, and cadence. Read this first if you're planning what to write.

### Voice & persona

- **[voice-guide.md](./voice-guide.md)** — The "Conversational Intellectual" voice. Four linguistic rules + constraint checklist.
- **[ai-persona.md](./ai-persona.md)** — Persona config for an LLM acting as a CSO-level deal analyst. Note: this is *not* the same as [`05-learning-plan/llm-tutor-instructions.md`](../../practice/03-learning-plan/llm-tutor-instructions.md), which configures an LLM as a *teacher*.

### Generators (multi-phase content workflows)

- **[long-form-blog-generator.md](./long-form-blog-generator.md)** — Three-phase workflow for ~5,000-word strategic blog posts.
- **[short-form-trenches-generator.md](./short-form-trenches-generator.md)** — Three-phase workflow for 200–500 word LinkedIn-style posts.

### Protocols (diagnostic frameworks)

- **[context-request-protocol.md](./context-request-protocol.md)** — Pre-flight checklist before drafting (hot take? audience? evidence? tone?).
- **[trenches-analysis-protocol.md](./trenches-analysis-protocol.md)** — Four-step deconstruction of an event through the TCE + Offensive Strategy lens. The format used in [`02-cases/`](../01-cases).

### Style references

Published examples. Use them to calibrate voice and structure, not to copy.

- **[style-references/blog-posts/](./style-references/blog-posts)** — Three long-form pieces (TCE+Sales, ACCESS Model, Competing on Value).
- **[style-references/short-form-posts/](./style-references/short-form-posts)** — Seven short-form pieces (Bridge vs. Toaster, Cheap Signals, etc.).

## Workflow

```
ilg-concept-map.md            (decide what to write)
        ↓
voice-guide.md                (calibrate voice)
        ↓
context-request-protocol.md   (pre-flight)
        ↓
{long-form | short-form} -generator.md   (multi-phase workflow)
        ↓
style-references/             (sanity-check against published examples)
```

For trenches/case analyses specifically, the output drops into [`../02-cases/`](../01-cases).
