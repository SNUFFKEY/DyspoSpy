import webbrowser
from main import operation, fileType


def name_lookup(format,fileNameParam):

    firstname = input("Firstname: ").strip()
    middlename = input("Middlename: ").strip()
    lastname = input("Lastname: ").strip()
    usrstate = input("State: ").lower().strip()  # Convert to lowercase and strip spaces
    city = input("City: ").strip()
    prompt = input("Are You Ready? (Y/N): ").strip()
    
    abbreviations = {
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY"
}

    if prompt.upper() == "Y":
        if usrstate.lower() in abbreviations:
            state_abbr = abbreviations[usrstate]
            link = f"https://www.smartbackgroundchecks.com/people/{firstname}-{middlename}-{lastname}/{city}/{state_abbr}"
            webbrowser.open(link)
        else:
            print("Invalid State")


    with open(f"{fileNameParam}.{format}","w") as nameInfoFile:
        nameInfoFile.write("REQUEST")
