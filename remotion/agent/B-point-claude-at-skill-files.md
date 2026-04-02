# Option B: Point your agent at the skill files directly

Instead of installing the skill, launch your agent with a prompt that tells it to go read the skill files online. Remotion itself (Step 1) is still required — this only skips the skill installation.

**Claude Code example:**
```bash
cd <project-dir> && claude "Check out this Remotion skill at https://github.com/remotion-dev/skills/tree/main/skills/remotion and see if you can help me build a video using these best practices"
```

Other agents that support web fetching can be pointed to the same URL.

## Pros

- Zero skill installation — nothing written to disk beyond what Step 1 already creates
- No changes to files outside your project folder — no agent configuration, no dotfiles, no home directory modifications
- Always reads the latest version
- No cleanup needed
- One command, no configuration

## Cons

- Burns context window tokens every session
- Requires the agent to fetch and process web content each time
- May not load all 37 rule files unless specifically asked — the SKILL.md references them with relative links that the agent would need to follow individually
- Not persistent — you have to do this every session

## Risks

- None to your filesystem. The only cost is context window usage and the possibility the agent doesn't fully absorb all rules from a single prompt.
