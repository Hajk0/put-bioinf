import random
from generator import Generator
from individual import Individual


class Population:
    def __init__(self, num_individuals, filename, expected_length, random_probability=0.1) -> None:
        print("Creating population...")
        self.individuals = []
        self.best_individual = None
        self.best_fitness = 0
        self.expected_length = expected_length
        self.num_individuals = num_individuals
        generator = Generator(filename, expected_length)
        for i in range(num_individuals):
            #print(f"Creating individual {i + 1}/{num_individuals}")
            sequence, chromosome, all_sequences = generator.generate_individual(random_probability=random_probability)
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
            # self.delete_worst_individuals()
            # print(self.num_individuals)
            self.update_best_individual()
            print(self.best_individual.fitness)
            #print(f"Generation {gen + 1}: Best fitness = {self.best_fitness}")

    def evolve2(self, generations=100, selection_rate=0.8, mutation_rate_individual=0.001, mutation_rate_gene=1, skip_best=10):
        self.sort_individuals()
        for gen in range(generations):
            free_spots = int(self.num_individuals * selection_rate)
            self.individuals = self.individuals[:free_spots]
            for child in range(free_spots, self.num_individuals):
                parent1 = self.tournament_selection(1)
                parent2 = self.tournament_selection(1)
                #try:
                child = parent1.crossover(parent2)
                ## Mutate only child
                # for i in range(int(mutation_rate_individual * len(child.chromosome))):
                child.mutate2(mutation_rate_gene)
                ##
                self.individuals.append(child)
                #except Exception as e:
                #    print(f"Error during crossover/mutation: {e}")
            ## Mutate all individuals
            for i in range(skip_best, len(self.individuals)): # Skip the best individuals
                if random.random() < mutation_rate_individual:
                    self.individuals[i].mutate2(mutation_rate_gene)
            ##
            self.sort_individuals()
            self.update_best_individual()
            if gen % 1000 == 0:
                print(f"Generation {gen + 1}: Best fitness = {self.best_fitness}")
                self.print_head()

    def evolve_if_progress(self, generations=10000, selection_rate=0.8, mutation_rate_individual=0.01, mutation_rate_gene=1, skip_best=10):
        self.sort_individuals()
        generations_without_progress = 0
        gen = 0
        while generations_without_progress < generations:
            free_spots = int(self.num_individuals * selection_rate)
            self.individuals = self.individuals[:free_spots]
            for child in range(free_spots, self.num_individuals):
                parent1 = self.tournament_selection(1)
                parent2 = self.tournament_selection(1)
                #try:
                child = parent1.crossover(parent2)
                ## Mutate only child
                # for i in range(int(mutation_rate_individual * len(child.chromosome))):
                child.mutate2(mutation_rate_gene)
                ##
                self.individuals.append(child)
                #except Exception as e:
                #    print(f"Error during crossover/mutation: {e}")
            ## Mutate all individuals
            for i in range(skip_best, len(self.individuals)): # Skip the best individuals
                if random.random() < mutation_rate_individual:
                    self.individuals[i].mutate2(mutation_rate_gene)
            ##
            self.sort_individuals()
            gen += 1
            generations_without_progress += 1
            if (self.update_best_individual()):
                generations_without_progress = 0
            if gen % 1000 == 0:
                print(f"Generation {gen + 1}: Best fitness = {self.best_fitness}")
                self.print_head()
        

    def sort_individuals(self):
        self.individuals = sorted(self.individuals, key=lambda x: x.fitness, reverse=True)

    def tournament_selection(self, tournament_size=5):
        tournament = random.sample(self.individuals, tournament_size)
        best = max(tournament, key=lambda x: x.fitness)
        return best

    def delete_worst_individuals(self):
        num_to_delete = len(self.individuals) - self.num_individuals
        self.individuals = sorted(self.individuals, key=lambda x: x.fitness, reverse=True)
        self.individuals = self.individuals[num_to_delete:]

    def update_best_individual(self):
        best = max(self.individuals, key=lambda x: x.fitness)
        if best.fitness > self.best_fitness:
            self.best_individual = best
            self.best_fitness = best.fitness
            print("New best individual found!", self.best_fitness)
            return True
        return False

    def print_head(self):
        for i in range(10):
            print(i, ":", self.individuals[i].fitness)