import os
import platform
import requests as req
import time
import re
import requests
from bs4 import BeautifulSoup

def logo():
        print(" _____          _   _ ")
        print("|_   _|_ _ _ __| | | | _____  __")
        print("  | |/ _` | '__| |_| |/ _ \ \/ /")
        print("  | | (_| | |  |  _  |  __/>  < Version: 1.00") 
        print("  |_|\__,_|_|  |_| |_|\___/_/\_\n")


def web_scrape():
        print("This Command Can't Clone Protected Sites TSL/SSL encryption")
        tim.sleep(1)
        weurl = input("Enter Web Scrape Link: ")
        response = requests.get(weurl)
        x = response.text
        print(" S = SAVE ")
        print(" P = DISPLAY OUTPUT ")
        wurld = input("Enter Your Choice: ")
        if wurld == "S":
            ftype = input("Enter File Name: ")
            with open(f'{ftype}', 'w') as file:
                file.write(x)
                print("Success")
        elif wurld == "P":
            print(x)
        else:
            print("No Option Chosen")
        
import requests
import re

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

def track_ip():
    def get_public_ip():
        return req.get("https://api.ipify.org").text

    def get_details(ip):
        response = req.get(f"https://ipinfo.io/{ip}/json")
        return response.json() if response.status_code == 200 else None

    def print_details(ip_info):
        if ip_info:
            print(f" [>] IP Address: {ip_info.get('ip')}")
            print(f" [>] Hostname: {ip_info.get('hostname', 'N/A')}")
            print(f" [>] City: {ip_info.get('city', 'N/A')}")
            print(f" [>] Region: {ip_info.get('region', 'N/A')}")
            print(f" [>] Country: {ip_info.get('country', 'N/A')}")
            print(f" [>] Location: {ip_info.get('loc', 'N/A')}")
            print(f" [>] Organization: {ip_info.get('org', 'N/A')}")
        else:
            input(" ENTER TO EXIT ")

    def run():
        while True:
            print("[1] CHECK OWN IP\n[2] CHECK OTHERS IP\n[0] EXIT")
            choice = input(" CHOOSE : ")

            if choice == '1':
                target_ip = get_public_ip()
            elif choice == '2':
                target_ip = input(" ENTER IP ADDRESS : ")
                continue
            elif choice == '0':
                break
            else:
                print(" NO OPTION FOUND")
                continue

            ip_details = get_details(target_ip)
            print_details(ip_details)

    run()

def main():
    while True:
        logo()
        print("[1] WebClone\n[2] IP Tracking\n[3]Link Extract (phills only)\n[0] EXIT")
        choice = input(" CHOOSE OPTION : ")

        if choice == '1':
            web_scrape()
        elif choice == '3':
        	link_fetch()
        elif choice == '2':
            track_ip()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select from the given options.")

if __name__ == "__main__":
    main()
