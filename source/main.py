from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

def bsoup(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None

    bs = BeautifulSoup(html.read(),'html.parser')

    return bs

def getNumofCompany(bs):
    companies = bs.find_all('td',{'class':'s10'})
    return (len(companies))

def getNumOfBitAndValue(bs):
    numValue = bs.find_all('td',{'class':'s60'})
    num = numValue[1].get_text().split(" ")
    basicvalue = numValue[0].get_text().strip('$')
    return num[1], basicvalue

def getToDayValue(bs):
    todayValues = bs.find_all('td',{'class':'s61'})
    tdvalue= todayValues[0].get_text().strip('$')
    return tdvalue
def main():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQHcNgqvu0l1S-aBE12KEooSK9CQlw7LrKA2M9ZToRMw4f5DM31TOvexQOIPu32lf0TLhVSpHJMCxdT/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false'
    bs = bsoup(url)
    numOfCompany = getNumofCompany(bs)
    num,basicvalue = getNumOfBitAndValue(bs)
    todayvalue=getToDayValue(bs)
    print(num)
    print(basicvalue)
    print(todayvalue)

if __name__ =="__main__":
    main()



