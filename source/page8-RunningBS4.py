from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://bitcointreasuries.org/")
bs = BeautifulSoup(html.read(),'html.parser')
print(bs.section)

