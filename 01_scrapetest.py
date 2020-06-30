from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser")
        title = bsObj.body.nonsense
    except AttributeError as e:
        return None
    return title


title = get_title("http://pythonscraping.com/exercises/exercise1.html")
print(title) if title else print("Title could not be found")