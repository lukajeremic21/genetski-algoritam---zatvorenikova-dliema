import random
import time
from math import log

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
    population = [''.join(random.choices(['C', 'D'], k=10)) for _ in range(population_size)]
    return population

# Define a function to evaluate the fitness of each strategy
def evaluate_fitness(strategy, population):
    payoff = 0
    for opponent in population:
        my_move = strategy[random.randint(0, 9)]
        opponent_move = opponent[random.randint(0, 9)]
        payoff += payoff_matrix[my_move + opponent_move][0]
    return payoff

# Define a function to select the fittest individuals from the population
def selection(population, selection_rate):
    fitness_scores = [evaluate_fitness(strategy, population) for strategy in population]
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
    num_selected = int(selection_rate * len(population))
    selected_population = sorted_population[:num_selected]
    return selected_population

# Define a function to recombine two strategies to create a new one
def recombination(parent1, parent2):
    crossover_point = random.randint(0, 9)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Define a function to mutate a strategy
def mutation(strategy, mutation_probability):
    mutated_strategy = []
    mutation_counter = 0
    for bit in strategy:
        if random.random() < mutation_probability:
            bit = 'C' if bit == 'D' else 'D'
            mutation_counter += 1
        mutated_strategy.append(bit)
    return ''.join(mutated_strategy), mutation_counter

# Generate the initial population
population = generate_initial_population(POPULATION_SIZE)

# Evolve the population over multiple generations
start_time = time.time()
for generation in range(NUM_GENERATIONS):
    print('Generation:', generation+1)
    
    # Select the fittest individuals from the population
    selected_population = selection(population, SELECTION_RATE)
    
    # Create new individuals through recombination
    offspring_population = []
    for _ in range(POPULATION_SIZE - len(selected_population)):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        child = recombination(parent1, parent2)
        offspring_population.append(child)
    
    # Mutate some of the new individuals
    mutation_counter = 0
    for i in range(len(offspring_population)):
        offspring_population[i], counter = mutation(offspring_population[i], MUTATION_PROBABILITY)
        mutation_counter += counter
    
    # Combine the selected and offspring populations
    population = selected_population + offspring_population

end_time = time.time()

# Evaluate the fitness of the final population
fitness_scores = [evaluate_fitness(strategy, population) for strategy in population]

# Print the fittest strategy and its fitness score
fittest_index = fitness_scores.index(max(fitness_scores))
print('Fittest strategy:', population[fittest_index])
print('Fitness score:', fitness_scores[fittest_index])

# Print the number of mutations performed
print('Number of mutations:', mutation_counter)

# Print the time complexity
time_complexity = end_time - start_time
print('Time complexity:', time_complexity)

# Calculate and print the time complexity of each part

# Time complexity of generating the initial population: O(POPULATION_SIZE)
initial_population_time = POPULATION_SIZE
print('Time complexity of generating initial population:', initial_population_time)

# Time complexity of evaluating the fitness of each strategy in the evolution loop: O(POPULATION_SIZE^2)
fitness_evaluation_time = NUM_GENERATIONS * (POPULATION_SIZE ** 2)
print('Time complexity of evaluating fitness:', fitness_evaluation_time)

# Time complexity of selecting the fittest individuals: O(POPULATION_SIZE * log(POPULATION_SIZE))
selection_time = NUM_GENERATIONS * POPULATION_SIZE * log(POPULATION_SIZE)
print('Time complexity of selection:', selection_time)

# Time complexity of recombination: O(POPULATION_SIZE)
recombination_time = NUM_GENERATIONS * POPULATION_SIZE
print('Time complexity of recombination:', recombination_time)

# Time complexity of mutation: O(POPULATION_SIZE)
mutation_time = NUM_GENERATIONS * POPULATION_SIZE
print('Time complexity of mutation:', mutation_time)

# Time complexity of combining populations: O(POPULATION_SIZE)
combining_time = NUM_GENERATIONS * POPULATION_SIZE
print('Time complexity of combining populations:', combining_time)

# Time complexity of evaluating the fitness of the final population: O(POPULATION_SIZE^2)
final_fitness_evaluation_time = POPULATION_SIZE ** 2
print('Time complexity of evaluating fitness of the final population:', final_fitness_evaluation_time)
