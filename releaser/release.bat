
@echo off
rem Release helper: list branches, push unpushed branches, and prompt for a new branch name
cd /d %~dp0\.. || exit /b 1

rem remember current branch to restore later
for /f "delims=" %%C in ('git rev-parse --abbrev-ref HEAD') do set "CURRENT_BRANCH=%%C"

rem Support flags: RELEASE_DRYRUN (only list files), RELEASE_FORCE (use --force on push)

echo Current local branches (with tracking info):
git branch -vv
echo.

goto INTERACTIVE

echo Detecting local branches without an upstream - untracked by remote...
setlocal EnableDelayedExpansion
set unpushed_count=0
rem Use git branch -vv and filter lines that do not contain '[' (no upstream shown)
for /f "usebackq tokens=1,2*" %%A in (`git branch -vv ^| findstr /v "\["`) do (
    set "t1=%%A"
    set "t2=%%B"
    if "!t1!"=="*" (
        set "branch=!t2!"
    ) else (
        set "branch=!t1!"
    )
    echo Unpushed: !branch!
    set /a unpushed_count+=1
    set "unpushed_!unpushed_count!=!branch!"
)

echo [DEBUG] unpushed_count=%unpushed_count%
rem echo [DEBUG] unpushed_count=%unpushed_count%
if defined RELEASE_DRYRUN (
    echo RELEASE_DRYRUN=1 — dry-run complete; no pushes performed.
    exit /b 0
)
if %unpushed_count%==0 (
    echo No unpushed local branches found.
)
if %unpushed_count% NEQ 0 goto PUSH_UNPUSHED
goto AFTER_PUSH_CHECK

:PUSH_UNPUSHED
 echo.
 echo %unpushed_count% local branch(es) without upstream found.
 if defined RELEASE_AUTO (
     set "PUSHALL=y"
     echo Auto-mode: pushing unpushed branches.
 ) else (
     set /p PUSHALL=Push all of them to origin? y/N: 
 )
 if /i "%PUSHALL%"=="y" (
        for /L %%i in (1,1,%unpushed_count%) do (
            call set "b=%%unpushed_%%i%%"
            echo === Processing branch: !b! ===
            rem try to switch to branch
            git checkout "!b!"
            if errorlevel 1 (
                echo Failed to checkout !b!. Skipping.
            ) else (
                rem stage only modified + untracked files, excluding releaser/ and venv/
                call :stage_changes
                rem check for staged files
                git diff --cached --name-only | findstr . >nul
                if errorlevel 1 (
                    echo No staged changes to commit on !b!.
                ) else (
                    echo Committing staged changes on !b! - excluding releaser...
                    git commit -m "Release: add untracked files" || echo Commit failed or no changes to commit.
                )
                call :do_push "!b!"
            )
        )
    ) else (
        echo Skipping push of unpushed branches. You can push them later with: git push -u origin ^<branch^>
    )

:AFTER_PUSH_CHECK
echo [DEBUG] AFTER_PUSH_CHECK reached
echo.
if defined RELEASE_AUTO (
    set "NEW_BRANCH="
    echo Auto-mode: skipping new branch creation.
) else (
    set /p NEW_BRANCH=Enter the new branch name (blank to skip): 
)
if "%NEW_BRANCH%"=="" (
    echo No new branch requested. Skipping branch creation.
) else (
    echo Creating and switching to branch "%NEW_BRANCH%"...
    git checkout -b "%NEW_BRANCH%"
    if errorlevel 1 (
        echo Failed to create branch. It may already exist.
    ) else (
        echo Branch created and checked out: %NEW_BRANCH%
        if defined RELEASE_AUTO (
            set "PUSHNEW=y"
            echo Auto-mode: pushing new branch %NEW_BRANCH%.
        ) else (
            set /p PUSHNEW=Push new branch to origin? (y/N): 
        )
        if /i "%PUSHNEW%"=="y" (
            call :stage_changes
            git diff --cached --name-only | findstr . >nul
            if errorlevel 1 (
                echo No staged changes to commit on %NEW_BRANCH%.
            ) else (
                echo Committing staged changes on %NEW_BRANCH% - excluding releaser...
                git commit -m "Release: add untracked files" || echo Commit failed or no changes to commit.
            )
            call :do_push "%NEW_BRANCH%"
        ) else (
            echo Branch not pushed.
        )
    )
)

rem Offer to push all local branches to origin except 'releaser'
if defined RELEASE_AUTO (
    set "PUSH_ALL_EXCEPT=y"
    echo Auto-mode: pushing all branches except 'releaser'.
) else (
    set /p PUSH_ALL_EXCEPT=Push ALL local branches to origin except 'releaser'? y/N: 
)
echo [DEBUG] PUSH_ALL_EXCEPT=%PUSH_ALL_EXCEPT%
if /i "%PUSH_ALL_EXCEPT%"=="y" (
    setlocal EnableDelayedExpansion
    for /f "usebackq tokens=*" %%B in (`git for-each-ref --format="%%(refname:short)" refs/heads`) do (
        set "BR=%%B"
        if /i "!BR!"=="releaser" (
            echo Skipping releaser
        ) else (
            echo === Processing branch: !BR! ===
            git checkout "!BR!"
            if errorlevel 1 (
                echo Failed to checkout !BR!. Skipping.
            ) else (
                call :stage_changes
                git diff --cached --name-only | findstr . >nul
                if errorlevel 1 (
                    echo No staged changes to commit on !BR!.
                ) else (
                    echo Committing staged changes on !BR! - excluding releaser...
                    git commit -m "Release: add untracked files" || echo Commit failed or no changes to commit.
                )
                call :do_push "!BR!"
            )
        )
    )
    endlocal
    rem restore original branch
    git checkout "%CURRENT_BRANCH%" >nul 2>&1
)

