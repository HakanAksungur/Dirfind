# Web Directory Discovery Tool

This project is a simple Python application that scans a specified website for hidden directories. It uses a user-provided target website and directory wordlist to send HTTP requests to potential directory paths. If a request returns an interesting HTTP status code (e.g., 200, 301, 302, 403, 401), the URL is immediately displayed.

## Features

- **User Input:** Accepts a target website and a directory wordlist file via command-line arguments.
- **URL Normalization:** Automatically prepends "http://" to the website if no scheme is provided.
- **Wordlist Processing:** Reads directory names from a wordlist file, stripping unnecessary whitespace and ignoring blank lines.
- **HTTP Requests:** Sends HTTP GET requests to each potential directory.
- **Live Output:** Prints URLs with interesting HTTP status codes (200, 301, 302, 403, 401) as they are discovered.
- **Turkish Localization in Code:** All output messages and code comments are written in Turkish.

## Requirements

- **Python 3.x**
- **Requests Library**  
  Install it using:
  ```bash
  pip install requests

## Usage
Run the script from the terminal with the following command:
 ```bash
python3 dirfind.py -h website.com -w wordlist.txt 
```
-h flag specifies the target website (e.g., website.com).
-w flag provides the path to the directory wordlist file (e.g., wordlist.txt).

## Example
If you have a file named wordlist.txt and you want to scan example.com, run:
 ```bash
python3 dirfind.py -h example.com -w wordlist.txt
```
During the scan, discovered directories with their HTTP status codes will be displayed in the terminal.

## Contributing
If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request in this repository.
