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
    sequences_used = 1
    coverage = 0
    while len(sequence) < full_sequence_length:
        # print(len(sequence))
        next_sequence, overlaping_next = find_best_next_sequence(sequence, sequences)
        prev_sequence, overlaping_prev = find_best_prev_sequence(sequence, sequences)
        if overlaping_next > 0 and overlaping_next > overlaping_prev:
            sequence += next_sequence[overlaping_next:]
            sequences.remove(next_sequence)
            sequences_used += 1
        if overlaping_prev > 0 and overlaping_prev >= overlaping_next:
            sequence = prev_sequence[:overlaping_prev] + sequence
            sequences.remove(prev_sequence)
            sequences_used += 1
        if not overlaping_prev and not overlaping_next:
            return sequence, coverage
    # print(len(sequence))
    coverage = sequences_used / len(sequence)
    # print("Coverage: ", coverage)
    return sequence, coverage


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
    data = read_sequences_from_file("sequences_negative.txt")
    # print(data)
    # print(compare_next_sequences("abc", "bcd"))
    # print(find_best_next_sequence("abc", ["bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz", "yza", "zab"]))
    # print(find_best_prev_sequence("abc", ["bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz", "yza", "zab"]))
    best_seq = ''
    best_coverage = 0
    for i in range(1000):
        result, coverage = greedy(data.copy(), 209)
        # print(result)
        # print(coverage)
        if best_coverage < coverage:
            best_seq = result
            best_coverage = coverage
        if coverage > 0.8:
            print(coverage)
    print(best_coverage)
    print(best_seq)
