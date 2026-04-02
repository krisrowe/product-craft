# Agent Skill Setup for Remotion

Remotion provides an agent skill (`remotion-best-practices`) that gives AI coding agents domain knowledge about Remotion APIs — text animations, timing, compositions, audio, etc. This is valuable for getting quality output from agents like Claude Code, Cursor, Gemini CLI, and others.

The skill content is agent-agnostic — verified: zero references to Claude, Cursor, Gemini, or any specific agent in the SKILL.md or any of the 37 rule files. It's pure Remotion domain knowledge. The guides below use Claude Code examples but the skill works with any agent that reads SKILL.md files.

> **Version reference:** This guide was written against `create-video@4.0.443` and the skills repo at commit [`d5d3955`](https://github.com/remotion-dev/skills/commit/d5d395582c6227249cec74f53ab79aca77a4ff16) (2026-03-19), package version `4.0.437`. The skill at that version contains 1 SKILL.md, 37 rule files, and 3 example .tsx assets. If Remotion changes the skill structure, steps below may need updating.

## Recommended: Option A

**Use the official installer.** Say Yes to the skill prompt, say No to the find-skills follow-up. This is the officially supported method and produces a project-scoped skill with no home directory modifications. See [Option A](A-official.md) for details.

## All options

| | Subject | Summary | Contained to project? |
|---|---------|---------|----------------------|
| **A** | [Official](A-official.md) | **Recommended.** Remotion's documented `npx skills add` method. Say Yes to skill, No to find-skills follow-up. | Yes, if you decline the find-skills follow-up. |
| **B** | [Point agent at skill files](B-point-claude-at-skill-files.md) | Launch your agent with a prompt to read the skill from GitHub. Zero install, but burns tokens and isn't persistent. | Yes |
| **C** | [Manual clone and copy](C-manual-clone-and-copy.md) | Clone the skill repo, copy files into your project. Produces the same result as Option A. Use this if npx is unavailable, restricted, or you need a fully scriptable non-interactive process. | Yes |
| **D** | [Skip skill](D-skip-skills.md) | Don't install the skill at all. Remotion works fine — agents can still help from general training knowledge, just without curated Remotion-specific rules. | Yes |

Each option has detailed pros, cons, and risks in its linked file.
