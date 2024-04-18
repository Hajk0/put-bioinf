import random

def read_sequences_from_file(filename):
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            sequences.append(line.strip())
    return sequences


def greedy(sequences, full_sequence_length):
    sequences_busy = [] # zmienić nazwę
    sequence_index = random.randint(0, len(sequences) - 1)
    sequences_busy.append(sequence_index)
    sequence = sequences[sequence_index]

    chromosome = [] # lista numerów sekwencji
    sequences_used = 1
    coveragee = 0

    while len(sequence) < full_sequence_length:
        pass


def compare_next_sequences(sequence, next_sequence, l=10):
    best_result = 0
    for i in range(1, l):
        if sequence[-i:] == next_sequence[:i]:
            best_result = i
    return best_result


def find_best_next_sequence(sequence, sequences):
    best_result = 0
    best_sequence = ""
    for s in sequences:
        result = compare_next_sequences(sequence, s)
        if result > best_result:
            best_result = result
            best_sequence = s
    return best_sequence, best_result