# Rebuild paper.pdf with pdflatex (TeX Live / TinyTeX).
# Usage:  powershell -ExecutionPolicy Bypass -File .\build.ps1
# The build runs in an ASCII-only temp directory, then copies paper.pdf back,
# because pdflatex can fail on non-ASCII working directory names.

$ErrorActionPreference = 'Stop'
$src = $PSScriptRoot

$tiny = Join-Path $env:LOCALAPPDATA 'TinyTeX\TinyTeX\bin\windows'
if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue)) {
    if (Test-Path (Join-Path $tiny 'pdflatex.exe')) {
        $env:PATH = "$tiny;$env:PATH"
    } else {
        throw 'pdflatex not found. Install TeX Live, or TinyTeX (see README.md).'
    }
}

$build = Join-Path $env:TEMP 'twin_paper_build'
New-Item -ItemType Directory -Force -Path $build | Out-Null
Copy-Item (Join-Path $src 'paper.tex') (Join-Path $build 'paper.tex') -Force

Push-Location $build
try {
    foreach ($texPass in 1..3) {
        pdflatex -interaction=nonstopmode -halt-on-error paper.tex | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "pdflatex pass $texPass failed. Inspect paper.log in the temp build dir."
        }
    }
    Select-String -Path 'paper.log' -Pattern 'Output written on' | ForEach-Object { $_.Line }
    Copy-Item 'paper.pdf' (Join-Path $src 'paper.pdf') -Force
    Write-Output 'paper.pdf rebuilt and copied back.'
} finally {
    Pop-Location
}
