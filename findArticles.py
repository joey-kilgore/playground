from bs4 import BeautifulSoup
import requests
import time

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
				articles.append(link.get('href'))

for url in otherPages:
	#print('Hold on')
	#time.sleep(5)
	#print('Hold off')
	print(url)
	r = requests.get(url)
	#time.sleep(5)
	data = r.text
	soup = BeautifulSoup(data)
	for div in soup.find_all('div', class_='rslt'):
		for subDiv in div.find_all('p'):
			for link in subDiv.find_all('a'):
				if not 'uid' in link.get('href'):
					totalArticles+=1
					articles.append(link.get('href'))
for link in articles:
	print(link)
print('TOTAL ARTICLES: '+str(totalArticles))
