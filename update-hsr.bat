:: Honkai: Star Rail Update Script by GamerNoTitle
:: Installation Process

:: Launch emulator
@REM start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 launch_player
@REM ping 127.0.0.1 -n 31 > nul
@REM :: Install new version
@REM start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 install_apk hsr.apk
@REM ping 127.0.0.1 -n 121 > nul
@REM :: Half an hour to update assets
@REM start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 launch_app com.miHoYo.hkrpg
@REM ping 127.0.0.1 -n 1800 > nul
:: Close the emulator
start "MuMu" "E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuManager.exe" api -v 0 shutdown_player
del "hsr.apk"