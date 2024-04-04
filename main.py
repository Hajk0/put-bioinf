from node import Node
from greedy import Greedy


def read_sequences_from_file(filename):
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            sequences.append(line.strip())
    return sequences


def create_graph(seqs):
    graph = {}

    for seq in seqs:
        if seq not in graph:
            graph[seq] = Node(seq)

    for node in graph.values():
        node.check_next(graph)
    
    return graph


if __name__ == '__main__':
    # Wczytaj sekwencje z pliku
    filename = 'sequences_positive.txt'  # nazwa pliku z sekwencjami
    sequences = read_sequences_from_file(filename)

    # Stwórz graf
    graph = create_graph(sequences)
    nodes_count = len(graph)
    next_count = 0
    for node in graph.values():
        print(node.data, [n.data for n in node.next])
        if node.next:
            next_count += len(node.next)
    print("Liczba węzłów:", nodes_count)
    print("Liczba krawędzi:", next_count)

    #
    # # Stwórz obiekt klasy Greedy
    greedy = Greedy(graph)
    result_greedy = greedy.reconstruct_sequence(sequence_length=209)
    print("Odtworzona sekwencja (Greedy):", result_greedy)
    print(len(result_greedy))