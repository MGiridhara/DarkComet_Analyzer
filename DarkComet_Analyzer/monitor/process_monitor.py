import psutil
import time
import csv
from datetime import datetime

CPU_THRESHOLD = 50

suspicious_keywords = [
    "hack",
    "inject",
    "malware",
    "trojan",
    "rat",
    "keylogger"
]

LOG_FILE = "logs/activity_log.csv"

def check_suspicious_process(name):

    name = name.lower()

    for keyword in suspicious_keywords:
        if keyword in name:
            return True

    return False

def log_activity(timestamp, pid, name, cpu, memory, status):

    with open(LOG_FILE, mode='a', newline='') as file:

        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            pid,
            name,
            cpu,
            f"{memory:.2f}",
            status
        ])

def monitor_processes():

    print("=" * 70)
    print("DarkComet RAT Behavioral Analyzer Using AI - Logging Process Monitor")
    print("=" * 70)

    while True:

        print("\nScanning Running Processes...\n")

        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):

            try:
                pid = process.info['pid']
                name = process.info['name']
                cpu = process.info['cpu_percent']
                memory = process.info['memory_percent']

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                status = "SAFE"

                print(f"PID: {pid} | {name} | CPU: {cpu}% | Memory: {memory:.2f}%")

                if cpu > CPU_THRESHOLD:
                    print(f"[WARNING] High CPU Usage Detected -> {name}")
                    status = "HIGH_CPU"

                if check_suspicious_process(name):
                    print(f"[ALERT] Suspicious Process Name Detected -> {name}")
                    status = "SUSPICIOUS"

                log_activity(timestamp, pid, name, cpu, memory, status)

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                pass

        print("\nLogs Saved Successfully...")
        print("Next Scan In 5 Seconds...\n")

        time.sleep(5)

monitor_processes()