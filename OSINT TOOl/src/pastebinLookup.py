import webbrowser


def pasteBinSearch():


  doxbin = f"https://doxbin.com/"
  pastebin = f"https://pastebin.com/"
  ivpaste = f"https://ivpaste.com/"
  pastedebian = f"https://paste.debian.net/"
  jsbin = f"https://Jsbin.com"
  pasteCentos =  f"https://paste.centos.org/"
  pasteEe = f"https://Paste.ee/"
  pastekde = f"https://Paste.kde.org"
  Rentry = f"https://rentry.co/"
  Obin = f"https://0bin.net"


  pastebinLinks = [
    doxbin, pastebin, ivpaste,jsbin, pastedebian, pasteCentos,Rentry,Obin,pastekde
  ]


  for link in pastebinLinks:

    webbrowser.open(f"{link}")
  
  # Search doxbin,pastebin,ivpaste etc
