import schedule
import time
import subprocess
import os
from datetime import datetime

# 创建保存日志的文件夹
logs_dir = "logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

def run_start_script():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f'[{timestamp}] Starting HSR task...')
    log_folder = os.path.join(logs_dir, "hsr")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, f"{timestamp}.log")
    subprocess.call([r"F:\Git\HSR-Auto\start.bat"], stdout=open(log_file, "a"), stderr=subprocess.STDOUT)

def run_check_update_script():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f'[{timestamp}] Checking HSR update...')
    log_folder = os.path.join(logs_dir, "hsr_check_update")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, f"{timestamp}.log")
    subprocess.call([r"F:\Git\HSR-Auto\CheckUpdate.bat"], stdout=open(log_file, "a"), stderr=subprocess.STDOUT)

def run_maa_exe():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f'[{timestamp}] Starting MAA task...')
    log_folder = os.path.join(logs_dir, "maa")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, f"{timestamp}.log")
    subprocess.call([r"F:\Git\HSR-Auto\start-maa.bat"], stdout=open(log_file, "a"), stderr=subprocess.STDOUT)

def run_kill():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f'[{timestamp}] Kill all.')
    log_folder = os.path.join(logs_dir, "kill")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, f"{timestamp}.log")
    subprocess.call([r"F:\Git\HSR-Auto\kill.bat"], stdout=open(log_file, "a"), stderr=subprocess.STDOUT)

# 在每天的零点和十二点运行 start.bat
schedule.every().day.at("00:00").do(run_start_script)
schedule.every().day.at("12:00").do(run_start_script)

# 在每天的早上十点运行 CheckUpdate.bat
schedule.every().day.at("10:00").do(run_check_update_script)

# 在每天的4:30、12:30、20:30运行 MAA.exe
schedule.every().day.at("04:15").do(run_maa_exe)
schedule.every().day.at("12:45").do(run_maa_exe)
schedule.every().day.at("20:30").do(run_maa_exe)

# 在特定时间关闭模拟器和MAA以防死循环
schedule.every().day.at("04:00").do(run_kill)
schedule.every().day.at("11:50").do(run_kill)
schedule.every().day.at("20:00").do(run_kill)
schedule.every().day.at("23:50").do(run_kill)

print('Scheduling tasks...')
while True:
    schedule.run_pending()
    time.sleep(1)
