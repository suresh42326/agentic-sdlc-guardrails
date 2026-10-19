#!/usr/bin/env sh
# Prints one line per tool this template expects.
# Required tools fail the summary; optional tools are listed after.
missing=0
for c in git python3 gh; do
  if command -v "$c" >/dev/null 2>&1; then
    printf "%-8s %s\n" "$c" "$("$c" --version 2>/dev/null | head -n 1)"
  else
    printf "%-8s MISSING\n" "$c"
    missing=1
  fi
done
echo "--- optional ---"
for c in node pnpm docker claude code; do
  if command -v "$c" >/dev/null 2>&1; then
    printf "%-8s %s\n" "$c" "$("$c" --version 2>/dev/null | head -n 1)"
  else
    printf "%-8s not installed\n" "$c"
  fi
done
if [ -f .claude/settings.json ] && grep -q '"PreToolUse"' .claude/settings.json; then
  echo "hooks    claude settings reference PreToolUse"
else
  echo "hooks    MISSING claude PreToolUse hook"
  missing=1
fi
exit "$missing"