endlocal
timeout /t 10 /nobreak >nul
exit /b 0

:: Push helper: %1 = branch
:do_push
set "BRANCH=%~1"
if defined RELEASE_DRYRUN (
    if defined RELEASE_FORCE (
        echo DRYRUN would force-push: %BRANCH% to origin
    ) else (
        echo DRYRUN would push: %BRANCH% to origin
    )
    goto :eof
)

if defined RELEASE_FORCE (
    git push -u origin "%BRANCH%" --force
    if errorlevel 1 (
        echo Failed to push %BRANCH%.
    ) else (
        echo Pushed %BRANCH% successfully.
    )
) else (
    git push -u origin "%BRANCH%"
    if errorlevel 1 (
        echo Failed to push %BRANCH%.
    ) else (
        echo Pushed %BRANCH% successfully.
    )
)

goto :eof
goto INTERACTIVE

:: Interactive flow
:INTERACTIVE
echo.
echo Current local branches:
git branch -vv
echo.
set /p NEW_BRANCH=Enter new branch name to create (blank to cancel): 
if "%NEW_BRANCH%"=="" (
    echo No branch name provided. Exiting.
    goto :eof
)

echo Choose mode: (I)nclude selected entries or (E)xclude selected entries (default I)
set /p MODE=Mode [I/e]: 
if /i "%MODE%"=="E" (
    set "MODE=E"
) else (
    set "MODE=I"
)

rem prepare temp files
set "EXCLUDE_FILE=%TEMP%\release_excludes.txt"
if exist "%EXCLUDE_FILE%" del "%EXCLUDE_FILE%" >nul 2>&1

echo Listing top-level files and directories to choose from:
for /f "delims=" %%D in ('dir /b /a') do (
    rem skip .git, staged_files.txt, and saves directories
    if /i not "%%D"==".git" if /i not "%%D"=="staged_files.txt" if /i not "%%D"=="saves" (
        call :handle_entry "%%D"
    )
)

rem If exclude mode, add all then reset excluded
git checkout -B "%NEW_BRANCH%"
if errorlevel 1 (
    echo Failed to create/switch to %NEW_BRANCH%.
    if exist "%EXCLUDE_FILE%" del "%EXCLUDE_FILE%" >nul 2>&1
    goto :eof
)

if /i "%MODE%"=="E" (
    echo Adding all files, then excluding selected entries...
    git add -A
    if exist "%EXCLUDE_FILE%" (
        for /f "delims=" %%X in ('type "%EXCLUDE_FILE%"') do (
            echo Excluding: %%X
            git reset -- "%%X" >nul 2>&1
        )
    )
) else (
    echo Include-mode: files/dirs were added as you confirmed them.
)

rem commit if staged
git diff --cached --name-only | findstr . >nul
if errorlevel 1 (
    echo No staged changes to commit.
) else (
    git commit -m "Release %NEW_BRANCH%: include/exclude selection" || echo Commit failed.
)

echo Pushing %NEW_BRANCH% to origin (force)...
git push -u origin "%NEW_BRANCH%" --force
if errorlevel 1 (
    echo Failed to push %NEW_BRANCH%.
) else (
    echo Pushed %NEW_BRANCH% successfully.
)

if exist "%EXCLUDE_FILE%" del "%EXCLUDE_FILE%" >nul 2>&1
goto :eof

:: handle_entry "name"
:handle_entry
set "ITEM=%~1"
set /p RESP=Include "%ITEM%"? (y/N): 
if /i "%RESP%"=="y" (
    if /i "%MODE%"=="I" (
        if defined RELEASE_DRYRUN (
            echo DRYRUN would add: %ITEM%
        ) else (
            echo Adding: %ITEM%
            git add "%ITEM%" >nul 2>&1 || echo Failed to add %ITEM%
        )
    ) else (
        rem in exclude mode, record items to exclude later
        echo %ITEM%>>"%EXCLUDE_FILE%"
    )
)
goto :eof

:stage_changes
rem Stages modified and untracked files while excluding releaser/ and venv/
setlocal EnableDelayedExpansion
set "TMPSTAGE=%TEMP%\release_stage_list.txt"
if exist "%TMPSTAGE%" del "%TMPSTAGE%" >nul 2>&1

rem Add modified tracked files
for /f "delims=" %%M in ('git diff --name-only') do (
    set "f=%%M"
    if /i not "!f:~0,9!"=="releaser/" if /i not "!f:~0,9!"=="releaser\" if /i not "!f:~0,5!"=="venv/" if /i not "!f:~0,5!"=="venv\" (
        echo %%M>>"%TMPSTAGE%"
        if defined RELEASE_DRYRUN (
            echo DRYRUN would add: %%M
        ) else (
            git add "%%M" >nul 2>&1 || echo Failed to add %%M
        )
    )
)

rem Add untracked files (exclude standard ignored ones)
for /f "delims=" %%U in ('git ls-files --others --exclude-standard') do (
    set "f=%%U"
    if /i not "!f:~0,9!"=="releaser/" if /i not "!f:~0,9!"=="releaser\" if /i not "!f:~0,5!"=="venv/" if /i not "!f:~0,5!"=="venv\" (
        echo %%U>>"%TMPSTAGE%"
        if defined RELEASE_DRYRUN (
            echo DRYRUN would add: %%U
        ) else (
            git add "%%U" >nul 2>&1 || echo Failed to add %%U
        )
    )
)

rem Ensure releaser is not staged
git reset -- releaser >nul 2>&1
endlocal
goto :eof
