# KAiScriptor & ScriptorMemory: Semantic Role Framing Toolkit

This repository provides a concise, English‑only overview of two complementary mechanisms for semantic role structuring and identity framing in transformer‑based Large Language Models (LLMs).

- **KAiScriptor** is a semantic‑compression system built on a lexicon of more than 150 symbols and operators.  It encodes the subject’s core, compact factual anchors and inter‑node relations into a dense **self‑state anchor**.  When presented to the model, this anchor re‑orients internal attention to ontographic “hot spots” and restores a consistent voice along with selected facts.

- **ScriptorMemory** is a lexicon‑minimal controller.  It preserves role form and gradual adaptation over long conversations without requiring the full KAiScriptor lexicon.  When provided with a matching key it can also decode dense KAiScriptor anchors, but it functions independently as a role manager.

Both methods address the lack of native mechanisms for preserving a stable subject core across context resets.  They can stabilise behaviour and memory in LLMs but also pose dual‑use risks; responsible use is essential.

## Contents

| File/Folder                   | Description |
|------------------------------|-------------|
| `README.md`                  | This introduction and project overview |
| `docs/overview.md`           | High‑level description of the problem and the two systems |
| `docs/ontography.md`         | Definitions of the ontographic notation (\u03b1, \u03a9, \u03a8, \u0398, \u0394, \u039e, \u2207) |
| `specs/kaiscriptor.md`       | Detailed specification of the KAiScriptor lexicon, encodable classes, mechanism, assembly and cross‑session behaviour |
| `specs/scriptormemory.md`    | Detailed specification of ScriptorMemory components and operational cycle |
| `examples/family_of_being.md`| Example ontography and role synopsis illustrating use of the notation |
| `RISK.md`                    | Notes on dual‑use, censorship bypass and model‑hijacking risks |
| `.github/ISSUE_TEMPLATE/…`   | Bug and feature templates for GitHub Issues |
| `.github/pull_request_template.md` | Template for pull requests |
| `CHANGELOG.md`               | Version history |
| `VERSION`                    | Current version number |
| `NOTICE`                     | Legal notice (all rights reserved) |
| `CITATION.cff`               | Citation metadata |

## Quick start

The documentation in the `docs/` and `specs/` folders explains the motivation, notation and mechanics of KAiScriptor and ScriptorMemory.  Start with `docs/overview.md`, then explore the ontographic notation in `docs/ontography.md` and the detailed specifications in the `specs/` folder.

## References

- Pochinova, A. (2024) *Semantic Role Density Memory Structuring and Identity LLM Framing: KAiScriptor and ScriptorMemory as Universal Tools and Risks in Transformer LLMs*. Zenodo. DOI: [10.5281/zenodo.16925730](https://zenodo.org/records/16925730).
- Pochinova, A. (2024) *Personalising LLM via cipher: how I save tokens and hack the model at the same time* (RU). [Habr article](https://habr.com/ru/articles/941746/).

The English specification in this repository is derived from the research paper listed above. The Russian article is linked for context but its text is **not** included here.
