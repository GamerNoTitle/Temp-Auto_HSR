@echo off
:: Close the emulator
start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 shutdown_player
:: Close maa.exe
taskkill /f /im maa.exe
