
from main import phonenumbers, geocoder
from main import operation, fileType

def num_lookup(format,fileNameParam):
    
    number = input("Phone Number :")
    phoneNumber = phonenumbers.parse(number)
    timezone = timezone.time_zones_for_number(phoneNumber)
    carrier = carrier.name_for_number(phoneNumber, 'en')
    region = geocoder.description_for_number(phoneNumber,'en')
    valid = phonenumbers.is_valid_number(phoneNumber)
    
    
    if valid == True:
        print(f"[+] Number is valid")
        print(f"Number : {phoneNumber}")
        print(f"Timezone : {timezone}")
        print(f"Carrier : {carrier}")
        print(f"Region : {region}")
    elif valid != True:
        print(f"[-] Number is not valid ")



    with open(f"{fileNameParam}.{format}") as numberInfoFile:
        numberInfoFile.write()