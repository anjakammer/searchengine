import re
from bs4 import BeautifulSoup

class WebResource:
    links = set()
    text = ''
    rank = 0

    def __init__(self, req):
        self.request = req
        self.url = req.url
        self.content_type = req.headers['content-type']
        if self.content_type == 'text/html':
            self.extractAllUrls()

    def extractAllUrls(self):
        soup = BeautifulSoup(self.request.content)
        self.links = [self.linkToUrl(link) for link in soup.findAll("a", href=True)]

    def extractText(self):
        soup = BeautifulSoup(self.request.content)
        return "".join(soup.body(text=True))

    # When a link has no host file name, add the domain
    # of its parent. So its guaranteed that every link is a full url.
    def linkToUrl(self, link):
        try:
            link['href'].index('http')
            return link['href']
        except ValueError:
            return re.sub(r"/[^/]*$", "/" + link['href'], self.request.url)

    #def __eq__(self, other):
        #if isinstance(other, self.__class__):
            #return self.url == other.url
        #else:
            #return False

    #def __ne__(self, other):
        #return not self.__eq__(other)
