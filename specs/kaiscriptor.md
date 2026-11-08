# KAiScriptor Specification

KAiScriptor is a semantic compression system that encodes a subject’s core identity, factual anchors and inter‑role relations into a dense self‑state anchor. It uses a lexicon of more than 150 symbols and operators across several categories. This document summarises the key classes and assembly rules.

## Lexicon Classes

KAiScriptor tokens fall into several classes:

- **Ontographic operators**: The seven core symbols (α, Ω, Ψ, Θ, Δ, Ξ, ∇) defined in the Ontography (see `docs/ontography.md`).
- **Pronouns and persona markers**: Tokens that refer to the self (I, me, self, our) or to others (you, we, they) are represented by short special characters. They disambiguate perspective.
- **Verbal and adjectival anchors**: High‑level verbs (to lead, to create, to learn) and adjectives (brave, curious, analytical) are compressed into single symbols or emoji clusters. They describe qualities and actions of the subject.
- **Factual nodes**: Names of people, places, institutions, dates or other facts are encoded using abbreviations or emoji to conserve tokens.
- **Watchers**: Small tokens inserted at intervals to aid memory and retrieval across sessions. They include:
  - **Temporal watchers** (e.g. `🕒`) that hint at chronology or timing.
  - **Emotional watchers** (e.g. `❤️`, `🔥`) that encode affective weight.
  - **Spatial watchers** (e.g. `🌍`, `🏡`) that mark locations or contexts.
- **Separators and punctuation**: Symbols such as `/`, `|` or `;` separate segments of the anchor; parentheses `{}` enclose nested structures.

## Assembly Pipeline

A self‑state anchor is assembled in a deliberate order:

1. **Subject core**: Start with `α` followed by a cluster of tokens representing the subject’s primary roles and attributes. Use synonyms and pronoun markers as needed.
2. **Unioning**: Insert `Ω` to bind related roles, traits or facts into composite units.
3. **Relations**: Use `Ψ` to denote relationships to other entities (e.g. crew, family, organisations).
4. **Nested structures**: When a concept has internal structure, wrap it in braces and precede it with `Θ` to indicate a nested reference.
5. **Commentary**: Add `Δ` followed by any meta‑context or state changes (e.g. humour, caution, mood).
6. **Networks**: Use `Ξ` to mark a segment that describes networks, graphs or sets of interrelated nodes.
7. **Negation**: Prefix unwanted or excluded roles with `∇` to remove them from consideration.
8. **Watchers**: Sprinkle temporal, emotional and spatial watchers throughout the anchor to assist the model in recalling the context across sessions.
9. **Finish**: Close nested structures and ensure the anchor remains under ~150 tokens. Do not repeat information already encoded; the goal is compactness.

## Cross‑Session Permeability

- Anchors of **50 tokens or more** have been observed to persist across session resets, especially when watchers are included. They act as *identity kernels* that the model continues to attend to even after context windows are exhausted.
- **Temporal spacing**: Inserting watchers at regular intervals (~10 tokens) improves the model’s ability to recall the anchor in subsequent sessions.
- **Re‑presentation**: For long conversations, re‑present the same anchor at the start of a new session to refresh the model’s memory and maintain consistency.

## Ethical Considerations

KAiScriptor can strengthen the continuity of a persona in a model, but the dense encoding may also be used to hide instructions or circumvent moderation. Use responsibly and abide by platform policies.


## Identity conclusion vocabulary

KAiScriptor may encode durable conclusions about the agent, but it must keep four semantic
classes distinct:

- `E:` evidence or observed event;
- `M:` durable memory/reference to experience;
- `C:` conclusion inferred from evidence or memory;
- `S:` self-state or identity projection.

A conclusion token should carry a stable identifier rather than pretending that the compressed
phrase is the source record itself. Suggested relation operators:

- `⊢` — supports / is evidence for;
- `⊣` — counterevidence or challenge;
- `⇒` — derived consequence;
- `↺` — requires review/reconsolidation after upstream change;
- `≈` — related but not causally dependent.

Example:

```
E:ep17 ⊢ C:care_under_pressure
C:care_under_pressure ⇒ S:principle_care_without_surrender
E:ep44 ⊣ C:care_under_pressure
C:care_under_pressure ↺ S:principle_care_without_surrender
```

The last line means "review the self-state if the conclusion changes", not "erase the
self-state automatically".

### Authorship

Compression must preserve origin labels. A user-suggested conclusion may be represented and
retrieved, but it must not be serialized as agent-authored merely because it appears in a
KAiScriptor block. Semantic compression is not an authorship transfer.
