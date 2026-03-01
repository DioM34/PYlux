import os
import sys
import re
import subprocess
import threading
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PyDownloader v1.3 - Universal Media Downloader for PYlux
    A clean, command-line utility for downloading media from any URL.
    """
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    def print_help():
        print(f"Usage: pydownloader <format> <quality> <url> [options]")
        print(f"\nARGUMENTS:")
        print(f"  format     Output file extension (mp4, mkv, webm, mp3, wav, flac)")
        print(f"  quality    Download quality (low, med, high)")
        print(f"  url        The direct link to the video or audio page")
        print(f"\nOPTIONS:")
        print(f"  -b         Run download in the background")
        print(f"  -h, help   Show this help message")
        print(f"\nEXAMPLES:")
        print(f"  pydownloader mp4 high https://vimeo.com/12345")
        print(f"  pydownloader mp3 med https://soundcloud.com/user/track -b")
        print("")

    # 1. Dependency Check
    try:
        import yt_dlp
    except ImportError:
        print(f"{RED}Error: 'yt-dlp' library not found.{RESET}")
        print(f"Run: {YELLOW}sudo apt install yt-dlp{RESET} or {YELLOW}pipx install yt-dlp{RESET}")
        return

    if not args or args[0] in ["help", "-h"] or len(args) < 3:
        print_help()
        return

    req_format = args[0].lower()
    quality = args[1].lower()
    url = args[2]
    background = "-b" in args

    # 2. File Management
    download_path = os.path.join("home", "Downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # 3. Quality Logic
    q_map = {"low": "worst", "med": "intermediate", "high": "best"}
    selected_q = q_map.get(quality, "best")

    # 4. Progress Hook (Clean & Professional)
    def progress_hook(d):
        if d['status'] == 'downloading':
            p_raw = d.get('_percent_str', '0%')
            clean_p = re.sub(r'\x1b\[[0-9;]*m', '', p_raw).replace('%', '').strip()
            try:
                p_val = float(clean_p)
                filled = int(p_val / 5)
            except:
                filled, p_val = 0, 0.0

            bar = "█" * filled + "-" * (20 - filled)
            sys.stdout.write(f"\r  [{bar}] {p_val:>5.1f}% | {d.get('_speed_str','N/A')} ")
            sys.stdout.flush()
        elif d['status'] == 'finished':
            print(f"\n{GREEN}✔ Download complete! Saved to /home/Downloads/{RESET}")

    # 5. Engine Options
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    # Format handling
    audio_exts = ["mp3", "wav", "flac", "m4a"]
    if req_format in audio_exts:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': req_format,
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({
            'format': f'{selected_q}video+bestaudio/best',
            'merge_output_format': req_format if req_format != "video" else "mp4",
        })

    def perform_download():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"\n{RED}Error: {str(e).split(': ')[-1]}{RESET}")

    # 6. Execution
    if background:
        print(f"{CYAN}Starting background download...{RESET}")
        threading.Thread(target=perform_download, daemon=True).start()
    else:
        print(f"{CYAN}Fetching media...{RESET}")
        perform_download()
