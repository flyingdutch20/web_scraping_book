from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


pages = set()
random.seed(datetime.datetime.now())


def getInternalLinks(bsObj, includeUrl):
    #retrieve a list of all internal links found on a page
    internalLinks = []
    #find all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                internalLinks.append(link.attrs["href"])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    #retrieve a list of all external links found on a page
    externalLinks = []
    #find all links that start with http or www
    #that do not contain the current url
    for link in bsObj.findAll("a",
                              href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0,
                                                                len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)- 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("https://www.dedoimedo.com/index.html")
