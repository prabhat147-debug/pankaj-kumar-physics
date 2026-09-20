@echo off
SET "GIT_PATH=C:\Users\HP\.gemini\antigravity\bin\mingit\cmd"
SET "GIT_BIN=C:\Users\HP\.gemini\antigravity\bin\mingit\mingw64\bin"
SET PATH=%GIT_PATH%;%GIT_BIN%;%PATH%

echo ============================================
echo   PrepPHY Website - GitHub Deployment Tool
echo ============================================
echo.
echo Working on: pankaj-kumar-physics
echo Remote: https://github.com/prabhat147-debug/pankaj-kumar-physics.git
echo.

cd /d "%~dp0"

echo [1/4] Staging all files...
git add .
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: git add failed. Exiting.
    pause
    exit /b 1
)

echo [2/4] Committing changes...
git commit -m "Deploy: PrepPHY website update - %DATE% %TIME%"
if %ERRORLEVEL% NEQ 0 (
    echo NOTE: Nothing new to commit, or commit failed.
)

echo [3/4] Pushing to GitHub...
echo NOTE: A browser window may open for GitHub sign-in. 
echo       Please sign in with the account: prabhat147-debug
echo.
git push origin main
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Push failed. Possible reasons:
    echo   - GitHub authentication needed (sign in when browser opens)
    echo   - No internet connection
    echo   - Repository doesn't exist on GitHub
    pause
    exit /b 1
)

echo.
echo ============================================
echo [4/4] SUCCESS! Website pushed to GitHub!
echo.
echo Live at: https://prabhat147-debug.github.io/pankaj-kumar-physics/
echo.
echo (GitHub Pages may take 1-2 minutes to update)
echo ============================================
echo.
pause
