# Prints one line per tool this template expects.
$missing = $false
foreach ($c in 'git','python','gh') {
    if (Get-Command $c -ErrorAction SilentlyContinue) {
        $v = (& $c --version 2>$null | Select-Object -First 1)
        '{0,-8} {1}' -f $c, $v
    } else {
        '{0,-8} MISSING' -f $c
        $missing = $true
    }
}
Write-Output '--- optional ---'
foreach ($c in 'node','pnpm','docker','claude','code') {
    if (Get-Command $c -ErrorAction SilentlyContinue) {
        $v = (& $c --version 2>$null | Select-Object -First 1)
        '{0,-8} {1}' -f $c, $v
    } else {
        '{0,-8} not installed' -f $c
    }
}
if ((Test-Path .claude/settings.json) -and (Select-String -Path .claude/settings.json -Pattern 'PreToolUse' -Quiet)) {
    Write-Output 'hooks    claude settings reference PreToolUse'
} else {
    Write-Output 'hooks    MISSING claude PreToolUse hook'
    $missing = $true
}
if ($missing) { exit 1 }
