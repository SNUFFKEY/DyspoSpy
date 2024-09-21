import webbrowser
import requests
import subprocess
from main import operation


def email_lookup(format,fileNameParam):
    
    email_name = input("Enter Email : ")
    
    
    if "@" in email_name:
        email_name = email_name.replace("@","%40")
    elif "@" not in email_name:
        pass

    google_dork = f"https://www.google.com/search?q=%22{email_name}%22"
    googleDorkRespone = requests.get(google_dork)




    if googleDorkRespone.status_code == 200:
        if format == "--html":

            with open("googleRespone.txt", "w") as responeFile:
                responseFileWrite = responeFile.write(googleDorkRespone.text)

        if format == "--txt":
            with open("googleRespone.txt", "w") as responeFile:
                responseFileWrite = responeFile.write(googleDorkRespone.text)

        if format == "--pdf":
            with open("googleRespone.pdf", "w") as responeFile:
                responseFileWrite = responeFile.write(googleDorkRespone.text)


    else:
         print(f"Error fetching Google search. Status code: {googleDorkRespone.status_code}")

    webbrowser.open(google_dork)


    def epiosSearch():
        epios_link = f"https://epieos.com/?q={email_name}.com&t=email"
        webbrowser.open(epios_link)
    
    epiosSearch()


    def thatsthemSearch(email_name):

        email = email_name.replace("%40","@")
        thatsthemLink = f"https://thatsthem.com/email/{email}"
        webbrowser.open(thatsthemLink)

    thatsthemSearch(email_name)




    def holeheSearch(email):
        
        subprocess.run["holehe","-u + " + email]
        pass

    holeheSearch(email_name)


    with open(f"{fileNameParam}.{format}") as emailFile:
        emailFile.write("")

    def HIBPsearch(email):
        pass
