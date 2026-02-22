import urllib.request
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    Enhanced Weather & Astronomy Tool for PYlux OS.
    Usage: weather [city_name]
    """
    city = args[0] if args else ""
    
    # ASCII Logo
    logo = f"""{Fore.YELLOW}
      \   /
       .-.
    -- (   ) --
       `-´
      /   \{Style.RESET_ALL}"""

    print(logo)
    print(f"{Fore.CYAN}Fetching live data for {city if city else 'your location'}...{Style.RESET_ALL}")

    def fetch_wttr(params):
        try:
            url = f"https://wttr.in/{city}{params}"
            req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.64.1'})
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8').strip()
        except:
            return None

    # Fetch main weather (compact format) and astronomy data
    weather_data = fetch_wttr("?0?q?T")
    astro_data = fetch_wttr("?format=%D+%S+%s+%m") 

    if not weather_data:
        print(f"{Fore.RED}Error: Could not connect to weather service.{Style.RESET_ALL}")
        return

    print("\n" + Fore.WHITE + "—" * 50)
    
    # Display Weather
    print(f"{Fore.MAGENTA}CURRENT WEATHER:{Style.RESET_ALL}")
    print(weather_data)
    
    # Display Astronomy (Dawn, Sunrise, Sunset, Moon Phase)
    if astro_data:
        # astro_data looks like: "06:12 06:40 18:20 🌕"
        parts = astro_data.split()
        if len(parts) >= 4:
            print("\n" + Fore.MAGENTA + "ASTRONOMY & TIME:" + Style.RESET_ALL)
            print(f"{Fore.CYAN}  🌅 Sunrise: {Fore.WHITE}{parts[1]}")
            print(f"{Fore.CYAN}  🌇 Sunset:  {Fore.WHITE}{parts[2]}")
            print(f"{Fore.CYAN}  🌙 Moon:    {Fore.WHITE}{parts[3]}")
    
    print(Fore.WHITE + "—" * 50 + "\n")
