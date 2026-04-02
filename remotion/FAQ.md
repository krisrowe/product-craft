# Remotion — Frequently Asked Questions

## Does Remotion work without the agent skill?

Yes. Remotion is a standalone video framework. The agent skill (`remotion-best-practices`) gives Claude Code better knowledge of Remotion-specific APIs, but Remotion renders video with or without it. The skill is a reference for the agent, not a runtime dependency.

## How does Claude Code help with Remotion if I don't install the skill?

Claude Code has Remotion knowledge from its training data — it's seen Remotion code in public repos. Without the skill it can still write Remotion components and help with video composition, but it won't have the curated, up-to-date rules for specific topics (captions, transitions, timing curves, audio visualization, etc.). It's the difference between "knows React generally and has seen some Remotion code" vs. "has a reference manual open."

## I thought a skill was just one SKILL.md file. Why does this one have 37 extra files?

SKILL.md is the required entry point — the file the agent loads first. But a skill directory can contain supporting files: additional docs, code examples, templates. The `remotion-best-practices` skill uses a `rules/` subfolder with 37 topic-specific .md files and 3 example .tsx assets.

The SKILL.md acts as a router: "for captions, read `rules/subtitles.md`; for audio, read `rules/audio.md`." Claude loads the specific rule file on demand when the topic comes up — it doesn't load all 37 at once. This is a well-designed pattern that avoids wasting context window tokens.

## What's actually in those rule files?

Each covers a specific Remotion topic with API details, code examples, and best practices. Topics include: 3D, animations, assets, audio, audio visualization, calculate-metadata, charts, compositions, captions, extract-frames, FFmpeg, fonts, GIFs, images, light leaks, Lottie, maps, measuring DOM nodes, measuring text, parameters, sequencing, sound effects, subtitles, Tailwind, text animations, timing, transitions, transparent video, trimming, video embedding, voiceover, and more.

The full list is in the [SKILL.md on GitHub](https://github.com/remotion-dev/skills/blob/main/skills/remotion/SKILL.md).

## Why do Options A and D create a symlink? Do I need one?

All options that install the skill locally (A and D) create a symlink because Claude Code discovers skills by scanning `<project>/.claude/skills/*/SKILL.md`. The actual skill files live in `.agents/skills/` — a platform-neutral directory that isn't specific to Claude Code. The symlink in `.claude/skills/` is how Claude Code finds the skill. Without it, Claude doesn't know the files exist.

This is the same structure that the official `npx skills add` installer creates. The `.agents/` directory is the canonical location; each agent gets a symlink from its own skills directory pointing there.

**Alternative: skip the symlink entirely.** If you only use Claude Code, you can put the files directly in `.claude/skills/remotion-best-practices/` — no `.agents/` directory, no symlink. That works fine. The `.agents/` + symlink pattern only matters if you also want Gemini CLI or other agents to find the same skill from a shared location.

## Why is the symlink a relative path instead of an absolute path?

The symlink uses `../../.agents/skills/remotion-best-practices` (relative) rather than an absolute path like `~/.agents/...` because it's inside a git repo. A relative path:

- Stays inside the project directory — no reference to the home dir
- Works on any machine regardless of username or home path
- Travels with the repo when cloned

An absolute path would point outside the project and break on anyone else's machine. The relative path works because `.claude/skills/` and `.agents/skills/` have a fixed relationship within the project root.

## Is this open source?

No. Remotion uses a custom "Remotion License" that is **source-available** but not open source:

- **Free** for individuals, teams of 3 or fewer, and nonprofits
- **Paid license required** for for-profit organizations with 4+ employees

The skills repo (`remotion-dev/skills`) has no LICENSE file of its own. See [PROVENANCE.md](PROVENANCE.md) for full details and quotes from the license.

## What does `npm run dev` do? Is it the only way to see the work?

It launches Remotion Studio — a local web server at http://localhost:3000 that lets you preview your video compositions in the browser. It's a development tool for live preview during development — you see changes instantly as you edit code. It runs only while you're working and stops when you `Ctrl+C`. No persistent service, no background daemon, nothing listening after you stop it.

There are three ways to see your work:

1. **`npm run dev`** — live preview in browser. Fastest feedback loop — changes appear as you save files. Best for iterating on compositions.
2. **`npx remotion still <CompositionId> out.png`** — render a single frame to an image. Quick spot-check without launching the studio.
3. **`npx remotion render <CompositionId> out.mp4`** — render the full video to MP4/GIF. This is the final output step and takes longer (renders every frame). You wouldn't do this every time you tweak a component.

The studio (`npm run dev`) is more efficient than rendering a full video each time because it only renders the frame you're looking at, in real time.

## Does the scaffolder support non-interactive (headless) installation?

The `npx create-video` scaffolder is interactive — it prompts for template choice, TailwindCSS, and skills. As of v4.0.443, there is no documented set of CLI flags to skip the interactive prompts. This means automated/CI setup would need to either use `expect`-style scripting or set up the project files manually.

## What exactly does `npx create-video` write to my system?

With "No" to agent skills:

| What | Where | Scope |
|------|-------|-------|
| Project template files | Current directory | Project-local |
| `node_modules/` (312 packages) | Current directory (after `npm install`) | Project-local |
| npx cache entry | `~/.npm/_npx/` | Shared npm cache (inert) |
| npm download cache | `~/.npm/_cacache/` | Shared npm cache |

Nothing else. No global packages, no home directory modifications, no services, no daemons.

## Can I uninstall Remotion completely?

Yes. Delete the project directory — that removes everything project-local. To also clean the npm caches:

```bash
rm -rf <project-dir>
# Optional: clean npx cache for the scaffolder
rm -rf ~/.npm/_npx/  # removes ALL npx cached packages, not just create-video
```

If you installed the skill via Option A and accepted the find-skills prompt, also run [rewind-remotion.py](rewind-remotion.py) to clean up the home directory artifacts.
