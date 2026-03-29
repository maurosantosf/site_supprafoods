# Script to install SQL Server Express 2022 Silently using Web Installer to download Media first
$ErrorActionPreference = "Stop"
$WorkingDir = "C:\Temp\SQLSetup"
if (-not (Test-Path $WorkingDir)) {
    New-Item -ItemType Directory -Force -Path $WorkingDir | Out-Null
}

$InstallerPath = Join-Path $WorkingDir "SQL2022-SSEI-Expr.exe"

Write-Host "Running Web Installer to download the Media..."
# The web installer can download the media. Let's use /q for quiet mode.
$DownloadArgs = @(
    "/q",
    "/ACTION=Download",
    "/MediaType=CAB",
    "/TargetPath=`"$WorkingDir`""
)

$Process = Start-Process -FilePath $InstallerPath -ArgumentList $DownloadArgs -Wait -NoNewWindow -PassThru

if ($Process.ExitCode -eq 0) {
    Write-Host "Media downloaded successfully."
}
else {
    Write-Host "Media download failed with exit code $($Process.ExitCode)"
    exit $Process.ExitCode
}

# Now find the extracted Setup executable
$SetupPath = Join-Path $WorkingDir "en-US\SETUP.EXE"
if (-not (Test-Path $SetupPath)) {
    # It might extract to just the base folder
    $SetupPath = Join-Path $WorkingDir "SETUP.EXE"
}
if (-not (Test-Path $SetupPath)) {
    Write-Host "SETUP.EXE not found after download!"
    exit 1
}

Write-Host "Running Actual SQL Server Setup..."
$InstallArgs = @(
    "/q",
    "/ACTION=Install",
    "/FEATURES=SQL",
    "/INSTANCENAME=SQLEXPRESS",
    "/SQLSVCACCOUNT=`"NT AUTHORITY\Network Service`"",
    "/SQLSYSADMINACCOUNTS=`"BUILTIN\Administrators`"",
    "/IACCEPTSQLSERVERLICENSETERMS",
    "/UPDATEENABLED=0"
)

$Process2 = Start-Process -FilePath $SetupPath -ArgumentList $InstallArgs -Wait -NoNewWindow -PassThru

if ($Process2.ExitCode -eq 0) {
    Write-Host "SQL Server Express installed successfully."
}
else {
    Write-Host "SQL Server setup failed with exit code $($Process2.ExitCode)"
    exit $Process2.ExitCode
}
