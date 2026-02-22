import os
from colorama import Fore, Style

# Ensure the notes directory exists
NOTES_DIR = "notes"
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux Notes Manager 1.0
    Usage:
      notes save <name> "<content>"
      notes view <name>
      notes ls
      notes rm <name>
    """
    C = Fore.CYAN + Style.BRIGHT
    W = Fore.WHITE + Style.BRIGHT
    G = Fore.GREEN
    R = Style.RESET_ALL

    if not args:
        print(f"\n{C}PYlux Notes Manager{R}")
        print(f"{W}Usage:{R} notes [save | view | ls | rm]")
        return

    command = args[0].lower()

    if command == "save":
        if len(args) < 3:
            print(f"{Fore.RED}Error: Usage: notes save <name> \"<content>\"{R}")
            return
        note_name = args[1]
        content = " ".join(args[2:])
        filepath = os.path.join(NOTES_DIR, f"{note_name}.txt")
        
        with open(filepath, "w") as f:
            f.write(content)
        print(f"{G}Note '{note_name}' saved successfully.{R}")

    elif command == "view":
        if len(args) < 2:
            print(f"{Fore.RED}Error: Specify a note name.{R}")
            return
        note_name = args[1]
        filepath = os.path.join(NOTES_DIR, f"{note_name}.txt")
        
        if os.path.exists(filepath):
            print(f"\n{C}--- Viewing: {note_name} ---{R}")
            with open(filepath, "r") as f:
                print(f"{W}{f.read()}{R}")
            print(f"{C}-----------------------{R}\n")
        else:
            print(f"{Fore.RED}Note '{note_name}' not found.{R}")

    elif command == "ls":
        files = [f.replace(".txt", "") for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
        print(f"\n{C}Your Saved Notes:{R}")
        if not files:
            print(f"{Style.DIM}No notes found.{R}")
        for f in files:
            print(f"{G}* {W}{f}{R}")
        print()

    elif command == "rm":
        if len(args) < 2:
            print(f"{Fore.RED}Error: Specify a note to remove.{R}")
            return
        note_name = args[1]
        filepath = os.path.join(NOTES_DIR, f"{note_name}.txt")
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"{G}Note '{note_name}' deleted.{R}")
        else:
            print(f"{Fore.RED}Note not found.{R}")

    else:
        print(f"{Fore.RED}Unknown command: {command}{R}")
