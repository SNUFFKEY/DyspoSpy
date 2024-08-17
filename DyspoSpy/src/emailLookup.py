import webbrowser
import requests
from main import operation


def email_lookup(format,fileNameParam):
    
    email_name = input("Enter Email : ")
    
    
    if "@" in email_name:
        filtered_email = email_name.replace("@","%40")

    google_dork = f"https://www.google.com/search?q=%22{filtered_email}%22"
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

    epios_link = f"https://epieos.com/?q={filtered_email}.com&t=email"
    
    webbrowser.open(google_dork)
    webbrowser.open(epios_link)


    with open(f"{fileNameParam}.{format}") as emailFile:
        emailFile.write("")