# Option D: Skip skill installation entirely

Say **No** to "Add agent skills?" during the scaffolder wizard.

The install process is identical to Options B and C — the same scaffolder, the same project. The only difference is that you don't separately show Claude the skill files. Claude can still help with Remotion from its general training knowledge, just without the curated rules. This may be the quickest way to get started if you're having trouble getting Claude visibility to the skill files via the other options.

## Pros

- Zero risk — nothing installed beyond the Remotion project itself
- No third-party CLI invoked
- No changes to files outside your project folder — no agent configuration, no dotfiles, no home directory modifications
- Remotion is fully functional without the skill
- Fastest path to getting started — no extra steps

## Cons

- Claude Code won't have the curated rules for specific Remotion topics (captions, transitions, audio visualization, timing, 3D, charts, fonts, etc.)
- Agent relies on general training knowledge, which may be less precise or current than the 37 rule files

## Risks

- None. You can always add the skill later via any of the other options.
