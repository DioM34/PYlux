import os
import time
import platform
import psutil
from datetime import datetime
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux htop 1.1 - Smooth Live System Monitor
    """
    # ANSI escape code to move cursor to home (0,0) and hide cursor
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    GOTO_HOME = "\033[H"
    CLEAR_SCREEN = "\033[2J"

    def get_bar(percent, width=20):
        filled = int(width * percent / 100)
        bar = "█" * filled + " " * (width - filled)
        color = Fore.GREEN if percent < 50 else Fore.YELLOW if percent < 80 else Fore.RED
        return f"{color}[{bar}]{Style.RESET_ALL} {percent}%"

    # Initial clear
    print(CLEAR_SCREEN + HIDE_CURSOR, end="")

    try:
        while True:
            # Move cursor to top instead of clearing everything
            print(GOTO_HOME, end="")
            
            now = datetime.now().strftime("%H:%M:%S")
            cpu_percents = psutil.cpu_percent(interval=0.5, percpu=True)
            mem = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # Header
            print(f"{Fore.CYAN}{Style.BRIGHT}PYlux htop v1.1{Style.RESET_ALL} - {Fore.WHITE}{now}{Style.RESET_ALL}")
            print(f"Tasks: {len(psutil.pids()):<4} | User: {username:<10} | Sudo: {str(is_sudo):<5}")
            print("-" * 55)

            # CPU Section
            print(f"{Fore.MAGENTA}CPU Usage per Core:{Style.RESET_ALL}")
            for i, percentage in enumerate(cpu_percents):
                # Added padding to core numbers to prevent shifting
                print(f" Core {i:2}: {get_bar(percentage)}")

            # Memory & Disk
            print(f"\n{Fore.MAGENTA}Memory & Storage:{Style.RESET_ALL}")
            print(f" RAM:    {get_bar(mem.percent)} ({mem.used // (1024**2):4}MB / {mem.total // (1024**2):4}MB)")
            print(f" DISK:   {get_bar(disk.percent)} ({disk.used // (1024**3):3}GB / {disk.total // (1024**3):3}GB)")

            # System Info Section
            print(f"\n{Fore.MAGENTA}System Info:{Style.RESET_ALL}")
            print(f" OS:     {platform.system()} {platform.release()}")
            print(f" Python: {platform.python_version()}")
            
            print(f"\n{Style.DIM}Press Ctrl+C to exit htop...{Style.RESET_ALL}")
            
            # Small delay
            time.sleep(0.1)

    except KeyboardInterrupt:
        print(SHOW_CURSOR + f"\n{Fore.YELLOW}Exiting htop...{Style.RESET_ALL}")
