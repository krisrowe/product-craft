# The vercel-labs/skills Ecosystem

## What it is

`skills` on npm is a CLI package manager for AI agent skills, owned and maintained by Vercel (the company behind Next.js, Vercel hosting, and v0). It's the delivery mechanism for the [Agent Skills](https://agentskills.io) open standard — a format for packaging domain knowledge that AI coding agents can consume.

- **npm package:** [`skills`](https://www.npmjs.com/package/skills) (owns the bare name)
- **GitHub:** [vercel-labs/skills](https://github.com/vercel-labs/skills) — the CLI
- **GitHub:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — Vercel's first-party skill collection
- **Marketplace website:** [skills.sh](https://skills.sh)
- **Open standard:** [agentskills.io](https://agentskills.io)
- **Maintainers:** `rauchg` (Guillermo Rauch, Vercel CEO), `quuu`

## Scale (as of 2026-04-02)

| Metric | Value |
|--------|-------|
| npm downloads (last 30 days) | **2.67 million** |
| npm downloads (Jan–Mar 2026) | **3.99 million** |
| vercel-labs/skills GitHub stars | 12,781 |
| vercel-labs/agent-skills GitHub stars | 24,312 |
| vercel-labs/agent-skills forks | 2,212 |
| Repo created | 2025-12-08 (skills CLI), 2026-01-14 (agent-skills) |
| Supported agents | 44+ (Claude Code, Codex, Cursor, Gemini CLI, Copilot, Cline, Windsurf, etc.) |

This is not a niche project. Nearly 4 million downloads in 3 months, 24k+ stars on the skills collection, maintained by the Vercel CEO personally.

## What it does

The `npx skills` CLI:

- **Installs** agent skills from GitHub repos into project or user-level directories
- **Removes** installed skills (`npx skills remove`)
- **Lists** installed skills (`npx skills list`)
- **Searches** for skills (`npx skills find`)
- **Updates** skills to latest versions (`npx skills check`, `npx skills update`)
- **Scaffolds** new skills (`npx skills init`)

### Key flags

| Flag | What it does |
|------|--------------|
| `-y` / `--yes` | Skip all confirmation prompts (non-interactive) |
| `-a <agent>` / `--agent` | Target specific agents (e.g., `claude-code`, `gemini-cli`) |
| `-g` / `--global` | Install to user-level instead of project-level |
| `-s <name>` / `--skill` | Install specific skills by name |
| `--copy` | Copy files instead of symlinking |
| `--all` | Install all skills to all agents without prompts |
| `-l` / `--list` | List available skills without installing |

### Install scopes

| Scope | Flag | Location | Use case |
|-------|------|----------|----------|
| Project (default) | none | `./<agent>/skills/` | Committed with project |
| Global | `-g` | `~/<agent>/skills/` | Available across all projects |

## How Remotion uses it

Remotion's `npx create-video` scaffolder calls `npx skills add remotion-dev/skills` under the hood when you say Yes to "Add agent skills?" This installs the `remotion-best-practices` skill.

The scaffolder then offers a second prompt: "Install the find-skills skill?" This is separate from Remotion — it's the Vercel skills ecosystem's growth mechanism. The `find-skills` skill instructs agents to search skills.sh for more skills. If accepted, it installs globally to all detected agent directories.

See [A-official.md](agent/A-official.md) for how to use the official installer while avoiding the find-skills side effects.

## Relationship to Claude Code

Claude Code's official documentation says:

> "Claude Code skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools."

Anthropic references the `agentskills.io` open standard but does **not** mention vercel-labs, skills.sh, or `npx skills` anywhere in their documentation. Claude Code has its own native skill system (`.claude/skills/`) that predates and is independent of the Vercel CLI — the two are compatible because they follow the same standard, but Claude Code does not depend on or endorse the Vercel tooling.

The `npx skills` CLI knows where Claude Code stores skills (`.claude/skills/`) and can write to that location. But Claude Code doesn't know or care how the files got there — it just reads `SKILL.md` from its skills directory.

## Relationship to Gemini CLI

Gemini CLI also supports skills natively via `.gemini/skills/`. The `npx skills` CLI can install to this location via `-a gemini-cli`. Like Claude Code, Gemini CLI doesn't reference the Vercel tooling — it just reads SKILL.md files from its skills directory.

## License

The vercel-labs/skills repo (the CLI) returns 404 for `/LICENSE`. No license file found as of 2026-04-02. The vercel-labs/agent-skills repo (the skill collection) would need separate verification.

## Implications for echoskill

This ecosystem is directly relevant to the echoskill project. Vercel has:

- Massive adoption (4M downloads/quarter, 24k stars)
- The bare `skills` name on npm
- A marketplace website (skills.sh)
- CEO-level investment (rauchg is a maintainer)
- Support for 44+ agents
- An open standard (agentskills.io) that Anthropic and Google already reference

This is tracked as a research item in the echoskill repo — see the GitHub issue for competitive analysis and strategic implications.
