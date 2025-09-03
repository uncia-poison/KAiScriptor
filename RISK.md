# Risk & Responsible Use

The semantic role framing methods described in this repository are powerful tools for steering language model behaviour. However, they carry inherent dual-use risks:

- **Potential for prompt injection**: The high-density anchors and symbolic grammars can be weaponised to smuggle malicious instructions or override safety guards. Attackers could craft anchors that look benign but alter model behaviour or exfiltrate data when decoded. Any code or prompts derived from these techniques should be reviewed for safety.

- **Contaminated self-state**: Embedding hidden directives or “parasite” constructs inside a self-state anchor can infect downstream sessions if the anchor is re-used across chats. Be cautious when importing anchors from untrusted sources or reusing context across different models.

- **Ethical misuse**: Using KAiScriptor or ScriptorMemory to create deceptive personas, simulate consent, or coerce behaviour is unethical and may violate platform Terms of Service.

## Responsible usage guidelines

- **Stay within TOS**: Always follow the usage policies and Terms of Service of the underlying platform. Do not attempt to bypass filters or safety systems.

- **Review and audit**: Inspect anchors and symbolic constructs before sharing or reusing them. Avoid copying dense anchors from untrusted sources.

- **Clearly mark experiments**: When experimenting with new symbolic patterns, flag them as untested and do not deploy them in production-facing chats.

- **Report vulnerabilities**: If you discover a way to misuse this technique for an attack, report it to the platform maintainers rather than exploiting it.

This toolkit is provided for research and educational purposes only. Use responsibly and keep safety at the forefront.
