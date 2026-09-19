@echo off
title Publish Er. Pankaj Kumar Website to GitHub
echo ========================================================
echo   Publish Er. Pankaj Kumar Physics Mentorship to GitHub
echo ========================================================
echo.
python "%~dp0push_to_github.py" %*
echo.
pause
