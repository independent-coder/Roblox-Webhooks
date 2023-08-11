@echo off

rem Check if Python is installed
python --version > nul 2>&1

if %errorlevel% equ 0 (
    rem Python is installed, continue with pip installation
    pip install robloxpy requests browser_cookie3 discord psutil pyautogui discord_webhook
) else (
    rem Python is not found, display an error message
    echo Python was not found. Please install the latest version of Python.
)

pause
exit
