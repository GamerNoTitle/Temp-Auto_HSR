@echo off
echo killing adb server...
adb kill-server
echo Done.
:: Launch emulator
start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 launch_player
echo waiting 30 seconds...
ping 127.0.0.1 -n 31 > nul
:: Launch Script
:: start "MuMuPlayer" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe" adb -v 0 connect
adb connect 127.0.0.1:7555
airtest run .\HSR-Auto.air\ --device Android://127.0.0.1:7555?cap_method=JAVACAP --log log/
:: Close the emulator
start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 shutdown_player
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set year=%datetime:~0,4%
set month=%datetime:~4,2%
set day=%datetime:~6,2%
set hour=%datetime:~8,2%
set minute=%datetime:~10,2%
set formatted_time=%year%-%month%-%day% %hour%-%minute%
airtest report HSR-Auto.air --log_root log --outfile "logs/hsr/%formatted_time%.html" --lang zh