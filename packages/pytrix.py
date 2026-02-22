import os
import time
import random
import sys
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PyTrix v1.0 - Digital Rain for PYlux
    Usage: pytrix [-c COLOR] [-s SPEED]
    Colors: green (default), blue, red, cyan, magenta, white
    """
    # Color Mapping
    colors = {
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "red": Fore.RED,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "white": Fore.WHITE
    }

    # Default Settings
    rain_color = Fore.GREEN
    speed = 0.05

    # Simple Argument Parsing
    if "-c" in args:
        try:
            color_choice = args[args.index("-c") + 1].lower()
            if color_choice in colors:
                rain_color = colors[color_choice]
        except IndexError:
            pass
    
    if "-s" in args:
        try:
            speed = float(args[args.index("-s") + 1])
        except (IndexError, ValueError):
            speed = 0.05

    # Terminal Dimensions
    try:
        columns, rows = os.get_terminal_size()
    except OSError:
        columns, rows = 80, 24

    # Rain State: drops stores the current row position for each column
    drops = [random.randint(-rows, 0) for _ in range(columns)]
    chars = ["0", "1", "α", "β", "γ", "δ", "λ", "π", " ", " ", " "]

    print("\033[2J\033[H\033[?25l", end="") # Clear screen and hide cursor

    try:
        while True:
            line = ""
            for i in range(columns):
                # Update drop position
                if drops[i] >= rows:
                    drops[i] = random.randint(-5, 0)
                
                # Logic: If the drop is "on screen", print a random char
                if drops[i] > 0:
                    # Occasionally make the head of the rain white/bright
                    if random.random() > 0.95:
                        line += f"{Fore.WHITE}{Style.BRIGHT}{random.choice(chars)}"
                    else:
                        line += f"{rain_color}{random.choice(chars)}"
                else:
                    line += " "
                
                drops[i] += 1
            
            # Print the full line and move cursor back to top for next frame
            sys.stdout.write(f"\033[H{line}\n")
            sys.stdout.flush()
            time.sleep(speed)

    except KeyboardInterrupt:
        # Restore terminal on exit
        print("\033[?25h\033[0m\033[2J\033[H")
        print(f"{Fore.CYAN}PyTrix session terminated by {username}.{Style.RESET_ALL}")
