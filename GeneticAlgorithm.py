import random
import Game as myModule

POPULATION = 10
GENERATIONS = 10
NUM_OF_CHROMOSOMES = 10

chromosomes = [[0]*NUM_OF_CHROMOSOMES]*POPULATION
fitness = [0]*NUM_OF_CHROMOSOMES

game = myModule.Game()

#Generate Population Chromosomes
for y in range(POPULATION):
    for i in range(10):
        chromosomes[y][i] = random.randint(0,3)
    fitness[y] = game.runGame(chromosomes[y])
    print(chromosomes[y], "  fitness: ", fitness[y])


for g in range(GENERATIONS):

    #selection


    #crossover


    #mutation


    #Fill new population



    
    
    
    
