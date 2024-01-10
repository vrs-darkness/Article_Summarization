import requests

from bs4 import BeautifulSoup


URL = input() # Give the input URL as input

pages = requests.get(URL)
soup = BeautifulSoup(pages.content,"html.parser")

content = soup.find(class_ = "gk gl gm gn go")

with open("Text.txt","w") as f:
    for i in content.find_all("p"):
        f.write(i.text)
        f.write("\n");

print("DONE!!")