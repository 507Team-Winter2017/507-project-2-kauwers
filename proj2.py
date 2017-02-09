#proj2.py
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, urllib.error, urllib.parse

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#I don't want to keep writing a way to get the Soup each time, returns the soup from a link input
def getSoup(link):
    thePage = link
    html=urlopen(thePage, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
### Your Problem 1 solution goes here
soup = getSoup("http://nytimes.com")
count = 0
for header in soup.find_all('h2'):
    if count < 10:
        if header.has_attr('class') and header['class'][0] == 'story-heading' and header.a:
            foundText = header.a.get_text().replace("/n", " ").strip()
            print(foundText)
            count+=1

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')
### Your Problem 2 solution goes here
soup = getSoup("http://michigandaily.com")
for section in soup.find_all('div'):
    if section.has_attr('class'):
        classList = section['class']
        if 'view-most-read' in classList:
            print(section.get_text().replace("/n", " ").strip())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
soup = getSoup("http://newmantaylor.com/gallery.html")
for image in soup.find_all('img'):
    if image.has_attr('alt'):
        altText = image['alt'].replace("/n", " ").strip()
        print(altText)
    else:
        print("No alternative text provided!!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")
### Your Problem 4 solution goes here



#this should take a web address, create soup from it, grab a contact email from that soup, print it and the count, and pass the count back to the calling function
def grabEmail(count, link):
    soup = getSoup(link)
    #print(soup)

    return count

#this should find all contact page links on a given page, and pass that link (and the count of pages found) to the grabEmail function.  It should return the count to it's calling function
def crawlContacts(count, link):
    return count

#this should cycle through all directory pages, maintaining the count, and calling the crawlContacts function for each page
def crawlFullDirectory(count, link):
    return

theCount = 0
grabEmail(theCount, "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4")
