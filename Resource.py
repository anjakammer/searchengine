__author__ = 'Anja'

class Resource(object):
    url = ""
    href = []
    content = ""

    def __init__(self, url, href, content):
        self.url = url
        self.href = href
        self.content = content
