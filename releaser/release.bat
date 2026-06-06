@echo off
setlocal enabledelayedexpansion

echo.
echo ==============================
echo   GIT RELEASE CREATOR
echo ==============================
echo.

:: Check if this is a git repo
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ERROR: This folder is not a git repository.
    echo Run: git init
    pause
    exit /b
)

:: Show existing release branches
echo Existing release branches:
git branch -r | findstr release-

echo.
echo ==============================
echo.

:: Get version from user
set /p VERSION=Enter version (example v1.0.0): 

if "%VERSION%"=="" (
    echo ERROR: Version cannot be empty.
    pause
    exit /b
)

set BRANCH=release-%VERSION%

echo.
echo Creating branch: %BRANCH%
echo.

:: Switch to main and update
git checkout main
git pull

if errorlevel 1 (
    echo ERROR: Failed to switch to main branch.
    pause
    exit /b
)

:: Create new release branch
git checkout -b %BRANCH%

:: Add all changes
git add .

:: Commit safely (avoid empty commit crash)
git commit -m "Release %VERSION%" >nul 2>&1

if errorlevel 1 (
    echo WARNING: Nothing to commit (maybe no changes).
)

:: Push branch
git push -u origin %BRANCH%

if errorlevel 1 (
    echo.
    echo ERROR: Push failed.
    echo Make sure:
    echo - You are logged into GitHub via browser once
    echo - Repo remote is set (git remote -v)
    pause
    exit /b
)

echo.
echo ==============================
echo SUCCESS!
echo Released: %BRANCH%
echo ==============================
pause