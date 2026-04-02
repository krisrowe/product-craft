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

## Why does Option D need a symlink?

Claude Code discovers skills by scanning `<project>/.claude/skills/*/SKILL.md`. The actual skill files live in `.agents/skills/` — a platform-neutral directory that isn't specific to Claude Code (Gemini CLI, Cursor, and other agents have their own skill directories). The symlink in `.claude/skills/` is how Claude Code finds the skill. Without it, Claude doesn't know the files exist.

This is the same structure that the official `npx skills add` installer creates. The `.agents/` directory is the canonical location; each agent gets a symlink from its own skills directory pointing there.

If you only use Claude Code and don't care about the platform-neutral layout, you could skip the symlink and put the files directly in `.claude/skills/remotion-best-practices/`. But the `.agents/` + symlink pattern is what the official tooling produces and what other agents expect.

## Is this open source?

No. Remotion uses a custom "Remotion License" that is **source-available** but not open source:

- **Free** for individuals, teams of 3 or fewer, and nonprofits
- **Paid license required** for for-profit organizations with 4+ employees

The skills repo (`remotion-dev/skills`) has no LICENSE file of its own. See [PROVENANCE.md](PROVENANCE.md) for full details and quotes from the license.

## What does `npm run dev` do?

It launches Remotion Studio — a local web server at http://localhost:3000 that lets you preview your video compositions in the browser. It's a development tool, not a production service. It runs only while you're working and stops when you `Ctrl+C`. No persistent service, no background daemon, nothing listening after you stop it.

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
