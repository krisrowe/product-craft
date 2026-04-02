# Product Craft

Tools, automation, and guides for the craft of making software products visible, demonstrable, and polished — demos, UX, visuals, and the processes that tie them together.

`product-pipeline` · `product-automation` · `ux-automation` · `demo-automation` · `video-as-code` · `design-as-code`

## What this repo is

A versioned, scripted, agent-friendly toolkit covering the presentational side of software products:

- **Demos** — programmatic video, animated terminals, live walkthroughs
- **Design/UX** — UI generation, design systems, prototyping tools
- **3D/Visuals** — product mockups, architectural visualization, motion graphics
- **Research** — evaluations and notes on emerging creative tools

The goal is to make each of these **automatable and repeatable** — not a one-off manual effort but a scripted process an agent or CI pipeline can reproduce.

## Contents

### [remotion/](remotion/)

[Remotion](https://www.remotion.dev/) — a React framework for creating programmatic videos. Video-as-code: fully version-controlled, deterministic, rendered locally. Used for animated terminal demos, product walkthroughs, and data visualizations.

### [research/](research/)

Notes, summaries, and findings from evaluating demo and creative tools — video frameworks, UI generators, 3D tooling, and where AI agents fit into each.

## Philosophy

Product craft should be **scripted, versioned, agent-friendly, and reversible**.

### Principles

1. **Automated** — if a human has to do it manually every time, it's not done. Demos, renders, and design artifacts should be producible by running a script or triggering an agent.
2. **Repeatable** — every setup is scripted and versioned. No ad-hoc installs, no "I think I ran this command." A new machine or a fresh start follows the same documented steps and gets the same result.
3. **Versioned** — demo assets are code, not binary blobs. Video-as-code (Remotion), design-as-markdown (Stitch), scene-as-script (Blender MCP). Everything lives in git.
4. **Agent-friendly** — tools and workflows should be operable by AI agents (Claude Code, Gemini CLI) without manual intervention. MCP integration where available.
5. **Provenance** — where each tool comes from, who maintains it, how mature it is, whether it's open source.
6. **Scope of impact** — exactly what each tool installs, where, and at what scope (project-local vs. user vs. system).
7. **Reversible** — uninstall is scripted, not manual. Every tool includes rollback with verification steps.
8. **Caveats documented** — known gotchas, aggressive installer behaviors, trust concerns. No surprises.

If you can't confidently uninstall something, you shouldn't install it.
