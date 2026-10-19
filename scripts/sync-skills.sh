#!/bin/sh
# Copy canonical skills from .agents/skills into .claude/skills.
# Claude Code discovers project skills under .claude/skills.
set -eu
root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)
src="$root/.agents/skills"
dest="$root/.claude/skills"
rm -rf "$dest"
mkdir -p "$dest"
cp -R "$src/." "$dest/"
echo "synced skills -> .claude/skills"
