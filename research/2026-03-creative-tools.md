# AI Creative Tools for Product Demos (March 2026)

**Source:** [A Markdown File Just Replaced Your Most Expensive Design Meeting (Google Stitch)](https://www.youtube.com/watch?v=CDClFY-R0dI)

> **Note:** Reviewed against video transcript for factual accuracy. Includes editorial commentary on how these tools connect to agent-driven development workflows.

---

## Google Stitch (UI/UX)

- **Text-to-UI generator** from Google (updated March 2026). Reduces reliance on traditional design-to-dev handoff by generating production-ready assets directly.
- **Vibe Design:** Describe business objectives in natural language to generate **high-fidelity UI** (not wireframes).
- **Infinite Canvas:** Generates up to **5 screens at once**; allows dropping in screenshots or code snippets for context.
- **Project Context:** The agent reasons across all screens for holistic edits (e.g., "apply a consistent dark theme").
- **Pricing:** Free tier includes **350 generations per month**.
- **Design Markdown (.design.md):** A machine-readable file capturing the design system (colors, typography, spacing) for coding agents.
- **Importing:** Can point to a URL to extract and "markdown-ify" a site's design perspective.

**Agent integration:**
- `.design.md` files work well with context caching — storing a project's design system in a cache lets coding agents maintain consistent UI rules without re-reading the spec every turn.
- Works via **MCP** with **Claude Code** and **Project IDX**.
- The "Playbooks" pattern provides a standard for structuring system instructions that bridge UI design and automated code generation.

## Remotion (Video Framework)

- **Video-as-Code:** A React framework that treats video as code rather than generative pixels. Fully version-controlled and deterministic.
- **Claude Code Skill:** High adoption (150k+ installs) via **skills.sh**.
- **Workflow:** The AI agent writes React components which Remotion renders into an **MP4** locally or via CI/CD.
- **Capabilities:** Handles text animations, motion graphics, and data visualizations.
- **Cost:** Free to render (uses your own compute).

**Agent integration:**
- Programmatic rendering can be integrated into automated pipelines — triggered by events, data updates, or CI/CD steps.
- Well-suited for generating demo videos of agent-driven products where the demo content itself is data-driven.

**See also:** [remotion/](../remotion/) for install guides, caveats, and rollback tooling.

## Blender MCP (3D Space)

- **Natural Language 3D:** Uses an **MCP server** to allow LLMs to control Blender via a chat window.
- **Python API Bridge:** Agents manipulate Blender's operators via Python scripts to build 3D scenes in real-time.
- **Real Assets:** Integrates with **Polyhaven**, **SketchFab**, and **Hyper 3D** for automated asset fetching.
- **Popularity:** Over **17k stars** on GitHub.
- **Impact:** Speeds up architectural walkthroughs, product mockups, and game prototyping.

**Agent integration:**
- A strong example of "agentizing" complex software — a robust Python API turns a high-learning-curve tool into a natural language utility.
- Could be connected to data pipelines to automate generation of 3D visualizations from structured data.

## Key Takeaways

1. **Markdown as interface** — `.design.md` (Stitch), `SKILL.md` (Remotion skills), and MCP tool schemas all use text-based specs as the bridge between humans and agents. This pattern is everywhere now.
2. **MCP is the integration layer** — Stitch, Remotion, and Blender all have MCP server integrations. The pattern: wrap a complex tool's API in an MCP server, and any agent can drive it.
3. **Video-as-code is production-ready** — Remotion at 150k+ skill installs suggests this isn't experimental anymore. The React ecosystem makes it accessible to anyone who can write components.
4. **Free tiers are generous** — Stitch (350 gen/mo), Remotion (free rendering), Blender (open source). The barrier to entry is knowledge, not cost.
