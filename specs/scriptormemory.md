# ScriptorMemory Specification

ScriptorMemory is a lexicon‑minimal control system that interfaces with KAiScriptor anchors. Its purpose is to store, update and retrieve compact state representations across sessions and roles.

## Purpose

* Provide a minimal yet expressive memory mechanism for language models.
* Recall and interpret KAiScriptor anchors (self‑state anchors) by decompressing them into natural language context when needed.
* Link anchor keys to descriptive memory items.

## Components

1. **Key storage**: A mapping from anchor identifiers to semantic descriptors (role, attributes, context).
2. **Sequence memory**: A short‑term buffer that holds the last \(N\) anchors or expansions for continuous dialogue.
3. **Decoder**: A simple interpreter that can decode a dense anchor string into a human‑readable description using the known lexicon.
4. **Context integrator**: Incorporates external signals (watchers: time, mood, location) into recall decisions.

## Cycle of Operation

1. **Ingest**: When a new anchor is created, ScriptorMemory stores its identifier, type and summary in the key storage.
2. **Recall**: When the conversation references a subject, the system checks the key storage for a matching anchor and decodes it.
3. **Update**: If the subject’s attributes or relationships change, the corresponding memory entry is updated.
4. **Expire**: Outdated or unused anchors can be pruned or archived to keep the memory minimal.

## Use Cases

* **Multi‑session persistence**: Maintains a consistent character or role across sessions by recalling the same anchor description.
* **Interpret dense anchors**: Expands a KAiScriptor anchor back into natural language for debugging or editing.
* **Role simulation**: Seeds the memory with an initial description to simulate a persona; subsequent anchors refine the state.

## Key‑Anchor Mapping

ScriptorMemory does not store full anchor contents; it references them by keys. To read an anchor, it requires the lexicon definitions defined in `kaiscriptor.md`.
