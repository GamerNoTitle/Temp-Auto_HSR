@echo off
echo killing adb server...
adb kill-server
echo Done.
:: Launch emulator
start "MuMuPlayer" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe" api -v 0 launch_player
echo waiting 30 seconds...
ping 127.0.0.1 -n 31 > nul
:: Launch Script
start "MuMuPlayer" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe" adb -v 0 connect
adb connect 127.0.0.1:7555
airtest run .\HSR-Auto.air\ --device Android://127.0.0.1:7555?cap_method=JAVACAP --log log/
:: Close the emulator
start "MuMuPlayer" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe" api -v 0 shutdown_player
pause