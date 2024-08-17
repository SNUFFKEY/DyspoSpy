from main import operation
import requests
import json


def ip_lookup(format,fileNameParam):
    unfiltered_ip = input("IP Address :")
    usrfilename = input("Name of file ? : ")


    ip = unfiltered_ip.strip()

    url = f"http://ip-api.com/json/{ip}"
    req = requests.get(url)
    results = req.text
    
    results_dict = json.loads(results)
    
    if req.status_code == 200:
        try:
            details = f"""
[+] IP Addres: {results_dict['query']}
[+] Country: {results_dict['country']}
[+] Region: {results_dict['city']}
[+] City: {results_dict['city']}
[+] Zip Code: {results_dict['zip']}
[+] Timezone: {results_dict['timezone']}
[+] ISP: {results_dict['isp']}
[+] Longitude: {results_dict['lon']}
[+] Latitude: {results_dict['lat']}
"""
            print(details)
        except:
            print("Cannot Lookup IP")

            
        with open(f"{fileNameParam}.{file}",'w') as file:
            try:
                file.write(details)
            except:
                print("Unable Find Information On The IP Provided")