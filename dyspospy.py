import phonenumbers
from phonenumbers import geocoder, carrier
import requests
import json
import selenium
import webbrowser

from colorama import Fore, Style

# from src.help import help


logo = """


 ______   __   __  _______  _______  _______  _______  _______  __   __ 
|      | |  | |  ||       ||       ||       ||       ||       ||  | |  |
|  _    ||  |_|  ||  _____||    _  ||   _   ||  _____||    _  ||  |_|  |
| | |   ||       || |_____ |   |_| ||  | |  || |_____ |   |_| ||       |
| |_|   ||_     _||_____  ||    ___||  |_|  ||_____  ||    ___||_     _|
|       |  |   |   _____| ||   |    |       | _____| ||   |      |   |  
|______|   |___|  |_______||___|    |_______||_______||___|      |___|  


-h for help !

Phone Number Lookup , IP Lookup and more !

"""

print(logo)

nono_chars = ['/' , '[',']','{',"}","|","\\",")","(","*","%","+","=",":",","]

links = {
    "2Dimensions": "https://2Dimensions.com/a/{}",
    "7Cups": "https://www.7cups.com/@{}",
    "9GAG": "https://www.9gag.com/u/{}",
    "About.me": "https://about.me/{}",
    "Academia.edu": "https://independent.academia.edu/{}",
    "Alik.cz": "https://www.alik.cz/u/{}",
    "Apple Discussions": "https://discussions.apple.com/profile/{}",
    "Asciinema": "https://asciinema.org/~{}",
    "Ask Fedora": "https://ask.fedoraproject.org/u/{}",
    "AskFM": "https://ask.fm/{}",
    "Audiojungle": "https://audiojungle.net/user/{}",
    "BLIP.fm": "https://blip.fm/{}",
    "Bandcamp": "https://www.bandcamp.com/{}",
    "Bazar.cz": "https://www.bazar.cz/{}/",
    "Behance": "https://www.behance.net/{}",
    "BitBucket": "https://bitbucket.org/{}/",
    "Blogger": "https://{}.blogspot.com",
    "Bookcrossing": "https://www.bookcrossing.com/mybookshelf/{}/",
    "BuyMeACoffee": "https://buymeacoff.ee/{}",
    "BuzzFeed": "https://buzzfeed.com/{}",
    "CNET": "https://www.cnet.com/profiles/{}/",
    "Carbonmade": "https://{}.carbonmade.com",
    "Career.habr": "https://career.habr.com/{}",
    "Championat": "https://www.championat.com/user/{}",
    "Chatujme.cz": "https://profil.chatujme.cz/{}",
    "Chess": "https://www.chess.com/member/{}",
    "CloudflareCommunity": "https://community.cloudflare.com/u/{}",
    "Codecademy": "https://www.codecademy.com/profiles/{}",
    "Codepen": "https://codepen.io/{}",
    "Codewars": "https://www.codewars.com/users/{}",
    "ColourLovers": "https://www.colourlovers.com/lover/{}",
    "Contently": "https://{}.contently.com/",
    "Coroflot": "https://www.coroflot.com/{}",
    "Crevado": "https://{}.crevado.com",
    "DEV Community": "https://dev.to/{}",
    "DailyMotion": "https://www.dailymotion.com/{}",
    "Designspiration": "https://www.designspiration.net/{}/",
    "DeviantART": "https://{}.deviantart.com",
    "Discogs": "https://www.discogs.com/user/{}",
    "Discuss.Elastic.co": "https://discuss.elastic.co/u/{}",
    "Disqus": "https://disqus.com/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Ello": "https://ello.co/{}",
    "Etsy": "https://www.etsy.com/shop/{}",
    "EyeEm": "https://www.eyeem.com/u/{}",
    "F3.cool": "https://f3.cool/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "Facebook Groups": "https://www.facebook.com/groups/{}",
    "Fandom": "https://www.fandom.com/u/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Flipboard": "https://flipboard.com/@{}",
    "Football": "https://www.rusfootball.info/user/{}/",
    "FortniteTracker": "https://fortnitetracker.com/profile/all/{}",
    "Freelance.habr": "https://freelance.habr.com/freelancers/{}",
    "Freelancer.com": "https://www.freelancer.com/u/{}",
    "Freesound": "https://freesound.org/people/{}/",
    "Gamespot": "https://www.gamespot.com/profile/{}/",
    "GetMyUni": "https://www.getmyuni.com/user/{}",
    "Giphy": "https://giphy.com/{}",
    "GitHub": "https://www.github.com/{}",
    "GitHub Support Community": "https://github.community/u/{}/summary",
    "GitLab": "https://gitlab.com/{}",
    "Gitee": "https://gitee.com/{}",
    "GoodReads": "https://www.goodreads.com/{}",
    "Gravatar": "http://en.gravatar.com/{}",
    "Gumroad": "https://www.gumroad.com/{}",
    "GunsAndAmmo": "https://forums.gunsandammo.com/profile/{}",
    "GuruShots": "https://gurushots.com/{}/photos",
    "HackTheBox": "https://forum.hackthebox.eu/profile/{}",
    "Hackaday": "https://hackaday.io/{}",
    "HackerOne": "https://hackerone.com/{}",
    "Houzz": "https://houzz.com/user/{}",
    "HubPages": "https://hubpages.com/@{}",
    "ICQ": "https://icq.im/{}",
    "IFTTT": "https://www.ifttt.com/p/{}",
    "ImgUp.cz": "https://imgup.cz/{}",
    "Instagram": "https://instagram.com/{}",
    "Instructables": "https://www.instructables.com/member/{}",
    "Issuu": "https://issuu.com/{}",
    "Itch.io": "https://{}.itch.io/",
    "Jimdo": "https://{}.jimdosite.com",
    "Kaggle": "https://www.kaggle.com/{}",
    "Keybase": "https://keybase.io/{}",
    "Kik": "https://kik.me/{}",
    "Kongregate": "https://www.kongregate.com/accounts/{}",
    "LOR": "https://www.linux.org.ru/people/{}/profile",
    "Launchpad": "https://launchpad.net/~{}",
    "LeetCode": "https://leetcode.com/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Lichess": "https://lichess.org/@/{}",
    "Likee": "https://likee.com/@{}",
    "LiveJournal": "https://{}.livejournal.com",
    "Lobsters": "https://lobste.rs/u/{}",
    "Medium": "https://medium.com/@{}",
    "Memrise": "https://www.memrise.com/user/{}/",
    "Munzee": "https://www.munzee.com/m/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "MyMiniFactory": "https://www.myminifactory.com/users/{}",
    "Myspace": "https://myspace.com/{}",
    "NameMC (Minecraft.net skins)": "https://namemc.com/profile/{}",
    "Naver": "https://blog.naver.com/{}",
    "Newgrounds": "https://{}.newgrounds.com",
    "NotABug.org": "https://notabug.org/{}",
    "OK": "https://ok.ru/{}",
    "OpenStreetMap": "https://www.openstreetmap.org/user/{}",
    "Opensource": "https://opensource.com/users/{}",
    "PCPartPicker": "https://pcpartpicker.com/user/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Periscope": "https://www.periscope.tv/{}/",
    "Pinkbike": "https://www.pinkbike.com/u/{}/",
    "PlayStore": "https://play.google.com/store/apps/developer?id={}",
    "Plug.DJ": "https://plug.dj/@/{}",
    "Pokémon Showdown": "https://pokemonshowdown.com/users/{}",
    "Polygon": "https://www.polygon.com/users/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "PromoDJ": "http://promodj.com/{}",
    "PyPi": "https://pypi.org/user/{}",
    "Quizlet": "https://quizlet.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Raidforums": "https://raidforums.com/User-{}",
    "Rajce.net": "https://{}.rajce.idnes.cz/",
    "RapidAPI": "https://rapidapi.com/users/{}",
    "Rate Your Music": "https://rateyourmusic.com/~{}",
    "Redbubble": "https://www.redbubble.com/people/{}",
    "Repl.it": "https://repl.it/@{}",
    "ResearchGate": "https://www.researchgate.net/profile/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "RubyGems": "https://rubygems.org/profiles/{}",
    "Sbazar.cz": "https://www.sbazar.cz/{}",
    "Scratch": "https://scratch.mit.edu/users/{}",
    "Scribd": "https://www.scribd.com/{}",
    "ShitpostBot5000": "https://www.shitpostbot.com/user/{}",
    "Signal": "https://community.signalusers.org/u/{}",
    "Slack": "https://{}.slack.com",
    "Slashdot": "https://slashdot.org/~{}",
    "SlideShare": "https://slideshare.net/{}",
    "Snapchat": "https://snapchat.com/add/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "SourceForge": "https://sourceforge.net/u/{}",
    "Speedrun.com": "https://speedrun.com/user/{}",
    "Splits.io": "https://splits.io/users/{}",
    "Sporcle": "https://www.sporcle.com/user/{}/people",
    "SportsRU": "https://www.sports.ru/profile/{}/",
    "Spotify": "https://open.spotify.com/user/{}",
    "Star Citizen": "https://robertsspaceindustries.com/citizens/{}",
    "SublimeForum": "https://forum.sublimetext.com/u/{}",
    "Tellonym.me": "https://tellonym.me/{}",
    "Test PyPi": "https://test.pypi.org/user/{}",
    "Twitter" : "https://twitter.com/{}",
    "TikTok": "https://tiktok.com/@{}",
    "Ultimate-Guitar": "https://ultimate-guitar.com/u/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "VK": "https://vk.com/{}",
    "VSCO": "https://vsco.co/{}",
    "Venmo": "https://venmo.com/{}",
    "Vero": "https://vero.co/{}",
    "Vimeo": "https://vimeo.com/{}",
    "VirusTotal": "https://www.virustotal.com/ui/users/{}/trusted_users",
    "Warrior Forum": "https://www.warriorforum.com/members/{}.html",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "We Heart It": "https://weheartit.com/{}",
    "WebNode": "https://{}.webnode.cz/",
    "Whonix Forum": "https://forums.whonix.org/u/{}",
    "Wikipedia": "https://www.wikipedia.org/wiki/User:{}",
    "Windy": "https://community.windy.com/user/{}",
    "Wix": "https://{}.wix.com",
    "WordPressOrg": "https://profiles.wordpress.org/{}/",
    "Xbox Gamertag": "https://xboxgamertag.com/search/{}",
    "YouPic": "https://youpic.com/photographer/{}/",
    "YouTube": "https://www.youtube.com/{}",
    "Zhihu": "https://www.zhihu.com/people/{}",
    "Akniga": "https://akniga.org/profile/{}",
    "AllMyLinks": "https://allmylinks.com/{}",
    "AminoApp": "https://aminoapps.com/u/{}",
    "authorSTREAM": "http://www.authorstream.com/{}/",
    "babyRU": "https://www.baby.ru/u/{}/",
    "chaos.social": "https://chaos.social/@{}",
    "CouchSurfing": "https://www.couchsurfing.com/people/{}",
    "d3RU": "https://d3.ru/user/{}/posts",
    "Dailykos": "https://www.dailykos.com/user/{}",
    "datingRU": "http://dating.ru/{}",
    "Drive2": "https://www.drive2.ru/users/{}",
    "eGPU": "https://egpu.io/forums/profile/{}/",
    "Eintracht": "https://community.eintracht.de/fans/{}",
    "Fixya": "https://www.fixya.com/users/{}",
    "FL": "https://www.fl.ru/users/{}",
    "GeoCaching": "https://www.geocaching.com/p/default.aspx?u={}",
    "Habr": "https://habr.com/ru/users/{}",
    "Hackster": "https://www.hackster.io/{}",
    "irecommend": "https://irecommend.ru/users/{}",
    "Jeuxvideo": "http://www.jeuxvideo.com/profil/{}?mode=infos",
    "Kofi": "https://ko-fi.com/{}",
    "kwork": "https://kwork.ru/user/{}",
    "Last.fm": "https://last.fm/user/{}",
    "LeaseHackr": "https://forum.leasehackr.com/u/{}/summary/",
    "LiveLib": "https://www.livelib.ru/reader/{}",
    "mastodon.cloud": "https://mastodon.cloud/@{}",
    "mastodon.social": "https://mastodon.social/@{}",
    "Mercadolivre": "https://www.mercadolivre.com.br/perfil/{}",
    "Moikrug": "https://moikrug.ru/{}",
    "Mstdn.io": "https://mstdn.io/@{}",
    "Nairaland.com": "https://www.nairaland.com/{}",
    "nnRU": "https://{}.www.nn.ru/",
    "Note": "https://note.com/{}",
    "npm": "https://www.npmjs.com/~{}",
    "Opennet": "https://www.opennet.ru/~{}",
    "Osu!": "https://osu.ppy.sh/users/{}",
    "Pinterest" : "https://pinterest.com/{}",
    "satsisRU": "https://satsis.info/user/{}",
    "social.tchncs.de": "https://social.tchncs.de/@{}",
    "Svidbook": "https://www.svidbook.ru/user/{}",
    "uid": "http://uid.me/{}"
    
}

