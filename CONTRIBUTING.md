# Contributing to Product Craft

## Vision

"Product craft" is a term we're coining here, not an established industry concept. We're using it to mean: applying the same engineering rigor (automation, version control, CI/CD, agent-driven workflows) to the presentational and experiential side of software that we already apply to the software itself. Productization of productization.

The components of product craft:

- **Demos** — showing what a product does. Video, animated terminals, live walkthroughs. These should be code, not screen recordings. Regeneratable, not one-off.
- **Design/UX** — how a product looks and feels. UI generation, design systems, prototyping. Increasingly expressible as markdown and agent-operable.
- **Visuals** — 3D mockups, motion graphics, data visualizations. Scriptable via APIs and MCP servers.
- **Research** — ongoing evaluation of tools, frameworks, and techniques. What's mature, what's emerging, what's safe to adopt.

The unifying principle: every one of these should be **automatable by an AI agent**. If a tool can't be driven programmatically — installed via script, operated via CLI or MCP, uninstalled cleanly — it doesn't belong here. The goal is a toolkit where an engineer who has never done design or video work can follow a guide, run a script, and produce something polished — or hand the whole thing to an agent.

Each tool in this repo is also a product in its own right (Remotion is a company, Google Stitch is a Google product, Blender is open-source software). We document them as a consumer would want to be informed: what it is, who's behind it, what it installs, what it touches, and how to fully remove it.

## Repo structure

```
product-craft/
├── README.md              — what this repo is, contents, principles
├── CONTRIBUTING.md         — this file: architecture, conventions
├── research/              — tool evaluations, video notes, findings
├── remotion/              — video-as-code: guides, scripts, rollback
│   ├── README.md          — install, usage, uninstall, caveats
│   └── rewind-remotion.py — rollback script
├── design/                — (future) UI/UX tools: Google Stitch, etc.
└── 3d/                    — (future) 3D tools: Blender MCP, etc.
```

## Conventions

### One folder per tool

Each tool gets its own folder with at minimum:
- `README.md` — what it is, install guide, usage, uninstall, caveats
- Rollback/uninstall script if the tool modifies anything outside its project directory

### Research notes

Research files live in `research/` and follow the naming pattern `YYYY-MM-topic.md`. Each links to its source (video, article, repo) and includes both factual summary and editorial commentary on agent integration patterns.

### Privacy

This is a public repo. Never include:
- Absolute paths containing usernames
- GitHub usernames or personal identifiers
- References to personal projects or workflows
- Cloud IDs, credentials, or account-specific values

Use generic placeholders: `<project-dir>`, `<repo-name>`, `your-org/repo`.

### Navigation

Every `.md` file should be reachable from `README.md` — either directly or through intermediate READMEs. A reader should never need to browse the file tree to discover content.

## Origin story

This repo was born from a software engineer almost skipping past a YouTube video about creative AI tools — design generators, video frameworks, 3D scene builders — because it felt outside the normal engineering wheelhouse. The video turned out to contain directly applicable tools (Remotion, Google Stitch, Blender MCP) that could be driven programmatically by the same AI agents already in the developer workflow. The realization: product craft isn't a separate discipline from engineering when the tools are code-driven and agent-operable. This repo exists to lower the barrier so that next time, there's no reluctance — just a guide to follow.
