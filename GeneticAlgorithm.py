import random
import Game as myModule

class GeneticAlgorithm:

    POPULATION = 10
    GENERATIONS = 1
    NUM_OF_CHROMOSOMES = 10

    tempLine = []

    chromosomes = [[0]*NUM_OF_CHROMOSOMES]*POPULATION
    parChromosome = [[0]*NUM_OF_CHROMOSOMES]*2
    fitness = [0]*NUM_OF_CHROMOSOMES

    game = myModule.Game()


    def __init__(self):
        self.generatePopulation()


    def generatePopulation(self):
        for y in range(0,self.POPULATION):
            for i in range(0,self.NUM_OF_CHROMOSOMES):
                self.chromosomes[y][i] = random.randint(0,3)
            self.fitness[y] = self.game.runGame(self.chromosomes[y])
            print(self.chromosomes[y], "  fitness: ", self.fitness[y], "   y: ", y)
        print()
        for a in range(10):
            print(self.chromosomes[a] , "   y: ", a)
        self.start(self.chromosomes)


    def start(self, chromosomes):
        for g in range(self.GENERATIONS):
            newChromosomes = [[0]*self.NUM_OF_CHROMOSOMES]*self.POPULATION

            for c in range(0,self.POPULATION-1,2):
                #selection             
                self.parChromosome[0] = chromosomes[random.randint(0,self.POPULATION-1)]
                self.parChromosome[1] = chromosomes[random.randint(0,self.POPULATION-1)]

                newChromosomes[c] = self.parChromosome[1]
                newChromosomes[c+1] = self.parChromosome[0]

                print()
                print(newChromosomes[c])
                print(newChromosomes[c+1])
                print()

                #crossover
                for f in range(0,1):
                    if(random.random() < 0.8):
                        crossPoint = random.randint(0,self.NUM_OF_CHROMOSOMES-1)
                        for i in range(0,self.NUM_OF_CHROMOSOMES-1):
                            if(i > crossPoint):
                                newChromosomes[c+f][i] = self.parChromosome[f][i]

                #mutation
            print()
            for c in range(self.POPULATION):
                print(newChromosomes[c])

            #Fill new population


ga = GeneticAlgorithm()




