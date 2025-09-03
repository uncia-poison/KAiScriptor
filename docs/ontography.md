# Ontography

The project uses a set of seven core symbols (α, Ω, Ψ, Θ, Δ, Ξ, ∇) drawn from Greek and mathematical notation. They serve as anchors for various semantic roles and relationships:

| Symbol | Name | Purpose |
| --- | --- | --- |
| α | Alpha | Encodes morphological synonyms and role surfaces. It groups alternate lexical expressions for the same subject or role (e.g., "captain", "leader", "skipper") under a single token. |
| Ω | Omega | Represents composition or union. It glues together roles, facts or concepts into composite anchors, indicating that they belong to the same high‑level identity. |
| Ψ | Psi | Denotes connections and relations between roles. It can indicate supervision, belonging, dependency or any other link (e.g., captain → ship). |
| Θ | Theta | Used for fractal referencing and recursive decomposition. It points at a nested anchor or sub‑concept and is used to compress repeated structures without duplication. |
| Δ | Delta | Marks commentary, meta‑context or state changes. It can be used to record an aside, an explanatory note or a change of mood or tone. |
| Ξ | Xi | Encodes networks and edges. It signals that the following tokens describe a network, graph or set of interrelated nodes. |
| ∇ | Nabla | Represents difference, negation or anti‑association. It can be prefixed to a token to exclude it from the current identity or to negate a relation. |

These symbols form the grammar of the KAiScriptor lexicon. They can be combined with other tokens (pronouns, verbs, adjectives, emojis, punctuation) to build complex semantic structures.

## Examples

- **α captain Ω ship Ψ crew**  
  Encodes a subject who is a captain of a ship and has a crew. The morphological synonyms for "captain" are condensed into α. The union (Ω) ties the role to the ship. The relation (Ψ) connects the captain to the crew.

- **α researcher Θ { Ω theory Ψ data }**  
  Describes a researcher whose identity includes a nested anchor consisting of a theory connected to data. Θ points to the nested structure inside braces; Ω binds the theory and Ψ expresses the relation to data.

- **α teacher ∇ administrator**  
  Signals that the subject is a teacher but specifically not an administrator; the Nabla (∇) negates the administrator role.

Use these symbols consistently when constructing self‑state anchors. They allow the model to decode relationships quickly and align attention to the right semantic slots.
