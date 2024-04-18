class Individual:
    def __init__(self, chromosome, text, coverage) -> None:
        self.chromosome = chromosome
        self.text = text
        self.fitness = self.calculate_fitness(coverage, len(text))

