class Node:
    def __init__(self, data):
        self.data = data
        self.next = []

    def check_next(self, graph):
        for node in graph.values():
            if node.data == self.data:
                continue
            elif node.data[:-1] == self.data[1:]: # pasuja idealnie (9 takich samych znakow)
                self.add_next(node)
            # print(len(node.data[:-2]), len(self.data[1:]))

    def add_next(self, node):
        self.next.append(node)