import random
import Game as myModule

POPULATION = 10
GENERATIONS = 10
NUM_OF_CHROMOSOMES = 10

chromosomes = [[0]*NUM_OF_CHROMOSOMES]*POPULATION

for y in range(POPULATION):
    for i in range(10):
        chromosomes[y][i] = random.randint(0,3)

    print(chromosomes[y])

game = myModule.Game([1,0,0,1,0,0,3,0,3,0])
print(game.runGame())

