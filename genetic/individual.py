import random
3
class Individual:
    def __init__(self, chromosome, sequence, avaible_sequences, expected_length) -> None:
        self.chromosome = chromosome # List of tuples (index, overlaping)
        self.sequence = sequence # String of the sequence
        self.avaible_sequences = avaible_sequences # List of all sequences
        self.expected_length = expected_length
        self.normalize_chromosome()
        self.update_sequence()
        self.fitness = self.calculate_fitness()

    def __repr__(self) -> str:
        STR = ""
        STR += f"\nChromosome: {self.chromosome}"
        STR += f"\nSequence: {self.sequence}" 
        STR += f"\nFitness: {self.fitness}"
        return STR
    
    def normalize_chromosome(self):
        center_found = False
        for i in range(len(self.chromosome) - 1):
            if self.chromosome[i][1] == -1:
                center_found = True
            if center_found:
                self.chromosome[i] = (self.chromosome[i][0], self.chromosome[i + 1][1])
        self.chromosome[-1] = (self.chromosome[-1][0], 0)
    
    def update_sequence(self):
        self.sequence = self.avaible_sequences[self.chromosome[0][0]]
        for i in range(1, len(self.chromosome)):
            if i > -1:
                self.sequence += self.avaible_sequences[self.chromosome[i][0]][self.chromosome[i - 1][1]:]

    def calculate_fitness(self):
        seq_used = len(self.chromosome)
        full_seq_len = len(self.sequence)
        return (seq_used - (abs(full_seq_len - self.expected_length))) / full_seq_len

    def crossover(self, otherIndividual):
        new_chromosome = []
        unavailable_indexes = set()
        random_cut = random.randint(0, len(self.chromosome) - 1)
        
        for i in range(random_cut):
            new_chromosome.append(self.chromosome[i])
            unavailable_indexes.add(self.chromosome[i][0])

        for i in range(random_cut, len(otherIndividual.chromosome)):
            if otherIndividual.chromosome[i][0] not in unavailable_indexes:
                if new_chromosome:
                    fit = self.check_fit(self.avaible_sequences[new_chromosome[-1][0]], self.avaible_sequences[otherIndividual.chromosome[i][0]])
                    new_chromosome.append((otherIndividual.chromosome[i][0], fit))
                else:
                    new_chromosome.append(otherIndividual.chromosome[i])
                unavailable_indexes.add(otherIndividual.chromosome[i][0])

        new_individual = Individual(new_chromosome, "", self.avaible_sequences, self.expected_length)
        return new_individual

    def mutate(self, mutation_rate=0.01):
        for i in range(len(self.chromosome)):
            if random.random() < mutation_rate:
                new_index = random.randint(0, len(self.avaible_sequences) - 1)
                if new_index not in [c[0] for c in self.chromosome]:
                    fit = self.check_fit(self.avaible_sequences[self.chromosome[i - 1][0]], self.avaible_sequences[new_index])
                    self.chromosome[i] = (new_index, fit)
        self.update_sequence()
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        seq_used = len(self.chromosome)
        full_seq_len = len(self.sequence)
        return (seq_used - (abs(full_seq_len - self.expected_length))) / full_seq_len

    def check_fit(self, left_sequence, right_sequence):
        best_result = 0
        for i in range(1, len(left_sequence)):
            if left_sequence[-i:] == right_sequence[:i]:
                best_result = i
        return best_result

