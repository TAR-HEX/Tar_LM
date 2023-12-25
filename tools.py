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
    def save_or_print():
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
    def clear_screen():
        os.system("cls" if platform.system() == "Windows" else "clear")

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
        print("[1] LinkExtracting (phills only)\n[2] IP Tracking\n[0] EXIT")
        choice = input(" CHOOSE OPTION : ")

        if choice == '1':
            web_scrape()
        elif choice == '2':
            track_ip()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select from the given options.")

if __name__ == "__main__":
    main()