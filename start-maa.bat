@echo off
:: Launch emulator
start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 launch_player
ping 127.0.0.1 -n 31 > nul
"F:\MAA\MAA.exe"
:: Close the emulator
start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 shutdown_player