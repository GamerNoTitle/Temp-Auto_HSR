# Temp-Auto_HSR

因为近一个月没时间上崩铁所以萌生了让电脑自动帮我肝崩铁的想法，于是花了三个小时编写、调试做出了这个，仅供参考

**需要安装python环境，使用airtest**

- start.bat 一键开始，是设置计划任务的时候的入口点
- CheckUpdate.bat 检查崩铁更新，因为5.9更新2.2，但是那会不在家，所以下了个检测更新
- start-maa.bat 启动MAA，因为我发现我的MAA启动mumu会失败，所以用mumu自带的管理器启动后直接打开MAA进行任务，任务进行完MAA关闭后bat会把mumu关掉