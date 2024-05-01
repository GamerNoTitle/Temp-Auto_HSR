:: Honkai: Star Rail Update Script by GamerNoTitle
:: Installation Process

:: Launch emulator
"E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe" api -v 0 launch_player
ping 127.0.0.1 -n 121 > nul
:: Install new version
MuMuManager.exe api -v 0 install_apk hsr.apk
ping 127.0.0.1 -n 121 > nul
:: Half an hour to update assets
"E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe" api -v 0 launch_app [package]
ping 127.0.0.1 -n 1800 > nul
:: Close the emulator
"E:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe" api -v 0 shutdown_player