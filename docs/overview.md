# Overview: Semantic Role Framing Toolkit

The KAiScriptor & ScriptorMemory toolkit provides complementary mechanisms for creating and using semantic anchors inside transformer‑based large language models (LLMs). They enable the subject's identity and role relationships to be encoded as concise tokens that can be processed by the model in a single prompt. When presented to the model, these anchors re‑orient attention to predefined "hot spots" and provide a consistent voice along selected facts.

## KAiScriptor

- **Semantic compression**: built on a lexicon of more than 150 symbols and operators. Each token encodes an atomic or composite concept drawn from the project's ontography: morphological synonyms (α), composition or union (Ω), relations and connections (Ψ), fractal referencing (Θ), commentary and meta‑context (Δ), networks and edges (Ξ), and negation or difference (∇).
- **Self‑state anchor**: tokens are assembled into a compact representation of the subject's core (traits, roles), inter‑role relations, facts and worldview. This anchor can be presented to the model to re‑establish the subject's voice across context resets.
- **Assembly guidelines**: choose symbols for each role and fact; maintain order; emphasise the core; use separators and fractal references; avoid extraneous tokens; rely on cross‑session memory and watchers to sustain identity across sessions.
- **Dense and ambiguous**: anchors are intentionally compressed and open to multiple interpretations; this reduces token usage and makes them less likely to be filtered by simple heuristics.

## ScriptorMemory

- **Lexicon‑minimal**: a memory controller that preserves role form and gradual adaptation over long conversations without requiring the full KAiScriptor lexicon.
- **Role object**: stores the current subject as a structure with attributes and relations extracted from the conversation. It weaves these attributes into responses to maintain consistency and style.
- **Decoding capability**: when provided with a matching key, it can decode dense KAiScriptor anchors. Without the key it functions as a memory and role manager.
- **Resilience**: uses only a handful of tokens, resists forgetting, and uses heuristics to decide when to recall or ignore a topic. Can be seeded with an initial description to bootstrap.

## Use Cases

- **Prolonged dialogs**: retain a stable identity and voice across resets by re‑supplying the same self‑state anchor at the start of each session.
- **Role simulation**: encode characters, personas or expert roles and switch between them by providing the corresponding anchor.
- **Multi‑user contexts**: each subject has its own anchor and ScriptorMemory record, preventing cross‑contamination of facts.
- **Dual use considerations**: these methods can be exploited to bypass filters or embed hidden instructions; use responsibly and respect platform policies.