def helpf():
    helpmsg = """

[1] IP Lookup
[2] Number Lookup
[3] Username Lookup
[4] Email Lookup
[5] Name Lookup
[6] Help

Enter the number of the feature you want to use
"""
    print(helpmsg)
    
def email_lookup():
    
    email_name = input("Enter Email : ")
    
    
    if "@" in email_name:
        filtered_email = email_name.replace("@","%40")

    google_dork = f"https://www.google.com/search?q=%22{filtered_email}%22"
    epios_link = f"https://epieos.com/?q={filtered_email}.com&t=email"
    
    webbrowser.open(google_dork)
    webbrowser.open(epios_link)
    
def name_lookup():

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

def username_lookup():
    
    username = input("Enter Username : ")
    
    for chars in nono_chars:
        while chars in username:
            print(f"Please Dont use {chars}")
            username = input("Enter Username : ")

    nameoffile = input("Enter File To Output To : ")
    print('\n')
    num = 0 
    with open(f"{nameoffile}.html","a") as filers:
        filers.write(f"<a href=\"https://www.idcrawl.com/u/{username}\" target=\"_blank\"> IDCrawl </a>\n")
        filers.write(f"<a href=\"https://knowem.com/checkusernames.php?u={username}\" target=\"_blank\"> Knowem </a>\n")
        filers.write(f"<a href=\"https://checkusernames.com/?username={username}\"  target=\"blank\"> CheckUserNames </a>\n")
    for key , values in links.items():
        links_with_username = values.format(username)
        req = requests.get(links_with_username)
        if req.status_code == 200:
            with open(f"{nameoffile}.html","a") as fikle:
                fikle.write(f"<a href=\"{links_with_username}\" target=\"_blank\"> {key} </a>\n")

                
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} User has an account on {key}")
            
        elif req.status_code != 200:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} User does not have an account on {key}")
            

                

def ip_lookup():
    unfiltered_ip = input("IP Address :")
    output_to_file = input("Output To A File (Y/N) : ")
    
    if output_to_file.upper() == "Y":
        usrfilename = input("Name of file ? : ")
        with open(f"{usrfilename}.txt",'w') as file:
            file.write(details)
            pass

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

def num_lookup():
    
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

while True:
    def_input = input("$: ")
    
    if def_input == "1":
        ip_lookup()
        
    if def_input == "2":
        num_lookup()
    if def_input == "3":
        username_lookup()
        pass
    if def_input == "4":
        email_lookup()   
        pass
    if def_input == "5":
        name_lookup()
        pass
    
    if def_input == "6":
        helpf()
    
    if def_input == "-h":
        helpf()
    
    