import requests

from bs4 import BeautifulSoup




def Extract(URL):
    pages = requests.get(URL)
    soup = BeautifulSoup(pages.text,"lxml")

    # content = soup.find( id = "root")
    with open("Text.txt","w") as f:
        for i in soup.find_all("p"):
            f.write(i.text)
            f.write("\n")
