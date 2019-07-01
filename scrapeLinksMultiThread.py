from bs4 import BeautifulSoup
import requests
import time
import os, sys
from time import gmtime, strftime
from multiprocessing.dummy import Pool as ThreadPool

def getArticleLinks(originalSearchURL):
    r = requests.get(originalSearchURL)
    data = r.text
    soup = BeautifulSoup(data)

    otherPages = []
    totalArticles = 0
    articles = []
    for div in soup.find_all('div', class_='rslt'):
	    for subDiv in div.find_all('p'):
		    for link in subDiv.find_all('a'):
			    #print(link.get('href'))
			    if 'uid' in link.get('href'):
				    otherPages.append('https://www.ncbi.nlm.nih.gov' + link.get('href'))
			    else:
				    totalArticles+=1
				    articles.append('https://www.ncbi.nlm.nih.gov' + link.get('href'))

    for url in otherPages:
        print(url)
        gettingPage = True
        while gettingPage:
            try:
                r = requests.get(url)
                gettingPage = False
            except:
                #print("Connection refused by the server..")
                #print("Let me sleep for 5 seconds")
                #print("ZZzzzz...")
                time.sleep(5)
                #print("Was a nice sleep, now let me continue...")
            continue

        data = r.text
        soup = BeautifulSoup(data)
        for div in soup.find_all('div', class_='rslt'):
            for subDiv in div.find_all('p'):
                for link in subDiv.find_all('a'):
                    if not 'uid' in link.get('href') and not ('https://www.ncbi.nlm.nih.gov' + link.get('href')) in articles:
                        totalArticles+=1
                        articles.append('https://www.ncbi.nlm.nih.gov' + link.get('href'))
    return articles


def getTitle(articleURL):
    print(articleURL)
    gettingPage = True
    while gettingPage:
        try:
            r = requests.get(articleURL)
            gettingPage = False
        except:
            #print("Connection refused by the server..")
            #print("Let me sleep for 5 seconds")
            #print("ZZzzzz...")
            time.sleep(5)
            #print("Was a nice sleep, now let me continue...")
            continue

    data = r.text
    soup = BeautifulSoup(data)
    for div in soup.find_all('div', class_='rprt abstract'):
        for h1 in div.find_all('h1'):
            try:
                return str(h1.getText())+'\n'
            except:
                return 'unknownn character/title' 
    return 'no article title found'

def saveArticlesToFile(titles, links):
    dateTime = time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = 'scrapedArticles_'+dateTime+'.txt'
    file = open(fileName, 'w')
    for i in range(len(titles)):
        try:
            file.write(titles[i])
        except:
            file.write('Unknown Title')
        file.write(links[i])
        file.write('\n\n')

def main():
    url = ''
    if len(sys.argv) > 1:
        search = ''
        for word in sys.argv[1:]:
            search += word + '+'
        search[:-1]
        url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=' + search
    else:
        url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=unmyelinated+model'

    startTime = time.time()
    links = getArticleLinks(url)
    pool = ThreadPool(30)
    titles = pool.map(getTitle, links)
    totalTime = time.time()-startTime
    print('TITLES FOUND: ' + str(len(titles)))
    print('TIME: ' + str(totalTime))
    saveArticlesToFile(titles, links)

main()
