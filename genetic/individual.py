import random

class Individual:
    def __init__(self, chromosome, sequence, avaible_sequences, expected_length) -> None:
        self.chromosome = chromosome
        self.sequence = sequence
        self.avaible_sequences = avaible_sequences
        self.expected_length = expected_length
        self.fitness = self.calculate_fitness()

    def __repr__(self) -> str:
        STR = ""
        STR += f"\nChromosome: {self.chromosome}"
        STR += f"\nSequence: {self.sequence}" 
        STR += f"\nFitness: {self.fitness}"
        return STR

    def calculate_fitness(self):
        seq_used = len(self.chromosome)
        full_seq_len = len(self.sequence)
        return (seq_used - (abs(full_seq_len - self.expected_length))) / full_seq_len

    def crossover(self, otherIndividual):
        cutting_place = random.randint(len(self.sequence))
        for i in range(cutting_place):
            pass
        # TODO(finish crossover function)

    def check_fit(self, left_sequence, right_sequence):
        best_result = 0
        for i in range(1, len(left_sequence)):
            if left_sequence[-i:] == right_sequence[:i]:
                best_result = i
        return best_result

