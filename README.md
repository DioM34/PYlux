# 🐧 PYlux

**PYlux** is a Python-based sandbox environment that simulates a Linux-like experience. It is 100% open-source, lightweight, and free for everyone.

<img width="1279" height="719" alt="pylux-image" src="https://github.com/user-attachments/assets/322e1787-38e1-423b-b912-5ac9e7781072" />

> [!IMPORTANT]
> **DISCLAIMER:** This project was developed through "vibecoding" with the help of [Claude](https://claude.ai) by Anthropic. If you encounter bugs, please contribute by opening an issue or a pull request!

---

## ✨ Features

* **📦 The `py` Package Manager** – Install, remove, and upgrade packages. Supports multiple community repositories via `py repo add/remove/list`.
* **📂 Real Directory Logic** – Experience a system structured like Linux with `/bin`, `/core`, `/boot` and `/packages`.
* **🎨 Customizable MOTD** – Personalize your startup experience by editing the `motd.txt`.
* **🛡️ Sandbox Mode** – Stay within your PYlux environment without accidentally exiting to your host system.
* **🔐 Sudo & Privilege System** – Protected commands require `sudo` with masked password input.
* **🔁 Tab Autocomplete** – Auto-complete commands and filenames as you type.
* **📜 Command History** – Full session history with export support via `history -e`.
* **🚀 Active Package Support** – The library of available packages is constantly expanding.
* **🍃 Resource Efficient** – Significantly lighter on hardware than running a full Virtual Machine (VM).
* **🤝 Community Driven** – Built on community requests and ideas.

---

## 📂 System Structure

PYlux mimics a standard Unix-like hierarchy to keep system files and user scripts organized:

* **`/bin`**: Contains all core system commands and binaries.
* **`/core`**: The "heart" of the system. Contains boot files, login logic, and user creation scripts.
* **`/packages`**: The landing zone for all external tools installed via the `py` manager.
* **`/boot`**: The directory for the bootmessages and the logo.
* **`config.json`**: Single source of truth for system version and OS configuration.
* **`motd.txt`**: Edit this file to change the ASCII logo and welcome message shown at boot.

---

## ⌨️ Core Commands

Once inside the PYlux terminal, you can use these built-in commands located in `/bin`:

| Command | Description |
| :--- | :--- |
| `help` | Displays the help menu and available commands. |
| `ls` | Lists files and folders in your current directory. |
| `cd <dir>` | Change your current working directory. |
| `mkdir <name>` | Create a new directory within the sandbox. |
| `touch <file>` | Create a new empty file or update a file's timestamp. |
| `rm <file>` | Remove a file or directory. |
| `cp <src> <dst>` | Copy a file to a new location. |
| `mv <src> <dst>` | Move or rename a file. |
| `cat <file>` | Print the contents of a file. |
| `nano <file>` | Open a file in the built-in text editor. |
| `echo <text>` | Print text to the terminal. |
| `pwd` | Print the current working directory. |
| `whoami` | Show the currently logged-in user. |
| `history` | View your command history. Use `-c` to clear, `-e <file>` to export. |
| `man <cmd>` | Show the manual/help for a command. |
| `clear` | Clears the terminal screen for a fresh start. |
| `sudo <cmd>` | Run a command with elevated privileges. |
| `su` | Switch to root session. |
| `uptime` | Show how long the system has been running. |
| `date` | Display the current date and time. |
| `py install <pkg>` | Install a package from the repository. |
| `py remove <pkg>` | Remove an installed package. |
| `py update` | Sync the latest package list from all repos. |
| `py upgrade` | Upgrade all installed packages. |
| `py list` | Browse all available packages. |
| `py repo list` | Show all configured package repositories. |
| `py repo add <name> <url>` | Add a community package repository. |
| `py repo remove <name>` | Remove a community repository. |

---

## 🛠️ Dependencies

To run PYlux, ensure you meet the following requirements:

* **Python:** `3.13+`
* **OS:** Windows 10/11 or Linux
* **Required:** `colorama` — install via `pip install colorama`
* **Optional:** `pip` (for extended package support)

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DioM34/PYlux.git
   ```

2. **Navigate to the folder:**
   ```bash
   cd PYlux
   ```

3. **Install dependencies:**
   ```bash
   pip install colorama
   ```

4. **Run the simulation:**
   ```bash
   python main.py
   ```

> [!TIP]
> On your first boot, the system will trigger the **User Creation Wizard** located in the `/core` directory. Follow the prompts to set up your username and password!

---

## 🌐 Community Repositories

PYlux 1.1 supports community-hosted package repos! If you want to host your own packages:

1. Create a `packages.json` file following the same format as the [official repo](https://github.com/DioM34/PYlux).
2. Host it anywhere (GitHub raw, your own server, etc.).
3. Users can add it with:
   ```
   sudo py repo add myrepo https://raw.githubusercontent.com/you/yourrepo/main/packages.json
   py update
   ```

---

## 💡 Customization

**Changing the Welcome Screen**  
Open `core/motd.txt` in any editor. You can add your own **ASCII Art** or custom instructions. This will be displayed every time `main.py` is executed, right before the command prompt appears.

**Changing the version**  
The version number lives in `config.json` at the root. Bumping it there will automatically reflect across the entire system.

---

## ❤️ Support & Contributing

If you enjoy using PYlux, please consider giving this project a ⭐ Star. It motivates me to keep updating and improving the code!

- **Suggestions:** Open a Pull Request with your ideas.
- **Bugs:** Report issues via the GitHub Issues tab.
- **Feedback:** I actively listen to community requests!

Made with ❤️ and [Claude](https://claude.ai) by Anthropic.
