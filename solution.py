import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time  as time

class SOLUTION:
    def __init__(self, ID) -> None:
        self.ID = ID
        self.weights = [[np.random.rand(), np.random.rand()],
                        [np.random.rand(), np.random.rand()],
                        [np.random.rand(), np.random.rand()]]
        for row in range(0, 3):
            for col in range(0, 2):
                self.weights[row][col] = self.weights[row][col] * 2 - 1

    def Evaluate(self, gOrD: str):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + gOrD + " " + str(self.ID))
        while not os.path.exists("fitness" + str(self.ID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.ID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()

    def start_sim(self, gOrD: str):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + gOrD + " " + str(self.ID))

    def wait_for_sim(self):
        while not os.path.exists("fitness" + str(self.ID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.ID) + ".txt", "r")
        self.fitness = float(f.read()) * -1
        f.close()
        os.system("del fitness" + str(self.ID) + ".txt")
        #print(self.fitness)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5], size=[1,1,1])
        pyrosim.End()
        return

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
        pyrosim.End()
        return

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.ID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range (0,3):
            for currentCol in range(0, 2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow,
                                      targetNeuronName = currentCol+3,
                                      weight = self.weights[currentRow][currentCol])
        pyrosim.End()
        return
    
    def Mutate(self):
        row = random.randint(0, 2)
        col = random.randint(0, 1)
        self.weights[row][col] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.ID = id