@echo off
python AutoUpdate.py
if exist "hsr.apk" (
    start update-hsr.bat
) else (
    REM None
)