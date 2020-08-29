import html2text
import requests

url = requests.get("https://www.fool.com/investing/2020/05/13/is-this-warren-buffetts-favorite-stock-right-now.aspx")
htmltext = url.text
print(htmltext)

h = html2text.HTML2Text()
h.ignore_links = True
text = h.handle(htmltext)
print(text)