import os
import time
import random
import sys
from colorama import Fore, Style

# Try to import msvcrt for Windows or use sys/tty for Linux/macOS
try:
    import msvcrt
except ImportError:
    import selectors
    import termios
    import tty

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux Snake 1.0
    Usage: snake
    Controls: WASD to move, Ctrl+C to quit.
    """
    WIDTH = 40
    HEIGHT = 20
    SNAKE_COLOR = Fore.GREEN
    FOOD_COLOR = Fore.RED
    
    # ANSI Sequences for smooth rendering
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    GOTO_HOME = "\033[H"
    CLEAR_SCREEN = "\033[2J"

    def get_input():
        if 'msvcrt' in sys.modules:
            if msvcrt.kbhit():
                return msvcrt.getch().decode('utf-8').lower()
        else:
            # Non-blocking input logic for Linux/macOS
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                sel = selectors.DefaultSelector()
                sel.register(sys.stdin, selectors.EVENT_READ)
                if sel.select(timeout=0):
                    return sys.stdin.read(1).lower()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None

    # Initial state
    snake = [[10, 10], [10, 9], [10, 8]]
    direction = 'd'
    food = [random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2)]
    score = 0

    print(CLEAR_SCREEN + HIDE_CURSOR, end="")

    try:
        while True:
            print(GOTO_HOME, end="")
            
            # Draw Header
            print(f"{Fore.CYAN}PYlux Snake v1.0{Style.RESET_ALL} | Score: {Fore.YELLOW}{score}{Style.RESET_ALL}")
            
            # Capture Input
            key = get_input()
            if key in ['w', 'a', 's', 'd']:
                # Prevent reversing directly into self
                if (key == 'w' and direction != 's') or \
                   (key == 's' and direction != 'w') or \
                   (key == 'a' and direction != 'd') or \
                   (key == 'd' and direction != 'a'):
                    direction = key

            # Update Head
            head = list(snake[0])
            if direction == 'w': head[0] -= 1
            if direction == 's': head[0] += 1
            if direction == 'a': head[1] -= 1
            if direction == 'd': head[1] += 1

            # Game Over Checks (Walls or Self)
            if head[0] <= 0 or head[0] >= HEIGHT-1 or head[1] <= 0 or head[1] >= WIDTH-1 or head in snake:
                break

            snake.insert(0, head)

            # Check Food
            if head == food:
                score += 1
                food = [random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2)]
            else:
                snake.pop()

            # Render Screen
            for r in range(HEIGHT):
                line = ""
                for c in range(WIDTH):
                    if r == 0 or r == HEIGHT-1 or c == 0 or c == WIDTH-1:
                        line += f"{Fore.WHITE}# "
                    elif [r, c] == snake[0]:
                        line += f"{SNAKE_COLOR}O "
                    elif [r, c] in snake:
                        line += f"{SNAKE_COLOR}o "
                    elif [r, c] == food:
                        line += f"{FOOD_COLOR}* "
                    else:
                        line += "  "
                print(line)
            
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass
    finally:
        print(SHOW_CURSOR + CLEAR_SCREEN + GOTO_HOME)
        print(f"{Fore.RED}GAME OVER!{Style.RESET_ALL} Final Score: {score}")
        print(f"Logged activity for user: {username}")
