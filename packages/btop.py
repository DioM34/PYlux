import os
import time
import platform
import psutil
from datetime import datetime
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux htop 1.0 - Live System Monitor
    Usage: htop
    Press Ctrl+C to exit.
    """
    
    def get_bar(percent, width=20):
        filled = int(width * percent / 100)
        bar = "█" * filled + " " * (width - filled)
        color = Fore.GREEN if percent < 50 else Fore.YELLOW if percent < 80 else Fore.RED
        return f"{color}[{bar}]{Style.RESET_ALL} {percent}%"

    try:
        while True:
            # Clear screen for that 'live' app feel
            os.system('cls' if os.name == 'nt' else 'clear')
            
            now = datetime.now().strftime("%H:%M:%S")
            cpu_count = psutil.cpu_count()
            cpu_percents = psutil.cpu_percent(interval=0.5, percpu=True)
            mem = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            print(f"{Fore.CYAN}{Style.BRIGHT}PYlux htop v1.0{Style.RESET_ALL} - {Fore.WHITE}{now}{Style.RESET_ALL}")
            print(f"Tasks: {len(psutil.pids())} total | User: {username} | Sudo: {is_sudo}")
            print("-" * 50)

            # CPU Section
            print(f"{Fore.MAGENTA}CPU usage per Core:{Style.RESET_ALL}")
            for i, percentage in enumerate(cpu_percents):
                print(f" Core {i}: {get_bar(percentage)}")

            # Memory Section
            print(f"\n{Fore.MAGENTA}Memory usage:{Style.RESET_ALL}")
            print(f" RAM:    {get_bar(mem.percent)} ({mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB)")

            # Disk Section
            print(f"\n{Fore.MAGENTA}Disk usage (/):{Style.RESET_ALL}")
            print(f" DISK:   {get_bar(disk.percent)} ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)")

            # System Info Section
            print(f"\n{Fore.MAGENTA}System Info:{Style.RESET_ALL}")
            print(f" {Fore.WHITE}OS: {platform.system()} {platform.release()}")
            print(f" Python: {platform.python_version()}")
            
            print(f"\n{Style.DIM}Press Ctrl+C to exit htop...{Style.RESET_ALL}")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Exiting htop...{Style.RESET_ALL}")
