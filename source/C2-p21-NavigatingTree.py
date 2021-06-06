from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'html.parser')

#for child in bs.find('table', {'id':'giftList'}).children:
#    print(child)

#for decendant in bs.find('table',{'id':'giftList'}).descendants:
#    print(decendant)

#for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
#    print(sibling)

#for title in bs.find('table',{'id':'giftList'}).tr:
#    print(title.get_text())


print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

