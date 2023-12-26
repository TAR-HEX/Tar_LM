import os
import platform
import requests as req
import time
import re
import requests
from bs4 import BeautifulSoup

blue = "\033[1;34m"
green = "\033[1;32m"
cyan = "\033[1;36m"
purple = "\033[1;35m"
white = "\033[1;37m"
reset = "\033[0m"
yellow = "\033[1;33m"
red = "\033[1;31m"

def logo():
        time.sleep(0.5)
        print(f"{red}_____          _   _ ")
        print(f"|_   _|_ _ _ __| | | | _____  __")
        print(f"  | |/ _` | '__| |_| |/ _ \ \/ /")
        print(f"  | | (_| | |  |  _  |  __/>  <{yellow} Version: 1.00{red}")
        print(f"  |_|\__,_|_|  |_| |_|\___/_/\_\n{reset}")


def web_scrape():
        weurl = input("Enter Web Scrape Link: ")
        response = requests.get(weurl)
        x = response.text
        wurld = input("Enter Your Choice: ")
        if wurld == "/save":
            ftype = input("Enter File Name: ")
            with open(f'{ftype}', 'w') as file:
                file.write(x)
                print("Success")
        elif wurld == "/print":
            print(x)
        else:
            print("No Option Chosen")
        

def link_fetch():
    user_input = input("Enter URL: ")
    try:
        response = requests.get(user_input)
        response.raise_for_status()  # Check for any request errors
        # Extract the HTML content from the response
        html_content = response.text
        # Define a regex pattern to match the "link" values
        pattern = r"link:\s+'(https://[^']+)'"
        # Use re.findall to find all the link values in the JavaScript code
        link_values = re.findall(pattern, html_content)

        if link_values:
            print(link_values)
            with open('links.txt', 'a') as file:
                name = input("Enter The Name: ")
                counter = 1
                s = ": "
                for link_value in link_values:
                    file.write(f"{counter}>{name}{s}{link_value}\n")
                    counter += 1
                print("Links Saved")
        else:
            print("No 'link' values found in the JavaScript code on the provided URL")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    while True:
        time.sleep(1)
        logo()
        time.sleep(1)
        print("Press '/help' for help or 'exit' to exit.")
        user_input = input("Enter the command: ")

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == "/webscrape":
            save_or_print()
        elif user_input.lower() == "/help":
            print("Press 'exit' to exit the program.")
            print("You must be connected to the network.")
            print("Press /webscrape for Scraping Websites")
        else:
            print("Invalid command. Type '/help' for instructions.")

def url_shortner():
    try:
        user_link = input(f"{yellow}Enter The Url :- {reset}")
        urls = f"https://is.gd/create.php?format=simple&url={user_link}"
        user_response = requests.get(urls)
        shorturl = user_response.text
        print(f"{red}=>{reset} {blue}{shorturl}{reset}")
    except requests.ConnectionError:
        print(f"{red}ERROR{reset}")
        time.sleep(0.5)
        print(f"{yellow}Make Sure Your{reset} {red}Internet{reset} {yellow}Is Enabled!{reset}")

def track_ip():
    def get_public_ip():
        return req.get("https://api.ipify.org").text

    def get_details(ip):
        response = req.get(f"https://ipinfo.io/{ip}/json")
        return response.json() if response.status_code == 200 else None

    def print_details(ip_info):
        if ip_info:
            print(f" {red}[>]{reset} {yellow}IP Address:{reset} {ip_info.get('ip')}")
            print(f" {red}[>]{reset} {yellow}Hostname:{reset} {ip_info.get('hostname', 'N/A')}")
            print(f" {red}[>]{reset} {yellow}City:{reset} {ip_info.get('city', 'N/A')}")
            print(f" {red}[>]{reset} {yellow}Region:{reset} {ip_info.get('region', 'N/A')}")
            print(f" {red}[>]{reset} {yellow}Country:{reset} {ip_info.get('country', 'N/A')}")
            print(f" {red}[>]{reset} {yellow}Location:{reset} {ip_info.get('loc', 'N/A')}")
            print(f" {red}[>]{reset} {yellow}Organization:{reset} {ip_info.get('org', 'N/A')}")
        else:
            input(f"{red} ENTER TO EXIT {reset}")

    def run():
        while True:
            logo()
            print(f"{red}[1]{reset} {yellow}CHECK OWN IP{reset}\n{red}[2]{reset} {yellow}CHECK OTHERS IP{reset}\n{red}[0]{reset} {green}EXIT{reset}")
            choice = input(f"{red}CHOOSE : {reset} ")

            if choice == '1':
                target_ip = get_public_ip()
                ip_details = get_details(target_ip)
                print_details(ip_details)
            elif choice == '2':
                target_ip = input(f"{red}ENTER IP ADDRESS : {reset}")
                if target_ip:
                    ip_details = get_details(target_ip)
                    print_details(ip_details)
                else:
                    print("No IP address provided.")
            elif choice == '0':
                break
            else:
                print(" NO OPTION FOUND")
                continue

    run()

def main():
    while True:
        logo()
        print(f"{red}[1]{reset}{yellow}WebClone{reset}\n{red}[2]{reset}{yellow} IP Tracking{reset}\n{red}[3]{reset}{yellow}Fetch Url{reset}\n{red}[4]{reset}{yellow}Mask Url{reset}\n{cyan}[0]{reset}{green}EXIT{reset}")
        choice = input(f"{red} CHOOSE OPTION : {reset}")

        if choice == '1':
            web_scrape()
        elif choice == '3':
            link_fetch()
        elif choice == '2':
            track_ip()
        elif choice == '4':
        	url_shortner()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select from the given options.")

if __name__ == "__main__":
    main()