import random

# Define the payoff matrix for the game
payoff_matrix = {'CC': (3, 3), 'CD': (0, 5), 'DC': (5, 0), 'DD': (1, 1)}

# Define the population size and the number of generations
POPULATION_SIZE = 100
NUM_GENERATIONS = 50

# Define the mutation probability and the selection rate
MUTATION_PROBABILITY = 0.1
SELECTION_RATE = 0.5

# Define the initial population as a list of strategies
def generate_initial_population(population_size):
    population = []
    for i in range(population_size):
        strategy = ''.join(random.choices(['C', 'D'], k=10))
        population.append(strategy)
    return population

# Define a function to evaluate the fitness of each strategy
def evaluate_fitness(strategy):
    payoff = 0
    for opponent in population:
        my_move = strategy[random.randint(0, 9)]
        opponent_move = opponent[random.randint(0, 9)]
        payoff += payoff_matrix[my_move + opponent_move][0]
    return payoff

# Define a function to select the fittest individuals from the population
def selection(population, selection_rate):
    fitness_scores = [evaluate_fitness(strategy) for strategy in population]
    sorted_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k], reverse=True)
    num_selected = int(selection_rate * len(population))
    selected_indices = sorted_indices[:num_selected]
    selected_population = [population[i] for i in selected_indices]
    return selected_population

# Define a function to recombine two strategies to create a new one
def recombination(parent1, parent2):
    crossover_point = random.randint(0, 9)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Define a function to mutate a strategy
def mutation(strategy, mutation_probability):
    mutated_strategy = ''
    for bit in strategy:
        if random.random() < mutation_probability:
            mutated_strategy += 'C' if bit == 'D' else 'D'
        else:
            mutated_strategy += bit
    return mutated_strategy

# Generate the initial population
population = generate_initial_population(POPULATION_SIZE)

# Evolve the population over multiple generations
for generation in range(NUM_GENERATIONS):
    print('Generation:', generation+1)
    
    # Select the fittest individuals from the population
    selected_population = selection(population, SELECTION_RATE)
    
    # Create new individuals through recombination
    offspring_population = []
    for i in range(POPULATION_SIZE - len(selected_population)):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        child = recombination(parent1, parent2)
        offspring_population.append(child)
    
    # Mutate some of the new individuals
    for i in range(len(offspring_population)):
        offspring_population[i] = mutation(offspring_population[i], MUTATION_PROBABILITY)
    
    # Combine the selected and offspring populations
    population = selected_population + offspring_population

# Evaluate the fitness of the final population
fitness_scores = [evaluate_fitness(strategy) for strategy in population]

# Print the fittest strategy and its fitness score
fittest_index = max(range(len(fitness_scores)), key=fitness_scores.__getitem__)
print('Fittest strategy:', population[fittest_index])
print('Fitness score:', fitness_scores[fittest_index])
