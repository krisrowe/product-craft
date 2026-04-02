# Option A: Use the official `npx skills add` installer

> Versions tested: see [agent/README](README.md#options)

This is Remotion's [documented approach](https://www.remotion.dev/docs/ai/skills):

> "You can install them by running: `npx skills add remotion-dev/skills`"
> "You are also offered the option to add skills when you create a new Remotion project"

Say **Yes** to "Add agent skills?" during the scaffolder wizard, then follow the prompts.

## Pros

- Official, documented method
- Gets all 37 rule files with correct directory structure and symlinks
- Automatic — no manual steps beyond answering prompts

## Cons

- Invokes the [vercel-labs/skills](https://github.com/vercel-labs/skills) CLI, a third-party tool separate from Remotion
- Offers a follow-up "Install the find-skills skill?" prompt that, if accepted, installs a user-scoped skill to ~30 agent config directories across your home directory (see [Caveats](../README.md#caveats---vercel-labsskills-installer))

## Risks

- If you say Yes to the find-skills follow-up: ~30 new hidden directories in your home dir, behavioral injection into every Claude/Gemini session, symlinks for agents you don't have installed
- If you say No to the find-skills follow-up: no risk — the project-scoped remotion skill is safe

## Cleanup if needed

1. Say **Yes** to "Add agent skills?" (installs remotion-best-practices, project-scoped — safe)
2. Say **No** to "Install the find-skills skill?" — this is the follow-up that causes the home directory sprawl
3. If you accidentally said Yes to both, run [rewind-remotion.py](../rewind-remotion.py) to remove the find-skills artifacts while keeping the project-scoped remotion skill intact:
   ```bash
   python3 rewind-remotion.py --dry-run --home ~/.agents
   # Review, then:
   python3 rewind-remotion.py --home ~/.agents
   ```

## What the official install creates in your project

```
<project>/.agents/skills/remotion-best-practices/
├── SKILL.md          (skill instructions)
└── rules/            (37 rule files — audio, video, transitions, etc.)
    └── assets/       (3 example .tsx files)

<project>/.claude/skills/remotion-best-practices -> ../../.agents/skills/remotion-best-practices
```

The `.claude/skills/` symlink is how Claude Code discovers the skill. The `.agents/` directory is a platform-neutral location that could also be symlinked from `.gemini/skills/` if desired.
