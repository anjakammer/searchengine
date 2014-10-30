from crawler import Crawler
from page_rank import PageRank
from normalizer import Normalizer

c = Crawler([
    'http://mysql12.f4.htw-berlin.de/crawl/d01.html',
    'http://mysql12.f4.htw-berlin.de/crawl/d06.html',
    'http://mysql12.f4.htw-berlin.de/crawl/d08.html'
])

c.start()
resources = c.web_resources
print(len(c.web_resources))

#for res in c.web_resources:
    #print("######")
    #print(res.url)
    #print(res.links)

pr = PageRank(resources)
print(pr.getCurrentRankRow())
print(pr.ranks)
pr.calculate()
print("THE RANKS")
print(pr.getCurrentRankRow())


for index, source in enumerate(resources):
    source.rank = pr.getCurrentRankRow()[index]

resources[0].extractText()
n = Normalizer(resources[0].extractText())
print(n.getTokens())
#for en in pr.end_nodes():
    #print(en.url)
#p = pr.backlinks_for(c.web_resources[0].url)
#print(c.web_resources[0].url)
#for i in p:
    #print(i.url)
#print("####")

#p = pr.parent_for(c.web_resources[1].url)
#print(c.web_resources[1].url)
#for i in p:
    #print(i.url)



