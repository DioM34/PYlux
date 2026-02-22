import os
from colorama import Fore, Style

# This points to the file being written by your updated main.py
LOG_FILE = os.path.join("core", "system.log")

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux System Logs 1.0
    Usage: 
      logs          - View recent activity
      logs search <term> - Find specific events
      logs clear    - Wipe logs (Requires sudo)
    """
    HEADER = Fore.MAGENTA + Style.BRIGHT
    CYAN = Fore.CYAN
    RESET = Style.RESET_ALL

    if not os.path.exists(LOG_FILE):
        print(f"{Fore.YELLOW}No system logs found. Start typing commands to generate some!{RESET}")
        return

    # Feature: Clear Logs (Sudo Required)
    if args and args[0] == "clear":
        if not is_sudo:
            print(f"{Fore.RED}Error: 'logs clear' requires sudo.{RESET}")
        else:
            try:
                os.remove(LOG_FILE)
                print(f"{Fore.GREEN}System logs successfully wiped.{RESET}")
            except Exception as e:
                print(f"{Fore.RED}Error clearing logs: {e}{RESET}")
        return

    print(f"\n{HEADER}═══ PYlux System Activity Log ═══{RESET}")
    
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            
        # Feature: Search
        if args and args[0] == "search" and len(args) > 1:
            query = args[1].lower()
            lines = [l for l in lines if query in l.lower()]
            print(f"{Style.DIM}Showing results for: '{query}'{RESET}")

        # Default: Show last 15 entries for a clean view
        display_lines = lines[-15:]
        if not display_lines:
            print(f"{Style.DIM} No log entries match your criteria.{RESET}")
        else:
            for line in display_lines:
                # Highlight root/sudo actions in Red, others in White
                if "USER: root" in line:
                    print(f"{Fore.RED}{line.strip()}{RESET}")
                else:
                    print(f"{Fore.WHITE}{line.strip()}{RESET}")
                
    except Exception as e:
        print(f"{Fore.RED}Error reading logs: {e}{RESET}")

    print(f"{HEADER}══════════════════════════════════{RESET}\n")
