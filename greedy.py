class Greedy:
    def __init__(self, graph):
        self.graph = graph

    def reconstruct_sequence(self, sequence_length):
        result = ''
        best_result = ''
        for node in self.graph.values():
            print("NEW START")
            result = node.data
            current_node = node
            prev_node = None
            while current_node.next:
                prev_node = current_node
                current_node = current_node.next[0]
                print(current_node.data, prev_node.cost)
                result += current_node.data[-prev_node.cost[0]:]
            if len(result) > len(best_result):
                best_result = result
            if len(result) == sequence_length:
                return best_result
        return best_result
