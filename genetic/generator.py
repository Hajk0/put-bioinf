import random
from individual import Individual


class Generator:
    def __init__(self, filename, full_sequence_length):
        self.full_sequence_length = full_sequence_length
        self.sequences = []
        with open(filename, 'r') as file:
            for line in file:
                self.sequences.append(line.strip())

    def generate_individual(self):
        chromosome = []
        index = random.randint(0, len(self.sequences) - 1)
        sequence = self.sequences[index]
        chromosome.append((index, -1))

        while len(sequence) < self.full_sequence_length:
            random_direction = random.choice(["next", "prev"])
            random_addition = random.choice(["random", "best"])
            random_addition = "best"#
            if random_addition == "random":
                index, overlaping = self.find_random_sequence(sequence, [c[0] for c in chromosome], random_direction) # chromosome[0]
            elif random_addition == "best":
                index, overlaping = self.find_best_sequence(sequence, [c[0] for c in chromosome], random_direction)

            if index == -1:
                break

            if random_direction == "next":
                sequence += self.sequences[index][overlaping:]
                chromosome.append((index, overlaping))
            elif random_direction == "prev":
                sequence = self.sequences[index][:-overlaping] + sequence
                chromosome.insert(0, (index, overlaping))

        return sequence, chromosome, self.sequences


    
    def compare_next_sequences(self, sequence, next_sequence):
        best_result = 0
        for i in range(1, len(next_sequence)):
            if sequence[-i:] == next_sequence[:i]:
                best_result = i
        return best_result

    def find_best_sequence(self, main_sequence, used_indexes, direction="next"): # direction: next or prev
        best_index = -1
        best_overlapping = 0
        for i in range(len(self.sequences)):
            if i in used_indexes:
                continue
            if direction == "next":
                overlapping = self.compare_next_sequences(main_sequence, self.sequences[i])
            elif direction == "prev":
                overlapping = self.compare_next_sequences(self.sequences[i], main_sequence)

            if overlapping > best_overlapping:
                best_overlapping = overlapping
                best_index = i

        return best_index, best_overlapping

    def find_random_sequence(self, main_sequence, used_indexes, direction="next"):
        while True:
            index = random.randint(0, len(self.sequences) - 1)
            if index not in used_indexes:
                if direction == "next":
                    overlapping = self.compare_next_sequences(main_sequence, self.sequences[index])
                    if overlapping > 0:
                        return index, overlapping
                if direction == "prev" and self.compare_next_sequences(self.sequences[index], main_sequence) > 0:
                    overlapping = self.compare_next_sequences(self.sequences[index], main_sequence)
                    if overlapping > 0:
                        return index, overlapping
        


if __name__ == "__main__":
    generator = Generator("../data/sequences_negative.txt", 209)
    best = generator.find_best_sequence("AAAAAAAAAA", [], "next")
    randoms = generator.find_random_sequence("AAAAAAAAAA", [], "prev")
    print(best, generator.sequences[best[0]])
    print(randoms, generator.sequences[randoms[0]])
    individual_data = generator.generate_individual()
    print(individual_data)

    individual = Individual(individual_data[1], individual_data[0], individual_data[2], 209)
    print(individual.calculate_fitness)
    other_individual = Individual(individual_data[1], individual_data[0], individual_data[2], 209)
    print("Crossover:")
    new_individual = individual.crossover(other_individual)
    print(new_individual)
    