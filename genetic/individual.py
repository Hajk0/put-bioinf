class Individual:
    def __init__(self, chromosome, sequence, coverage) -> None:
        self.chromosome = chromosome
        self.sequence = sequence
        self.fitness = self.calculate_fitness(coverage, len(sequence))

