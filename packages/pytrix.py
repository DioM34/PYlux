import os
import time
import random
import sys
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PyTrix v2.1 - Digital Rain with Help & Color support.
    """
    colors = {
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "red": Fore.RED,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "white": Fore.WHITE,
        "yellow": Fore.YELLOW
    }

    # --- HELP MENU ---
    if "-h" in args or "--help" in args:
        print(f"\n{Fore.CYAN}═══ PyTrix Help ═══{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Usage:{Style.RESET_ALL} pytrix [-c COLOR] [-s SPEED]")
        print(f"\n{Fore.YELLOW}Options:{Style.RESET_ALL}")
        print(f"  -c <color>    Change rain color (Default: green)")
        print(f"  -s <speed>    Adjust speed (Default: 0.05, smaller is faster)")
        print(f"\n{Fore.YELLOW}Available Colors:{Style.RESET_ALL}")
        print(f"  " + ", ".join([f"{colors[c]}{c}{Style.RESET_ALL}" for c in colors]))
        print(f"\n{Fore.DIM}Press Ctrl+C to exit.{Style.RESET_ALL}\n")
        return

    # Default Settings
    rain_color = Fore.GREEN
    speed = 0.05

    # Argument Parsing
    if "-c" in args:
        try:
            color_choice = args[args.index("-c") + 1].lower()
            if color_choice in colors:
                rain_color = colors[color_choice]
        except: pass

    if "-s" in args:
        try:
            speed = float(args[args.index("-s") + 1])
        except: pass

    try:
        columns, rows = os.get_terminal_size()
    except:
        columns, rows = 80, 24

    drops = [random.randint(0, rows) for _ in range(columns)]
    chars = ["0", "1", "α", "β", "γ", "δ", "λ", "π", " ", " "]

    # Clear screen and hide cursor
    print("\033[2J\033[?25l", end="")

    try:
        while True:
            for i in range(len(drops)):
                char = random.choice(chars)

                # Move cursor to current drop position
                sys.stdout.write(f"\033[{drops[i]+1};{i+1}H")

                # Draw the head
                if random.random() > 0.9:
                    sys.stdout.write(f"{Fore.WHITE}{Style.BRIGHT}{char}")
                else:
                    sys.stdout.write(f"{rain_color}{char}")

                drops[i] += 1

                if drops[i] >= rows:
                    drops[i] = 0

                # Trail eraser
                erase_pos = (drops[i] - 10) % rows
                sys.stdout.write(f"\033[{erase_pos+1};{i+1}H ")

            sys.stdout.flush()
            time.sleep(speed)

    except KeyboardInterrupt:
        print("\033[?25h\033[0m\033[2J\033[H")
        print(f"{Fore.CYAN}PyTrix session terminated by {username}.{Style.RESET_ALL}")
