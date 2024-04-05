class Node:
    def __init__(self, data):
        self.data = data
        self.next = []
        self.cost = []

    def check_next(self, graph, l=10):

        for i in range(1, len(self.data)):
            print(i)
            for node in graph.values():
                if node.next:
                    continue
                if node.data == self.data:
                    continue
                if node.data[:-i] == self.data[i:]:
                    self.add_next(node, i)

    def add_next(self, node, c): # c - cost (ilość nowych znaków w porównaniu do poprzedniego słowa)
        self.next.append(node)
        self.cost.append(c)