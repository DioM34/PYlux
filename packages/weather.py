import urllib.request
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    Enhanced Weather & Astronomy Tool for PYlux OS.
    Usage: 
      weather [city]            - Current weather and today's table
      weather [city] --tomorrow  - Forecast for the next day
    """
    # Check for the tomorrow flag
    show_tomorrow = "--tomorrow" in args
    city_args = [arg for arg in args if arg != "--tomorrow"]
    city = city_args[0] if city_args else ""
    
    # ASCII Logo
    logo = f"""{Fore.YELLOW}
      \\   /
       .-.
    -- (   ) --
       `-´
      /   \\{Style.RESET_ALL}"""

    print(logo)
    
    target_label = "tomorrow" if show_tomorrow else "today"
    print(f"{Fore.CYAN}Fetching {target_label}'s forecast for {city if city else 'your location'}...{Style.RESET_ALL}")

    def fetch_wttr(params):
        try:
            url = f"https://wttr.in/{city}{params}"
            # Using curl user-agent ensures we get the formatted text output
            req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.64.1'})
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8').strip()
        except:
            return None

    # Fetch main weather (compact format)
    # ?0 = today, ?1 = tomorrow
    day_param = "1" if show_tomorrow else "0"
    
    # We fetch with formatting: ?0?q?T for summary, but for the table we use:
    # 'n' = narrow format, '0' = current only, but let's use the full v2 report
    # and strip it down to what we need.
    weather_report = fetch_wttr(f"?{day_param}?n?F") 

    if not weather_report:
        print(f"{Fore.RED}Error: Could not connect to weather service.{Style.RESET_ALL}")
        return

    print("\n" + Fore.WHITE + "—" * 60)
    
    # Display the structured table provided by wttr.in
    # This includes time, temperature (Celsius), and condition
    print(f"{Fore.MAGENTA}{target_label.upper()} FORECAST & DETAILS:{Style.RESET_ALL}")
    print(weather_report)
    
    print(Fore.WHITE + "—" * 60)
    if not show_tomorrow:
        print(f"{Fore.DIM}Tip: Type 'weather {city} --tomorrow' to see the next day.{RESET}")
    print("\n")
