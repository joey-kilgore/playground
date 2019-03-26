from bs4 import BeautifulSoup
import requests
import time
import os, sys
from time import gmtime, strftime

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()



THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file_path = os.path.join(THIS_FOLDER, 'webScrapeOutput '+strftime("%Y_%m_%d %H_%M_%S", gmtime())+ '.txt')
my_file = open(my_file_path, 'w')

url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=unmyelinated+model'
r = requests.get(url)

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
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    data = r.text
    soup = BeautifulSoup(data)
    for div in soup.find_all('div', class_='rslt'):
        for subDiv in div.find_all('p'):
            for link in subDiv.find_all('a'):
                if not 'uid' in link.get('href') and not ('https://www.ncbi.nlm.nih.gov' + link.get('href')) in articles:
                    totalArticles+=1
                    articles.append('https://www.ncbi.nlm.nih.gov' + link.get('href'))

progress = 0
for link in articles:
    my_file.write(link+'\n')
    gettingPage = True
    while gettingPage:
        try:
            r = requests.get(link)
            gettingPage = False
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    data = r.text
    soup = BeautifulSoup(data)
    for div in soup.find_all('div', class_='rprt abstract'):
        for h1 in div.find_all('h1'):
            try:
                my_file.write(str(h1.getText())+'\n')
            except:
                my_file.write('unknownn character/title\n')  
    my_file.write('\n')
    progress+=1
    printProgressBar(progress, len(articles), prefix = 'Progress:', suffix = 'Complete', length = 50)
my_file.close()
print('TOTAL ARTICLES: '+str(totalArticles))
