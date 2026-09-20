@echo off
title Uploading Pankaj Kumar Physics Mentorship to GitHub
echo ========================================================
echo   Uploading Website to:
echo   https://github.com/prabhat147-debug/pankaj-kumar-physics
echo ========================================================
echo.

set PATH=C:\Users\HP\.gemini\antigravity\bin\mingit\cmd;C:\Users\HP\.gemini\antigravity\bin\mingit\mingw64\bin;%PATH%

echo [1/3] Adding files to git...
git add .
git commit -m "Complete physics mentorship website for Er. Pankaj Kumar" 2>nul

echo [2/3] Verifying GitHub repository link...
git remote remove origin 2>nul
git remote add origin https://github.com/prabhat147-debug/pankaj-kumar-physics.git
git branch -M main

echo [3/3] Uploading files to GitHub...
echo.
echo NOTE: If a GitHub window pops up asking you to "Sign in with your browser",
echo       please click it and authorize. It takes just 2 seconds!
echo.
git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo  SUCCESS! Website uploaded successfully to GitHub!
    echo ========================================================
    echo.
    echo Next step to view live website on GitHub Pages:
    echo 1. Go to https://github.com/prabhat147-debug/pankaj-kumar-physics/settings/pages
    echo 2. Under Branch, select 'main' and click 'Save'.
    echo.
) else (
    echo.
    echo An issue occurred during upload. Check if you authorized the browser window.
    echo.
)

pause
