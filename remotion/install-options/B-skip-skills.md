# Option B: Skip skill installation entirely

Say **No** to "Add agent skills?" during the scaffolder wizard.

## Pros

- Zero risk — nothing installed beyond the Remotion project itself
- No third-party CLI invoked
- No changes to files outside your project folder — no agent configuration, no dotfiles, no home directory modifications
- Remotion is fully functional without the skill

## Cons

- Claude Code won't have the curated rules for specific Remotion topics (captions, transitions, audio visualization, timing, 3D, charts, fonts, etc.)
- Agent relies on general training knowledge, which may be less precise or current than the 37 rule files

## Risks

- None. You can always add the skill later via any of the other options.
