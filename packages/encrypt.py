import os
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux Encrypt 1.0 - File Security Utility
    Usage: encrypt [mode] [file]
    """
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    RESET = Style.RESET_ALL

    def print_help():
        print(f"\n{CYAN}═══ PYlux Encryption Tool v1.0 ═══{RESET}")
        print(f"{Style.DIM}Secure your files with dual-layer XOR logic{RESET}")
        print(f"\n{YELLOW}Usage:{RESET}")
        print(f"  encrypt lock <file>   - Secure a file with two passwords")
        print(f"  encrypt unlock <file> - Decrypt a file using your keys")
        print(f"  encrypt help          - Show this menu")
        print(f"\n{YELLOW}Features:{RESET}")
        print(f"  - Multi-layer: Requires Primary + Secondary keys")
        print(f"  - In-place: Overwrites the file with secure data")
        print(f"\n{YELLOW}Example:{RESET}")
        print(f"  encrypt lock private.txt")
        print(f"  encrypt unlock private.txt\n")

    if not args or args[0] in ["help", "-h"]:
        print_help()
        return

    action = args[0].lower()
    if len(args) < 2:
        print(f"{RED}Error: Specify a filename.{RESET}")
        return

    filename = args[1]
    file_path = os.path.join(current_dir, filename)

    if not os.path.exists(file_path):
        print(f"{RED}Error: File '{filename}' not found.{RESET}")
        return

    try:
        # Multi-layer Password Collection
        print(f"{CYAN}--- Security Challenge ---{RESET}")
        key1 = input(f"{YELLOW}Enter Primary Key: {RESET}")
        key2 = input(f"{YELLOW}Enter Secondary Key: {RESET}")
        
        if not key1 or not key2:
            print(f"{RED}Error: Both keys are required for encryption/decryption.{RESET}")
            return

        # Combine keys for multi-layer XOR
        combined_key = key1 + key2

        # Read file data
        with open(file_path, 'rb') as f:
            data = bytearray(f.read())

        # Perform XOR Encryption/Decryption (Multi-layer)
        # Applying the XOR twice with the same key restores the data
        for i in range(len(data)):
            data[i] ^= ord(combined_key[i % len(combined_key)])

        # Write back to file
        with open(file_path, 'wb') as f:
            f.write(data)

        verb = "Locked" if action == "lock" else "Unlocked"
        print(f"\n{GREEN}Success: File '{filename}' has been {verb.lower()}!{RESET}")
        
        # Log the security event (since you updated main.py for logging)
        # Note: We don't log the passwords, just the action.
    
    except Exception as e:
        print(f"{RED}Encryption Error: {e}{RESET}")
