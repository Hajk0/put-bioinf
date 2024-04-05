import random


def read_sequences_from_file(filename):
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            sequences.append(line.strip())
    return sequences


def greedy(sequences, full_sequence_length):
    sequence = random.choice(sequences)
    sequences.remove(sequence)
    while len(sequence) < full_sequence_length:
        print(len(sequence))
        next_sequence, overlaping_next = find_best_next_sequence(sequence, sequences)
        prev_sequence, overlaping_prev = find_best_prev_sequence(sequence, sequences)
        if overlaping_next > 0:
            sequence += next_sequence[overlaping_next:]
            sequences.remove(next_sequence)
        if overlaping_prev > 0:
            sequence = prev_sequence[:overlaping_prev] + sequence
            sequences.remove(prev_sequence)
        if not overlaping_prev and not overlaping_next:
            return sequence
    print(len(sequence))
    return sequence


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


def find_best_prev_sequence(sequence, sequences):
    best_result = 0
    best_sequence = ""
    for s in sequences:
        result = compare_next_sequences(s, sequence)
        if result > best_result:
            best_result = result
            best_sequence = s
    return best_sequence, best_result


if __name__ == "__main__":
    data = read_sequences_from_file("sequences_positive.txt")
    print(data)
    print(compare_next_sequences("abc", "bcd"))
    print(find_best_next_sequence("abc", ["bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz", "yza", "zab"]))
    print(find_best_prev_sequence("abc", ["bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz", "yza", "zab"]))
    print(greedy(data, 209))