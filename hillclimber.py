from solution import SOLUTION
import constants as c
import copy

class HILLCLIMBER:
    def __init__(self) -> None:
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate (self):
        self.child.Mutate()
        print("\n")
        #print("PARENT WEIGHTS: " + str(self.parent.weights))
        #print("CHILD WEIGHTS: " + str(self.child.weights))

    def Select(self):
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child

    def Print(self):
        print("\nPARENT FITNESS: " + str(self.parent.fitness) + " CHILD FITNESS " + str(self.child.fitness))

    def ShowBest(self):
        self.parent.Evaluate("GUI")