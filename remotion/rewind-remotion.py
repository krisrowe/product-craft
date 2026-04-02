#!/usr/bin/env python3
"""Rewind (rollback) a Remotion + vercel-labs/skills installation.

Removes:
  1. find-skills symlinks from all agent config directories
  2. Empty directories created solely for those symlinks
  3. The ~/.agents skill source and lock file
  4. Project-scope skills and .agents directory
  5. Optionally the entire project directory
  6. Optionally the npx cache entries

Usage:
  python3 rewind-remotion.py --home ~/.agents --project ~/ws/demos
  python3 rewind-remotion.py --home ~/.agents --project ~/ws/demos --remove-project
  python3 rewind-remotion.py --home ~/.agents  # skip project cleanup
  python3 rewind-remotion.py --dry-run --home ~/.agents --project ~/ws/demos

All paths are provided as arguments — nothing is hardcoded to a specific
user or machine layout.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path


def log(msg: str, dry: bool = False) -> None:
    prefix = "[DRY RUN] " if dry else ""
    print(f"  {prefix}{msg}")


def remove_file(path: Path, dry: bool) -> bool:
    if path.is_symlink() or path.exists():
        log(f"rm {path}", dry)
        if not dry:
            path.unlink()
        return True
    return False


def remove_tree(path: Path, dry: bool) -> bool:
    if path.exists():
        log(f"rm -rf {path}", dry)
        if not dry:
            shutil.rmtree(path)
        return True
    return False


def rmdir_if_empty(path: Path, dry: bool) -> bool:
    """Remove directory only if it is empty. Returns True if removed."""
    if not path.is_dir():
        return False
    try:
        if not any(path.iterdir()):
            log(f"rmdir {path}", dry)
            if not dry:
                path.rmdir()
            return True
    except PermissionError:
        pass
    return False


def find_symlinks(home: Path, name: str = "find-skills") -> list[Path]:
    """Find all symlinks named `name` under home, up to depth 6."""
    results = []
    for root, dirs, files in os.walk(home):
        depth = str(root).count(os.sep) - str(home).count(os.sep)
        if depth >= 6:
            dirs.clear()
            continue
        for entry in dirs + files:
            full = Path(root) / entry
            if full.is_symlink() and full.name == name:
                results.append(full)
    return sorted(results)


def cleanup_find_skills(home: Path, dry: bool) -> int:
    """Remove all find-skills symlinks and their empty parent directories."""
    symlinks = find_symlinks(home)
    if not symlinks:
        print("  No find-skills symlinks found.")
        return 0

    count = 0
    for sl in symlinks:
        if remove_file(sl, dry):
            count += 1
        # Try to clean up: skills/ dir, then parent, then grandparent
        # But only if they're empty after removal
        skills_dir = sl.parent  # e.g., ~/.cline/skills/
        parent = skills_dir.parent  # e.g., ~/.cline/
        grandparent = parent.parent  # e.g., ~/

        rmdir_if_empty(skills_dir, dry)
        # Only remove parent if it was created solely for skills
        # (i.e., now empty). Never remove well-known dirs like ~/.claude
        rmdir_if_empty(parent, dry)
        # Handle nested cases like ~/.codeium/windsurf/ or ~/.pi/agent/
        if parent.name in ("windsurf", "agent", "antigravity"):
            rmdir_if_empty(grandparent, dry)

    return count


def cleanup_agents_dir(agents_dir: Path, dry: bool) -> None:
    """Remove ~/.agents skill source and lock file."""
    skill_dir = agents_dir / "skills" / "find-skills"
    lock_file = agents_dir / ".skill-lock.json"

    remove_tree(skill_dir, dry)
    remove_file(lock_file, dry)
    rmdir_if_empty(agents_dir / "skills", dry)
    rmdir_if_empty(agents_dir, dry)


def cleanup_project_skills(project: Path, dry: bool) -> None:
    """Remove project-scope .agents/ and .claude/skills/ symlinks."""
    agents = project / ".agents"
    claude_skills = project / ".claude" / "skills"

    if claude_skills.is_dir():
        for entry in claude_skills.iterdir():
            if entry.is_symlink():
                remove_file(entry, dry)
        rmdir_if_empty(claude_skills, dry)
        rmdir_if_empty(project / ".claude", dry)

    remove_tree(agents, dry)


def cleanup_npx_cache(dry: bool) -> int:
    """Remove npx cache entries for create-video and skills."""
    npm_npx = Path.home() / ".npm" / "_npx"
    if not npm_npx.is_dir():
        return 0

    removed = 0
    for entry in npm_npx.iterdir():
        if not entry.is_dir():
            continue
        pkg_lock = entry / "node_modules" / ".package-lock.json"
        if not pkg_lock.exists():
            continue
        content = pkg_lock.read_text()
        if "create-video" in content or '"skills"' in content:
            remove_tree(entry, dry)
            removed += 1
    return removed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rollback a Remotion + vercel-labs/skills installation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--home",
        type=Path,
        required=True,
        help="Path to the .agents directory (e.g., ~/.agents)",
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=None,
        help="Path to the Remotion project directory (e.g., ~/ws/demos)",
    )
    parser.add_argument(
        "--remove-project",
        action="store_true",
        help="Remove the entire project directory (not just skills)",
    )
    parser.add_argument(
        "--clean-npx-cache",
        action="store_true",
        help="Remove npx cache entries for create-video and skills",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    args = parser.parse_args()
    dry = args.dry_run
    user_home = args.home.parent  # ~/.agents -> ~

    if dry:
        print("DRY RUN — no changes will be made.\n")

    # Step 1: Remove all find-skills symlinks from agent directories
    print("Step 1: Remove find-skills symlinks from all agent directories")
    count = cleanup_find_skills(user_home, dry)
    print(f"  → {count} symlinks {'would be ' if dry else ''}removed\n")

    # Step 2: Remove ~/.agents source and lock file
    print("Step 2: Remove .agents skill source and lock file")
    cleanup_agents_dir(args.home, dry)
    print()

    # Step 3: Project-scope cleanup
    if args.project:
        if args.remove_project:
            print(f"Step 3: Remove entire project directory {args.project}")
            remove_tree(args.project, dry)
        else:
            print(f"Step 3: Remove project-scope skills from {args.project}")
            cleanup_project_skills(args.project, dry)
        print()

    # Step 4: npx cache
    if args.clean_npx_cache:
        print("Step 4: Clean npx cache entries")
        removed = cleanup_npx_cache(dry)
        print(f"  → {removed} cache entries {'would be ' if dry else ''}removed\n")

    # Verification
    print("Verification:")
    remaining = find_symlinks(user_home, "find-skills")
    if remaining and not dry:
        print(f"  WARNING: {len(remaining)} find-skills symlinks still exist:")
        for sl in remaining:
            print(f"    {sl}")
    elif not dry:
        print("  ✓ No find-skills symlinks found")
        if not args.home.exists():
            print("  ✓ .agents directory removed")
        else:
            print(f"  ! .agents directory still exists: {args.home}")

    if dry:
        print("  (verification skipped in dry-run mode)")


if __name__ == "__main__":
    main()
