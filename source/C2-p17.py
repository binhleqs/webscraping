from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')

nameList = bs.findAll('span', {'class':'green'})
#print(nameList)
for name in nameList:
    print(name.get_text())

tags = bs.find_all('span', {'class':'red'})

for tag in tags:
    print(tag.get_text())


namenum = bs.find_all(text="the prince")
print(len(namenum))

greenfind= bs.find_all(class_ = 'green')
print(greenfind)
