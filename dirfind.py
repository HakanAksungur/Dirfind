import argparse
import requests
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Directory discovery tool",
        add_help=False,
        usage="python3 %(prog)s -h website.com -w wordlist.txt"
    )
    parser.add_argument('-h', dest='host', type=str, help='Target website (e.g., website.com)', required=True)
    parser.add_argument('-w', dest='wordlist', type=str, help='Path to the directory wordlist file', required=True)
    parser.add_argument('--help', action='help', help='Show this help message and exit')
    args = parser.parse_args()

    base_url = args.host
    if not (base_url.startswith("http://") or base_url.startswith("https://")):
        base_url = "http://" + base_url

    try:
        with open(args.wordlist, "r") as f:
            directories = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading wordlist file '{args.wordlist}': {e}")
        sys.exit(1)

    print(f"Scanning {base_url} using {len(directories)} directories from '{args.wordlist}'...")

    for directory in directories:
        url = base_url.rstrip("/") + "/" + directory.lstrip("/")
        try:
            response = requests.get(url, timeout=5)
            if response.status_code in [200, 301, 302, 403, 401]:
                print(f"[{response.status_code}] Found: {url}")
        except requests.RequestException as e:
            print(f"Error connecting to {url}: {e}")

if __name__ == '__main__':
    main()
