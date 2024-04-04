class Greedy:
    def __init__(self, graph):
        self.graph = graph

    def reconstruct_sequence(self, sequence_length):
        result = ''
        for node in self.graph.values():
            result = node.data
            current_node = node
            while current_node.next:
                current_node = current_node.next[0]
                result += current_node.data[-1]
            if len(result) == sequence_length:
                return result
