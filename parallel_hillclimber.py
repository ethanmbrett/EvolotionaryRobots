from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILLCLIMBER:
    def __init__(self) -> None:
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range (0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate (self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        #if (self.child.fitness > self.parent.fitness):
        #    self.parent = self.child
        for key in self.parents:
            if (self.children[key].fitness > self.parents[key].fitness):
                self.parents[key] = self.children[key]

    def Print(self):
        print("\n")
        for key in self.parents:
            print("PARENT FITNESS: " + str(self.parents[key].fitness) + " CHILD FITNESS: " + str(self.children[key].fitness))
        print("\n")

    def ShowBest(self):
        #self.parent.Evaluate("GUI")
        best = 0
        bestKey = 0
        for key in self.parents:
            if self.parents[key].fitness > best:
                best = self.parents[key].fitness
                bestKey = key
        self.parents[bestKey].start_sim("GUI")
        self.parents[bestKey].wait_for_sim()

    def Evaluate(self, solutions):
        for name in solutions:
            solutions[name].start_sim("DIRECT")
        for name in solutions:
            solutions[name].wait_for_sim()