from individual import Individual
from population import Population
from generator import Generator


def crossover_test():
    generator = Generator("../data/sequences_negative.txt", 209)
    individual_data = generator.generate_individual()
    individual_data_2 = generator.generate_individual()
    individual = Individual(individual_data[1], individual_data[0], individual_data[2], 209)
    other_individual = Individual(individual_data_2[1], individual_data_2[0], individual_data_2[2], 209)
    print("Parent 1:", individual)
    print("Parent 2:", other_individual)
    print("Crossover:", end='')
    new_individual = individual.crossover(other_individual)
    print(new_individual)

#"../data/sequences_negative.txt"
#"../data/sequences_positive.txt"
#"../data/sequences_negative_long.txt"
def population_test():
    population = Population(100, "../data/sequences_positive.txt", 209, random_probability=0.1)
    population.evolve2(generations=100000, selection_rate=0.65, mutation_rate_individual=0.001, mutation_rate_gene=1, skip_best=5)
    print("Best individual:", population.best_individual)

def population():
    population = Population(500, "../data/sequences_positive.txt", 209, random_probability=0.1)
    population.evolve_if_progress(generations=10000, selection_rate=0.3, mutation_rate_individual=0.001, mutation_rate_gene=1, skip_best=5)
    print("Best individual:", population.best_individual)

if __name__ == "__main__":
    # crossover_test()
    # population_test()
    population()