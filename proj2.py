#proj2.py


#### Problem 1 ####
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, urllib.error, urllib.parse

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

siteHandle = "http://nytimes.com"

html=urlopen(siteHandle, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

count = 0
for header in soup.find_all('h2'):
    if count < 10:
        if header.has_attr('class') and header['class'][0] == 'story-heading' and header.a:
            foundText = header.a.get_text().replace("/n", " ").strip()
            print(foundText)
            #print(count)
            count+=1


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here



#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
