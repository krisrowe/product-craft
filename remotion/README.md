# Remotion — Demo Video Creation

We use [Remotion](https://www.remotion.dev/) (React-based video framework) to create animated demo videos for our tools (echomodel, echofit, etc.). Videos are authored as React/TypeScript components with frame-based animation, previewed in a local studio, and rendered to MP4 or GIF.

## Why Remotion

- Programmatic: videos are code, diffable, version-controlled
- React ecosystem: Tailwind, components, TypeScript
- Local preview: `npm run dev` at localhost:3000
- Renders to MP4/GIF/WebM without external services

**See also:** [FAQ](FAQ.md) · [Provenance & Licensing](PROVENANCE.md)

## Project repo

Remotion projects live in their own repos, separate from this documentation.

## Setup

### Principles

Remotion is a Node.js project that lives entirely in its own directory. It uses the system Node.js (installed via Homebrew) and installs all dependencies locally in `node_modules/`. No global packages, no system-level changes, no pipx — just a standard npm project.

To keep it consistent with a workspace convention (`~/src/<purpose-specific-repo>`):

1. **Dedicated repo** — one Remotion project per repo, named for its purpose (e.g., `echo-demos`, `product-videos`)
2. **GitHub remote** — create the repo on GitHub first so it's backed up and cloneable
3. **Pin the version** — use `@4.0.443` (or whatever version you tested) rather than `@latest`

### Step 1: Scaffold the project

```bash
# Create the GitHub repo first
gh repo create <repo-name> --private --clone
cd <repo-name>

# Scaffold Remotion into the repo
npx create-video@4.0.443
```

**Wizard choices:**
- Template: **Blank**
- TailwindCSS: **Yes**
- **Add agent skills:** see Step 2 below for options

```bash
# Install dependencies (project-local only)
npm install

# Verify it works
npm run dev     # Preview at http://localhost:3000

# Commit and push
git add -A
git commit -m "Scaffold Remotion project"
git push -u origin main
```

### Step 2: Agent skill (optional but recommended)

Remotion provides an agent skill that gives AI coding agents (Claude Code, Cursor, Gemini CLI, etc.) domain knowledge about Remotion APIs. This improves the quality of agent-generated video code.

**See [agent/](agent/) for setup options** — from the official installer to zero-install approaches, with pros, cons, and risks for each.

---

### What the scaffolder installs (without skills)

| What | Where | Scope |
|------|-------|-------|
| Remotion + React + Tailwind | `<repo>/node_modules/` (312 packages) | Project-local |
| npx cache: create-video | `~/.npm/_npx/` | User-level cache (inert, cleanable) |
| npm cache | `~/.npm/_cacache/` | Shared npm infra |

No global packages. No home directory modifications. No skills. No symlinks. Fully contained in the repo directory plus standard npm cache.

## Usage

```bash
cd <project-dir>

# Preview in browser
npm run dev

# Render a specific composition to MP4
npx remotion render SkillInstallDemo out/skill-install.mp4

# Render to GIF
npx remotion render SkillInstallDemo out/skill-install.gif --image-format png
```

Compositions are registered in `src/Root.tsx`. Each composition is an independent video with its own duration, resolution, and fps.

## Install log

When installing Remotion, document the results in a dated install log (e.g., `2026-04-02_INSTALL.md`) covering what was created, what was modified, and what the rollback plan is. Keep machine-specific install logs separate from this reusable documentation.

## Uninstall / Rewind

Use [rewind-remotion.py](rewind-remotion.py) to roll back the installation. The script is reusable and accepts arguments — nothing is hardcoded to a specific user or machine layout.

### Preview (dry run)

```bash
python3 rewind-remotion.py --dry-run --home ~/.agents --project <project-dir> --clean-npx-cache
```

### Remove user-scope skills only (keep the project)

```bash
python3 rewind-remotion.py --home ~/.agents
```

This removes:
- All `find-skills` symlinks from every agent config directory (`~/.claude/skills/`, `~/.gemini/skills/`, `~/.cursor/skills/`, etc.)
- Empty directories created solely for those symlinks
- `~/.agents/skills/find-skills/` (the source SKILL.md)
- `~/.agents/.skill-lock.json` (the lock file)

### Remove everything (user-scope + project + npx cache)

```bash
python3 rewind-remotion.py --home ~/.agents --project <project-dir> --remove-project --clean-npx-cache
```

### What the script does

1. Finds all symlinks named `find-skills` under `$HOME` (up to depth 6)
2. Removes each symlink
3. Removes now-empty parent directories (only if empty — won't touch `~/.claude`, `~/.gemini`, etc. which have other contents)
4. Removes the `~/.agents` source directory and lock file
5. Optionally removes project-scope skills from the project dir
6. Optionally removes the entire project directory
7. Optionally removes npx cache entries for `create-video` and `skills`
8. Runs verification to confirm no symlinks remain

### Why we trust this script

The script's completeness was verified through source-code analysis and filesystem scanning:

1. **Source-code audit of `skills` v1.2.0** (3,665 lines compiled JS) confirmed:
   - All install paths derive from Node's `os.homedir()` — nothing is written outside `$HOME`
   - Two env vars (`CODEX_HOME`, `CLAUDE_CONFIG_DIR`) can override specific agent paths, but only for those agents. No other override mechanism exists.
   - The CLI has exactly 31 hardcoded `skillsDir` patterns plus a few `globalSkillsDir` overrides — all under `$HOME`
   - Filesystem writes are limited to `mkdirSync`, `symlinkSync`, and 6 `writeFile` calls (all writing SKILL.md content or the lock file)

2. **Dynamic discovery vs. hardcoded lists** — the script uses `find` to locate symlinks, not a hardcoded directory list. This means it will find and remove symlinks even if a future version of the `skills` CLI adds new agent directories. The only assumption is that symlinks are named `find-skills` and live under `$HOME`.

3. **Full filesystem scan confirmed no writes outside `$HOME`** — scanning `/opt`, `/usr/local`, `/Library`, `/Applications`, `/var`, `/etc`, and `/private/tmp` found zero `find-skills` symlinks or `.skill-lock.json` files.

4. **Safe deletion** — the script uses `rmdir` (not `rm -rf`) for parent directories, so it will never delete a directory that has acquired other contents since the install. Worst case: the symlink is removed but a now-empty directory stays behind.

### Manual verification after rollback

```bash
# Should return nothing:
find ~ -maxdepth 6 -type l -name "find-skills" 2>/dev/null

# Should not exist:
ls ~/.agents 2>/dev/null

# Should not contain find-skills:
ls ~/.claude/skills/ | grep find-skills
```

## Caveats — vercel-labs/skills installer

The Remotion scaffolder (`npx create-video`) bundles the [vercel-labs/skills](https://github.com/vercel-labs/skills) ecosystem installer. When you say "Yes" to "Add agent skills?" and then "Yes" to the follow-up "Install the find-skills skill?", it:

1. Installs a `find-skills` SKILL.md to `~/.agents/skills/find-skills/`
2. Creates symlinks into **every known AI agent's config directory** — including agents you don't have installed (Cursor, Cline, Copilot, Windsurf, Kiro, etc.)
3. This means it creates **~30 new hidden directories** in your home directory
4. The SKILL.md modifies agent behavior by injecting a system prompt that directs skill discovery toward the vercel-labs marketplace

This is aggressive for a one-time prompt during a video scaffolder. The directories are harmless (empty except for a symlink) but add clutter and could confuse config for agents you install later.

**Recommendation:** Say **No** to "Add agent skills?" during setup, or at minimum say **No** to the "Install find-skills?" follow-up prompt.

## Caveats — rollback scope

As tested with `create-video@4.0.443`, `skills` v1.2.0, and the skills repo at commit [`d5d3955`](https://github.com/remotion-dev/skills/commit/d5d395582c6227249cec74f53ab79aca77a4ff16) (2026-03-19):

The rollback script and install documentation cover all **known** filesystem changes. The following were verified from source code and filesystem inspection:

| Unknown | Risk | Specific paths | Verified | Mitigation |
|---------|------|----------------|----------|------------|
| npm cache writes | Negligible | `~/.npm/_logs/`, `~/.npm/_cacache/` | Standard npm infra, not Remotion-specific | `npm cache clean --force` |
| Node V8 compile cache | None observed | `~/Library/Caches/node/`, `/tmp/node-compile-cache*` | Checked — no files found. `NODE_COMPILE_CACHE` env var unset. | `ls ~/Library/Caches/node/` to verify |
| npm telemetry | Privacy only | No local artifacts | Outbound-only network activity | `npm config set metrics-registry ""` |
| esbuild postinstall | Confirmed project-local | `node_modules/@esbuild/darwin-arm64/` | Source-verified: only postinstall in 312 deps, writes binary inside node_modules only | `rm -rf <project-dir>` removes it |
| skills CLI writes | Source-verified: only SKILL.md + lock file | See install log | Audited all 6 `writeFile` calls in compiled source (3665 lines) | Covered by `rewind-remotion.py` |
| Global package corruption | **None** | Checked `/opt/homebrew/lib/node_modules`, `pip3 list` | No global npm/Python packages modified. Node v25.8.1, npm 11.11.0 unchanged. | N/A — no action needed |

None of these uncertainties represent a meaningful integrity risk. The script's `--remove-project` flag removes all project-local artifacts, and the symlink cleanup is exhaustive by design (uses `find`, not a hardcoded list). These findings were verified through source-code audit of the `skills` CLI and full filesystem scanning on a fairly new macOS machine.

## macOS time travel (if rollback isn't enough)

If you need to revert the machine to an exact prior state:

- **Time Machine:** Only works if it was already configured. Check: `tmutil listlocalsnapshots /`
- **APFS local snapshots:** macOS creates these automatically. A snapshot from before the install (e.g., before 08:30 on the install date) could be restored, but this is a heavy-handed approach for what amounts to symlinks and empty directories.
- **Full reset:** System Settings → General → Transfer or Reset → Erase All Content and Settings. Nuclear option, documented in `~/INSTALLED.md`.

For this particular installation, the script-based rollback is sufficient — every change is a file/symlink/directory, fully enumerable and removable.
