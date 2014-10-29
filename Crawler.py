__author__ = 'Anja'

import urllib2
from Resource import Resource
from bs4 import BeautifulSoup # To get everything
from string import Template
# Crawler besteht aus Downloader, Parser(Beautiful Soup) und Frontier
# Lucas, Ado

class Crawler():
    toVisit = []
    blacklist = []
    resources = []
    def __init__(self):
        urls = ['http://mysql12.f4.htw-berlin.de/crawl/d01.html','http://mysql12.f4.htw-berlin.de/crawl/d06.html', 'http://mysql12.f4.htw-berlin.de/crawl/d08.html']
        self.toVisit.extend(urls)
        self.frontier()

    def downloadSite(self, page):
        content = urllib2.urlopen(page).read()
        return content

    def parse(self, url):
        href = []
        html = urllib2.urlopen(url)
        source = BeautifulSoup(html.read())
        links = source.find_all('a')
        for link in links:
            if link.has_attr('href'):
                link = link['href']
                if (link.find('http://')) >= -1:
                    s = Template('http://mysql12.f4.htw-berlin.de/crawl/$url')
                    link = s.substitute(url=link)
                href.append(link)

        #erzeuge das Resources Object
        content = self.downloadSite(url) # Content muss in den Index
        self.resources.append(Resource(url, href, content))
        # Ende Downloader und Resourcenbau
        return href

    def frontier(self):
        while (len(self.toVisit) >0):               # Seed URLS in ToVisit
            for link in self.toVisit:
                foundLinks = self.parse(link)       # hole alle links raus
                for url in foundLinks:
                    if (self.blacklist.__contains__(url) or self.toVisit.__contains__(url)):    # schon auf eine Liste?
                        foundLinks.remove(url)                                                  # haben wir schon, kann weg

                self.toVisit.extend(foundLinks)
                self.blacklist.append(link)
                for link in self.blacklist:
                    if self.toVisit.__contains__(link):
                        self.toVisit.remove(link)
        print self.toVisit
        print self.resources
Crawler()