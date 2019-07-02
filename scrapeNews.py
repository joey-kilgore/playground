from bs4 import BeautifulSoup
import requests
import time
from random import randint


def scrape_news_summaries(s):
    time.sleep(randint(0, 2))  # relax and don't let google be angry
    r = requests.get("http://www.google.com/search?q="+s+"&tbm=nws")
    print(r.status_code)  # Print the status code
    content = r.text
    news_summaries = []
    soup = BeautifulSoup(content, "html.parser")
    #print(soup)
    links = soup.findAll("a")
    #print(links)
    for link in links:
        #print(link['href'])
        if '/url?q=' in link['href']:
            news_summaries.append(link['href'].replace('/url?q=',''))
    return news_summaries


l = scrape_news_summaries("AAPL")
#l = scrape_news_summaries("""T-Notes""")
for n in l:
    print(n)