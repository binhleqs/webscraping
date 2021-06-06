from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)

except URLError as e:
    print("The sever could not be found!")
else:
    print("It Worked!")

bs = BeautifulSoup(html.read(),'html.parser')

try:
    badContent = bs.find("nonExisting").anotherTag
except AttributeError as e :
    print("Tag was not found")
else:
    if badContent == None:
        print("Tag was nor found")
    else:
        print(badContent)


