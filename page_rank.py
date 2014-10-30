class PageRank:
    graph = []
    ranks = []
    t = 0.05
    delta = 0.04

    def __init__(self, graph):
        self.graph = graph
        size = len(graph)
        first_row = []
        for index, node in enumerate(self.graph):
            first_row.append(1 / size)
        self.ranks.append(first_row)

    def calculate(self):
        running = True
        print("CALCULATE:")
        while running:
            new_rank_row = []
            for node in self.graph:
                new_rank_row.append(self.next_rank_for(node))

            delta_sum = 0
            for index, rank in enumerate(new_rank_row):
                delta_sum += abs(rank - self.getCurrentRankRow()[index])
            if delta_sum <= self.delta:
                running = False

            self.ranks.append(new_rank_row)

    def next_rank_for(self, node):
        currentRanks = self.getCurrentRankRow()
        next_rank = 0

        # Rakes from the backlinks
        for bl in self.backlinks_for(node.url):
            next_rank += currentRanks[self.graph.index(bl)] / len(bl.links)

        # Ranks from the end nodes
        for en in self.end_nodes():
            next_rank += currentRanks[self.graph.index(en)] / len(self.graph)

        return self.d() * next_rank + (self.t / len(self.graph))

    def getCurrentRankRow(self):
        if len(self.ranks[-1]) < len(self.graph):
            return self.ranks[-2]
        else:
            return self.ranks[-1]

    # Gives back the nodes which have url as a child
    def backlinks_for(self, url):
        parents = []
        for node in self.graph:
            if (url in node.links):
                parents.append(node)
        return parents

    # Gives back the nodes which have no childern
    def end_nodes(self):
        end_nodes = []
        for node in self.graph:
            if (len(node.links) == 0):
                end_nodes.append(node)
        return end_nodes

    def d(self):
        return 1 - self.t


