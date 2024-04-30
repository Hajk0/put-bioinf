from generator import Generator
from individual import Individual


class Population:
    def __init__(self, num_individuals, filename, expected_length) -> None:
        print("Creating population...")
        self.individuals = []
        self.best_individual = None
        self.best_fitness = 0
        self.expected_length = expected_length
        self.num_individuals = num_individuals
        generator = Generator(filename, expected_length)
        for i in range(num_individuals):
            print(f"Creating individual {i + 1}/{num_individuals}")
            sequence, chromosome, all_sequences = generator.generate_individual()
            self.individuals.append(Individual(chromosome, sequence, all_sequences, expected_length))
