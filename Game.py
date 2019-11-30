class Game(object):

    def __init__(self, chromosomes):
        self.gameMap =[['I','X','X','X','X'],
                       ['I','I','X','X','X'],
                       ['X','I','I','X','X'],
                       ['X','X','I','X','X'],
                       ['X','I','I','X','X'],
                       ['X','I','X','X','X'],
                       ['I','I','X','X','X']]
        self.chromosomes = chromosomes
        self.fitness = 0
        self.currentY = 6
        self.currentX = 0
        self.currentPosition = 'I'


    def runGame(self):
        for i in range(0,10):
            if(self.chromosomes[i]==0):
                self.currentY = self.currentY - 1
            elif(self.chromosomes[i]==1):
                self.currentX = self.currentX + 1
            elif(self.chromosomes[i]==2):
                self.currentY = self.currentY + 1
            elif(self.chromosomes[i]==3):
                self.currentX = self.currentX - 1
            else:
                return '!'
            
            self.currentPosition = self.gameMap[self.currentY][self.currentX]
            self.fitness += 1
            #print(self.currentPosition)
            if(self.currentY > 6 or self.currentX > 4 or self.currentY < 0 or self.currentX < 0):
                return '!'
            elif(self.currentPosition == 'X'):
                break
        return self.fitness
