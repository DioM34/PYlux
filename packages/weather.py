import urllib.request
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    Fetches live weather data.
    Usage: weather [city_name]
    """
    # If no city is provided, wttr.in guesses based on IP
    city = args[0] if args else ""

    # We use ?0 to get a simplified version for the terminal
    # and ?q to make it compact
    url = f"https://wttr.in/{city}?0?q?T"

    print(f"{Fore.CYAN}Fetching weather data for {city if city else 'your location'}...")

    try:
        # We need to set a User-Agent so wttr.in knows we are a terminal/curl-like tool
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'curl/7.64.1'}
        )

        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')

            print("\n" + "="*40)
            # Print the data (wttr.in already provides ANSI colors)
            print(data)
            print("="*40 + "\n")

    except Exception as e:
        print(f"{Fore.RED}Error: Could not connect to weather service. ({e})")
