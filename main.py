from node import Node


def greedy_sequence_reconstruction(seqs):
    result = ''
    
    while len(seqs) > 0:
        # Znajdź najczęściej występujący prefiks
        prefix_count = {}
        for seq in seqs:
            prefix = seq[:2]  # Załóżmy, że długość prefiksu wynosi 2
            if prefix in prefix_count:
                prefix_count[prefix] += 1
            else:
                prefix_count[prefix] = 1
        
        most_common_prefix = max(prefix_count, key=prefix_count.get)
        
        # Dołącz prefiks do łańcucha wynikowego
        result += most_common_prefix
        
        # Usuń wszystkie wystąpienia prefiksu z sekwencji
        seqs = [seq.replace(most_common_prefix, '', 1) for seq in seqs]
        
        # Usuń puste sekwencje
        seqs = [seq for seq in seqs if seq]
    
    return result


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


# Wczytaj sekwencje z pliku
filename = 'sequences_positive.txt'  # nazwa pliku z sekwencjami
sequences = read_sequences_from_file(filename)

# Odtwórz sekwencję
reconstructed_sequence = greedy_sequence_reconstruction(sequences)
print("Odtworzona sekwencja:", reconstructed_sequence)
print(len(reconstructed_sequence))

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

