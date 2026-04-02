# Remotion — Provenance and Licensing

## What is Remotion?

Remotion is a React framework for creating videos programmatically. It is developed by **Remotion AG** (formerly Remotion Inc.), a company founded by Jonny Burger.

- **Website:** https://www.remotion.dev
- **GitHub:** https://github.com/remotion-dev/remotion
- **License:** Custom "Remotion License" (source-available, not open source)

## License

Remotion uses a **custom two-tier license**, not a standard open-source license (not MIT, Apache, GPL, etc.).

From the [LICENSE.md](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md):

> "Depending on the type of your legal entity, you are granted permission to use Remotion for your project. Individuals and small companies are allowed to use Remotion to create videos for free (even commercial), while a company license is required for for-profit organizations of a certain size."

### Free tier eligibility

> "You are eligible to use Remotion for free if you are:
> - an individual
> - a for-profit organization with up to 3 employees
> - a non-profit or not-for-profit organization
> - evaluating whether Remotion is a good fit, and are not yet using it in a commercial way"

### Company license required

For-profit organizations with 4+ employees must purchase a license at https://www.remotion.pro/license.

### Key distinction

Remotion is **source-available**, not **open source**. The source code is public on GitHub, but the license restricts commercial use above the free tier threshold. This is different from MIT/Apache/GPL where anyone can use the software for any purpose.

## Agent Skills — the `remotion-best-practices` skill

### What it is

A set of markdown files (SKILL.md + 38 rule files) that provide AI coding agents with domain knowledge about Remotion APIs and best practices. The skill itself is **prompt text, not executable code**.

### Where it lives

- **In the Remotion monorepo:** https://github.com/remotion-dev/remotion/tree/main/packages/skills
- **Standalone repo mirror:** https://github.com/remotion-dev/skills

The standalone repo's README.md says:

> "This is an internal package and has no documentation."

The SKILL.md frontmatter declares:
```yaml
name: remotion-best-practices
description: Best practices for Remotion - Video creation in React
```

The skill directory in the repo is `skills/remotion/` (not `skills/remotion-best-practices/`). The `remotion-best-practices` name comes from the SKILL.md frontmatter `name` field.

### Skill license

The standalone skills repo (`remotion-dev/skills`) contains **no LICENSE file**. The main Remotion repo's license presumably applies, but this is not explicitly stated. The skill files are markdown (agent instructions) and TypeScript examples, not Remotion library code — whether the Remotion License applies to prompt text is unclear.

### Official install methods

From https://www.remotion.dev/docs/ai/skills (verified via curl, 2026-04-02):

> "Remotion maintains a list of Agent Skills that define best practices for working in Remotion projects."
>
> "You can install them by running:"
> ```
> npx skills add remotion-dev/skills
> ```
>
> "You are also offered the option to add skills when you create a new Remotion project:"
> ```
> bun create video
> ```
>
> "The skills are also available on GitHub here."

Two official methods: `npx skills add` and during project creation (`bun create video` or `npx create-video`).

**No manual install method is documented.** However, the statement "also available on GitHub" with a direct link to the source files implies the files are intended to be accessible for direct use.

### What `npx skills add` actually does

`npx skills add remotion-dev/skills` invokes the [vercel-labs/skills](https://github.com/vercel-labs/skills) CLI (v1.2.0 as of 2026-04-02). This is a **separate tool from Remotion** — it's Vercel's "open agent skills ecosystem" installer.

When run during `npx create-video` project creation and the user accepts all prompts, the skills CLI:

1. Installs the `remotion-best-practices` skill to the project directory (project-scoped, harmless)
2. Offers a follow-up prompt: "Install the find-skills skill?"
3. If accepted, installs a `find-skills` skill to **33 agent config directories** across the home directory, creating ~30 new hidden directories for agents that are not installed

The second step is the aggressive behavior documented in [README.md](README.md) under Caveats. The first step (remotion-best-practices only) is safe and project-scoped.

### Our manual install approach

We use a clone-and-copy method instead of `npx skills add` to avoid the vercel-labs/skills CLI entirely:

```bash
git clone --depth=1 https://github.com/remotion-dev/skills.git /tmp/remotion-skills
mkdir -p .agents/skills/remotion-best-practices
cp -r /tmp/remotion-skills/skills/remotion/* .agents/skills/remotion-best-practices/
mkdir -p .claude/skills
ln -s ../../.agents/skills/remotion-best-practices .claude/skills/remotion-best-practices
rm -rf /tmp/remotion-skills
```

**This is not an officially documented method.** It works because the skill is just files — SKILL.md and markdown rules. There's nothing to "install" beyond placing the files where the agent can read them and creating a symlink for discovery.

**Trade-off:** We don't get automatic updates via `npx skills`. If Remotion updates the skill content, we'd need to re-clone and copy manually. This is acceptable given the alternative is running a CLI that modifies 33 agent config directories.

## The `create-video` scaffolder

### What it is

`npx create-video` is Remotion's project scaffolder. It creates a new Remotion project from a template.

- **npm:** `create-video` (v4.0.443 as of 2026-04-02)
- **Source:** Part of the Remotion monorepo at `packages/create-video/`

### What it installs

When run with "No" to agent skills:
- Project template files in the current directory
- `node_modules/` via `npm install` (312 packages, all project-local)
- npx cache entry at `~/.npm/_npx/` (inert)

Nothing outside the project directory is modified.

### npm audit findings

`npm audit` reports 7 vulnerabilities (2 low, 4 high, 1 critical) in the project dependencies as of 2026-04-02. These are in build-time dev dependencies within `node_modules/` and do not affect the host system. They are eliminated by removing the project directory.
