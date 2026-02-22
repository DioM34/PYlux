import os
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux File Explorer 1.1
    Usage: 
      explorer [path]          - List files and directories
      explorer read <file>     - Quickly view file content
    """
    # Visual Constants
    FOLDER_ICON = Fore.CYAN + "📁 "
    FILE_ICON = Fore.WHITE + "📄 "
    HEADER = Fore.MAGENTA + Style.BRIGHT
    RESET = Style.RESET_ALL

    # Feature: Quick Read
    if args and args[0] == "read":
        if len(args) < 2:
            print(f"{Fore.RED}Usage: explorer read <filename>{RESET}")
            return
        
        file_target = os.path.join(current_dir, args[1])
        if os.path.exists(file_target) and os.path.isfile(file_target):
            print(f"\n{HEADER}--- Reading: {args[1]} ---{RESET}")
            try:
                with open(file_target, 'r') as f:
                    print(f.read())
            except Exception as e:
                print(f"{Fore.RED}Could not read file: {e}{RESET}")
            print(f"{HEADER}----------------------------{RESET}\n")
        else:
            print(f"{Fore.RED}File '{args[1]}' not found.{RESET}")
        return

    # Feature: Directory Listing (Default)
    target_dir = args[0] if args else current_dir
    print(f"\n{HEADER}--- PYlux Explorer: {target_dir} ---{RESET}")

    try:
        if not os.path.exists(target_dir):
            print(f"{Fore.RED}Error: Path '{target_dir}' does not exist.{RESET}")
            return

        items = os.listdir(target_dir)
        folders = sorted([f for f in items if os.path.isdir(os.path.join(target_dir, f))])
        files = sorted([f for f in items if os.path.isfile(os.path.join(target_dir, f))])

        print(f"{'Type':<6} {'Name':<20} {'Size':<10}")
        print("-" * 40)

        for folder in folders:
            print(f"{FOLDER_ICON:<5} {Fore.CYAN}{folder:<20}{RESET} {'DIR':<10}")

        for file in files:
            file_path = os.path.join(target_dir, file)
            size_bytes = os.path.getsize(file_path)
            size_str = f"{size_bytes} B" if size_bytes < 1024 else f"{size_bytes / 1024:.1f} KB"
            print(f"{FILE_ICON:<5} {Fore.WHITE}{file:<20}{RESET} {size_str:<10}")

        print(f"{HEADER}--------------------------------------{RESET}")
        print(f"{Style.DIM}Tip: Use 'explorer read <file>' to view contents.{RESET}\n")

    except Exception as e:
        print(f"{Fore.RED}Explorer Error: {e}{RESET}")
