import requests
from bs4 import BeautifulSoup

URL = "https://openflights.org/html/route-maps"

def send_request():
    try:
        r = requests.get(URL,timeout=3)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err) 

    return r.content

def toBs4Soup():
    soup=BeautifulSoup(send_request(),"lxml")
    airlines = soup.find_all("a", href=lambda href: href and "airline" in href)
    
    return list(map(lambda tags: tags.text,airlines))
myList = []
def parse():
    hrefTags = toBs4Soup()
    
    phase1 = list(map(lambda parsed1: parsed1.split(" ("),hrefTags))
    airline_kısaltma = list(map(lambda y:y[1],phase1 ))
    airline_ad = list(map(lambda y:y[0].strip(),phase1 ))
    phase2 = list(map(lambda parsed2: parsed2.split(")"),airline_kısaltma))
    airline_kısaltma = list(map(lambda y:y[0].strip(),phase2 ))
    #print(len(airline_kısaltma))
    myList = list(zip(airline_ad,airline_kısaltma))
    print(myList)
parse()
