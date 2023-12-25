import time
import re
import requests
from bs4 import BeautifulSoup

def logo():
    time.sleep(1)
    print(" _____          _   _ ")
    print("|_   _|_ _ _ __| | | | _____  __")
    print("  | |/ _` | '__| |_| |/ _ \ \/ /")
    print("  | | (_| | |  |  _  |  __/>  < Version: 1.00") 
    print("  |_|\__,_|_|  |_| |_|\___/_/\_\n")

def wurl():
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
    user_input = input("Enter the URL or command: ")
   
    if user_input.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'
    elif user_input.lower() == "/links":
        with open('links.txt', 'r') as file:
            content = file.read()  # Fixed typo here
            print(content)
    elif user_input.lower() == "/deletelinks":
        with open('links.txt', 'w') as file:
            file.write("")
        print("Links deleted successfully")  # Added print statement
    elif user_input.lower() == "/webscrape":
        wurl()
    elif user_input.lower() == "/help":
        print("• Press 'exit' to exit the program.")
        print("• You must be connected to the network.")
        print("• Press /links to read saved links.")
        print("• Press /webscrape for Scraping Websites")
    else:
        try:
            # Send an HTTP GET request
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
                       
                    print("Links Saved")
                    counter += 1
            else:
                print("No 'link' values found in the JavaScript code on the provided URL")
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
