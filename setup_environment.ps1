param(
    [string]$Python = "python",
    [string]$VenvPath = ".venv"
)

$ErrorActionPreference = "Stop"

Write-Host "Creating virtual environment at $VenvPath ..."
& $Python -m venv $VenvPath

$PythonExe = Join-Path $VenvPath "Scripts\python.exe"
if (-not (Test-Path $PythonExe)) {
    throw "Could not find virtual-environment Python at $PythonExe"
}

Write-Host "Upgrading pip ..."
& $PythonExe -m pip install --upgrade pip

Write-Host "Installing project dependencies from requirements.txt ..."
& $PythonExe -m pip install -r requirements.txt

Write-Host ""
Write-Host "Environment is ready."
Write-Host "Activate it with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "Example PDF extraction command:"
Write-Host "  python pdf_equation_pipeline.py --paper-number 9 --save-docling-markdown output/pdf/paper_9_docling.md"
