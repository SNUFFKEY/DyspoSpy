

import requests
from colorama import Fore, Style
from main import links
from main import operation,fileType


nono_chars = ['/' , '[',']','{',"}","|","\\",")","(","*","%","+","=",":",","]


def username_lookup(format,fileNameParam,usernameToLookup=none):
    
    # username = input("Enter Username : ")

    if usernameToLookup != none:
        
    
        for chars in nono_chars:
            while chars in username:
                print(f"Please Dont use {chars}")
                username = input("Enter Username : ")

        nameoffile = input("Enter File To Output To : ")
        print('\n')
        num = 0 

        webbrowser.open(f"https://www.idcrawl.com/u/{username}")
        webbrowser.open(f"https://knowem.com/checkusernames.php?u={username}")
        webbrowser.open(f"https://checkusernames.com/?username={username}")

        # with open(f"{fileNameParam}.{format}","a") as filers:
        #     filers.write(f"<a href=\"https://www.idcrawl.com/u/{username}\" target=\"_blank\"> IDCrawl </a>\n")
        #     filers.write(f"<a href=\"https://knowem.com/checkusernames.php?u={username}\" target=\"_blank\"> Knowem </a>\n")
        #     filers.write(f"<a href=\"https://checkusernames.com/?username={username}\"  target=\"blank\"> CheckUserNames </a>\n")
        

        with open("$HOME/Downloads/DyspoSpy/data/links.txt","a") as linkFile:

            readLinkFile = linkFile.readline()
            for line in readLinkFile:
                print(line) 
                if "{}" in line:
                    line.replace("{}",)
            
            
            
            
                for key , values in links.items():
            links_with_username = values.format(username)
            req = requests.get(links_with_username)
            if req.status_code == 200:

                if format == "pdf" or "txt":
                    with open(f"{fileNameParam}.{format}","a") as fikle:
                        fikle.write(f"{links_with_username}\n")
                if format == "html":
                    extension = "html"
                    with open(f"{nameoffile}.{format}","a") as fikle:
                        fikle.write(f"<a href=\"{links_with_username}\" target=\"_blank\"> {key} </a>\n")



                    
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} User has an account on {key}")
                
            elif req.status_code != 200:
                print(f"{Fore.RED}[-]{Style.RESET_ALL} User does not have an account on {key}")


    else:
        print("Please Enter Valid Username !")        


