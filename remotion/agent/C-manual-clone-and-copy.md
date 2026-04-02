# Option C: Clone and copy manually (not officially documented)

> Versions tested: see [agent/README](README.md#options)

Clone the Remotion skills repo, copy the files into your project, and create the discovery symlink yourself. This replicates what the official installer produces without running the vercel-labs/skills CLI.

## Pros

- Full skill with all 37 rule files, loaded automatically every session
- No changes to files outside your project folder — no agent configuration, no dotfiles, no home directory modifications
- No third-party CLI invoked
- Fully reversible with `rm`

## Cons

- **Not an officially documented install method.** Remotion's docs only describe `npx skills add` and the scaffolder prompt. The docs do say the files are ["also available on GitHub"](https://www.remotion.dev/docs/ai/skills) with a link to the source, but do not provide manual install instructions.
- **No automatic updates.** If Remotion updates the skill, you'd need to re-clone and copy manually.
- **The source path differs from the installed name.** The files live at `skills/remotion/` in the repo but the SKILL.md declares `name: remotion-best-practices`. Our copy step accounts for this.

## Risks

- **The skills repo has no LICENSE file.** The main Remotion repo uses a custom source-available license (see [PROVENANCE.md](../PROVENANCE.md)). Whether that license applies to the skill markdown files is unclear.
- If the skill structure changes in a future Remotion release, the manual copy may not match what the official installer would produce.

## Steps

Run from inside the Remotion project directory:

```bash
# 1. Clone the skills repo to a temp location (nothing written to your project yet)
git clone --depth=1 https://github.com/remotion-dev/skills.git /tmp/remotion-skills

# 2. Create the skill directory inside your project
mkdir -p .agents/skills/remotion-best-practices

# 3. Copy skill files (SKILL.md + rules/) into your project
cp -r /tmp/remotion-skills/skills/remotion/* .agents/skills/remotion-best-practices/

# 4. Create the symlink so Claude Code discovers the skill
mkdir -p .claude/skills
ln -s ../../.agents/skills/remotion-best-practices .claude/skills/remotion-best-practices

# 5. Clean up the temp clone
rm -rf /tmp/remotion-skills

# 6. Commit
git add .agents/ .claude/skills/
git commit -m "Add remotion-best-practices skill (project-scope)"
```

Every write is inside the project directory. Nothing touches `~/`, `~/.claude/`, `~/.agents/`, or any other agent config.

## Uninstall

```bash
rm .claude/skills/remotion-best-practices
rm -rf .agents/
git add -A && git commit -m "Remove remotion-best-practices skill"
```
