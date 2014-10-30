import requests
from web_resource import WebResource

class Crawler:
    to_visit = set()
    visited = set()
    web_resources = []

    def __init__(self, start_urls):
        self.to_visit = set(start_urls)

    # Frontier. Starts the crawling.
    # Main loop and logic for visit the pages.
    def start(self):
        while(self.to_visit):
            # Download
            current_url = self.to_visit.pop()
            request = self.download(current_url)
            web_resource = WebResource(request)
            # Parse
            self.web_resources.append(web_resource)
            self.addUnknownUrlsToVisit(web_resource.links)

        # Show the visited
        #for web_resource in self.web_resources:
            #print("------")
            #print(web_resource.request.url)
            #print(web_resource.urls)

    # Downloads a url and marks the url as visited.
    def download(self, url):
        self.visited.add(url)
        return requests.get(url)

    # Checks if the urls are in the set visited. When not it
    # Adds them to the set to_visit for further crawling.
    def addUnknownUrlsToVisit(self, urls):
        for url in urls:
            if url not in self.visited:
                self.to_visit.add(url)



