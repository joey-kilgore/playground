import wikipediaapi

# getting a wiki page
wiki = wikipediaapi.Wikipedia('en')
page = wiki.page('Python_(programming_language)')

# check if page exists
print('Page - Exists: %s' % page.exists())

# get data from the page
#   like a title
print('Page - Title: %s' % page.title)
#   or the summary
print('Page - Summary: %s' % page.summary[0:60])

# get the URL
print(page.fullurl)
print()

# get full text
wiki = wikipediaapi.Wikipedia(
        language = 'en',
        extract_format = wikipediaapi.ExtractFormat.WIKI
        )
testWiki = wiki.page('Stuff')
print('TEST WIKI TEXT')
print(testWiki.text)
print()

# get in html format
wiki = wikipediaapi.Wikipedia(
        language = 'en',
        extract_format = wikipediaapi.ExtractFormat.HTML
        )
testWiki = wiki.page('Stuff')
print('TEST WIKI HTML')
print(testWiki.text)
print()

# get page sections
def print_sections(sections, level=0):
    for s in sections:
        print('%s: %s - %s' % ('*'*(level+1), s.title, s.text[0:40]))
        print_sections(s.sections, level+1)

print_sections(page.sections) # goes through the python page

# get links to other pages
def print_links(page):
    links = page.links
    for title in sorted(links.keys()):
        print('%s: %s' % (title, links[title]))

print_links(page) # goes through the python page

