import requests
import json
from colorama import Fore, Style, init
import os
from bs4 import BeautifulSoup
import re

init()

os.system("cls")
print(f"""{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}
    
 ██████╗ ██╗    ██╗███╗   ██╗███████╗██████╗ 
 ██╔══██╗██║    ██║████╗  ██║██╔════╝██╔══██╗
 ██████╔╝██║ █╗ ██║██╔██╗ ██║█████╗  ██████╔╝
 ██╔═══╝ ██║███╗██║██║╚██╗██║██╔══╝  ██╔══██╗
 ██║     ╚███╔███╔╝██║ ╚████║███████╗██║  ██║
 ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
 Developed by Papi#3534                      """)

def email_leaks():
    session = requests.session()
    url = "http://pwndb2am4tzkvold.onion.ws/"
    email = input(f"\n{Fore.WHITE}> {Fore.LIGHTMAGENTA_EX}Email{Fore.WHITE}: ")
    if "@" in email:
        luser = email.split("@")[0]
        domain = email.split("@")[1]
        
        data = {"luser": luser, "domain": domain, "luseropr": 0, "domainopr": 0, "submitform": "em"}
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61"}
        response = session.post(url, headers=headers, data=data).text
        
        soup = BeautifulSoup(response, "html.parser")
        
        lines = response.split("\n")
        count = 0
        passwords = []
        for x in lines:
            count += 1
            try:
                passwords.append(re.search("\[password\] => (.*)", x).group(1))
            except:
                pass
        new = passwords[1:]
        
        if len(passwords) < 2:
            print(f"\n{Fore.WHITE}> {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}No results found.")
            print(f"\n{Fore.WHITE}> {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Finished{Fore.WHITE}...")
        else:
            print("")
            for pwd in new:
                print(f"{Fore.WHITE}> {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{email}{Fore.WHITE}:{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{pwd}")
                
            print(f"\n{Fore.WHITE}> {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Finished{Fore.WHITE}...")
        
    else:
        print(f"\n {Fore.WHITE}[{Fore.LIGHTRED_EX}{Style.BRIGHT}ERROR{Fore.WHITE}] {Fore.LIGHTRED_EX}{Style.BRIGHT}Enter a valid e-mail.")

while True:
    email_leaks()