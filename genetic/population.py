import random
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
            #print(f"Creating individual {i + 1}/{num_individuals}")
            sequence, chromosome, all_sequences = generator.generate_individual()
            self.individuals.append(Individual(chromosome, sequence, all_sequences, expected_length))
    
    def evolve(self, generations=100, mutation_rate=0.01):
        for gen in range(generations):
            new_individuals = []
            for i in range(len(self.individuals)):
                parent1 = self.tournament_selection()
                parent2 = self.tournament_selection()
                try:
                    child = parent1.crossover(parent2)
                    child.mutate(mutation_rate)
                    new_individuals.append(child)
                except Exception as e:
                    print(f"Error during crossover/mutation: {e}")
            self.individuals = new_individuals
            self.update_best_individual()
            #print(f"Generation {gen + 1}: Best fitness = {self.best_fitness}")

    def tournament_selection(self, tournament_size=5):
        tournament = random.sample(self.individuals, tournament_size)
        best = max(tournament, key=lambda x: x.fitness)
        return best

    def update_best_individual(self):
        best = max(self.individuals, key=lambda x: x.fitness)
        if best.fitness > self.best_fitness:
            self.best_individual = best
            self.best_fitness = best.fitness
