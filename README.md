# Product Demos

Scripts, tools, documentation, and guides for creating software product demos — especially for AI agents, skills, MCP servers, and developer tools.

## What this repo is

A practical toolkit for making demo videos, screenshots, and presentations of software products. The goal is to make it easy to:

- **Get started** without being overwhelmed by unfamiliar tools or ecosystems
- **Know what you're installing** — where it came from, whether it's mature and safe, what it touches on your system
- **Install and configure** demo tools with proper isolation, following workspace conventions
- **Create demos** efficiently using code-driven approaches (video-as-code, programmatic animation)
- **Uninstall cleanly** when you're done, with confidence nothing was left behind

Each tool has its own folder with install guides, usage docs, caveats, and rollback scripts.

## Contents

### [remotion/](remotion/)

[Remotion](https://www.remotion.dev/) — a React framework for creating programmatic videos. Video-as-code: fully version-controlled, deterministic, rendered locally. Used for animated terminal demos, product walkthroughs, and data visualizations.

### [research/](research/)

Notes, summaries, and findings from evaluating demo tools and creative AI products.

## Philosophy

Demo tooling should be **contained, documented, repeatable, and reversible**.

### Principles

1. **Repeatable** — every setup is scripted and versioned. No ad-hoc installs, no "I think I ran this command." A new machine or a fresh start follows the same documented steps and gets the same result.
2. **Provenance** — where each tool comes from, who maintains it, how mature it is, whether it's open source.
3. **Install guide** — step-by-step with recommended choices, avoiding common pitfalls.
4. **Scope of impact** — exactly what it installs, where, and at what scope (project-local vs. user vs. system).
5. **Uninstall/rollback** — scripted, not manual. How to fully remove it, with verification steps.
6. **Caveats** — known gotchas, aggressive installer behaviors, or trust concerns.

If you can't confidently uninstall something, you shouldn't install it.
