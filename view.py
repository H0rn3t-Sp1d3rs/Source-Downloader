import requests,os
from bs4 import BeautifulSoup

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
    
banner = """\033[31m

			 _____  ___ ______  _____                                 
			| ___ \/ _ \|  _  \/  ___|                                
			| |_/ / /_\ \ | | |\ `--.                                 
			| ___ \  _  | | | | `--. \                                
			| |_/ / | | | |/ / /\__/ /                                
			\____/\_| |_/___/  \____/                                                                                                                                                     
 	 _____ ________  ______  ____   _ _   _ _____ _______   __
 	/  __ \  _  |  \/  ||  \/  | | | | \ | |_   _|_   _\ \ / /
 	| /  \/ | | | .  . || .  . | | | |  \| | | |   | |  \ V / 
 	| |   | | | | |\/| || |\/| | | | | . ` | | |   | |   \ /  
 	| \__/\ \_/ / |  | || |  | | |_| | |\  |_| |_  | |   | |  
 	 \____/\___/\_|  |_/\_|  |_/\___/\_| \_/\___/  \_/   \_/  
                                                                                                                    
\n"""
                 
                 
print(banner)
print("\033[33m	   	   Source Code Downloader")
print("\033[33m	   	   Code By : @h0rn3t_sp1d3r")
print("\033[32m	   	   Telegram Channel  : @BADS_COMMUNITY\n")

try:
    url = input (' Enter Url : ')
except FileNotFoundError:
    print("[!] URL Not Found ")
    exit()

response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    with open('web_source.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    print(f" Source has been saved to 'web_source.html'")
else:
    print("Failed to Save web page.")
