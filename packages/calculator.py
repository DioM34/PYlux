import math
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux Calculator 1.0
    Usage: calc <expression> or just 'calc' for interactive mode.
    """
    PURPLE = Fore.MAGENTA + Style.BRIGHT
    CYAN = Fore.CYAN + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Style.RESET_ALL

    print(f"\n{PURPLE}PYlux Calculator v1.0{RESET}")
    print(f"{Style.DIM}Type 'exit' to quit. Use ** for power, sqrt() for roots.{RESET}")
    print(f"{WHITE}—" * 30)

    def calculate(expression):
        try:
            # Allow use of math functions without typing math.
            safe_dict = {
                "abs": abs, "round": round, "pow": pow,
                "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,
                "tan": math.tan, "pi": math.pi, "e": math.e
            }
            # eval is safe here in a controlled virtual OS context
            result = eval(expression, {"__builtins__": None}, safe_dict)
            return result
        except Exception as e:
            return f"Error: {e}"

    # If args are passed (e.g., calc 5+5), do a quick calculation
    if args:
        expr = "".join(args)
        res = calculate(expr)
        print(f"{CYAN}Result: {WHITE}{res}{RESET}\n")
        return

    # Interactive Mode
    while True:
        try:
            user_input = input(f"{CYAN}calc> {WHITE}").strip().lower()
            if user_input in ['exit', 'quit', 'q']:
                print(f"{PURPLE}Exiting calculator...{RESET}\n")
                break
            if not user_input:
                continue

            result = calculate(user_input)
            print(f"{Fore.GREEN}= {result}{RESET}")
        except KeyboardInterrupt:
            print("")
            break
