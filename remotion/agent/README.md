# Agent Skill Setup for Remotion

Remotion provides an agent skill (`remotion-best-practices`) that gives AI coding agents domain knowledge about Remotion APIs — text animations, timing, compositions, audio, etc. This is valuable for getting quality output from agents like Claude Code, Cursor, Gemini CLI, and others.

The skill content is agent-agnostic — verified: zero references to Claude, Cursor, Gemini, or any specific agent in the SKILL.md or any of the 37 rule files. It's pure Remotion domain knowledge. The guides below use Claude Code examples but the skill works with any agent that reads SKILL.md files.

> **Version reference:** This guide was written against `create-video@4.0.443` and the skills repo at commit [`d5d3955`](https://github.com/remotion-dev/skills/commit/d5d395582c6227249cec74f53ab79aca77a4ff16) (2026-03-19), package version `4.0.437`. The skill at that version contains 1 SKILL.md, 37 rule files, and 3 example .tsx assets. If Remotion changes the skill structure, steps below may need updating.

## Options

**Options B, C, and D make no changes to files outside your chosen project folder** — no agent configuration, no dotfiles, no home directory modifications of any kind. Option A is the only approach that risks writing outside the project (if the find-skills follow-up prompt is accepted).

| | Subject | Summary |
|---|---------|---------|
| **A** | [Official](A-official.md) | Remotion's documented `npx skills add` method. Automatic, but invokes a third-party CLI that may modify your home directory if you accept the find-skills follow-up prompt. |
| **B** | [Point agent at skill files](B-point-claude-at-skill-files.md) | Launch your agent with a prompt to read the skill from GitHub. Zero install, but burns tokens and isn't persistent. No changes outside your project folder. |
| **C** | [Manual clone and copy](C-manual-clone-and-copy.md) | Clone the skill repo, copy files into your project. Full skill, project-scoped, no third-party CLI. Not officially documented. No changes outside your project folder. |
| **D** | [Skip skill](D-skip-skills.md) | Don't install the skill at all. Remotion works fine — agents can still help from general training knowledge, just without curated Remotion-specific rules. No changes outside your project folder. |

Each option has detailed pros, cons, and risks in its linked file.
