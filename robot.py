import pybullet as p
import pyrosim.pyrosim as pyro
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import os

class ROBOT:

    def __init__(self, id) -> None:
        self.id = id
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(id) + ".nndf")
        pyro.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain" + str(id) + ".nndf") 

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyro.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, index):
        for s in self.sensors:
            self.sensors[s].Get_Value(index)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyro.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, index):
        for m in self.motors:
            #self.motors[m].Set_Value(index, self.robotId)
            pass
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)
                #print("Neuron Name: " + str(neuronName))
                #print("Joint Name: " + jointName)
                #print("Target Angle: " + str(desiredAngle) + "\n\n")


    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        posOfLinkZero = stateOfLinkZero[0]
        xOfLinkZero = posOfLinkZero[0]
        f = open("tmp" + self.id + ".txt", "w")
        f.write(str(xOfLinkZero))
        f.close()
        os.rename("tmp"+str(self.id)+".txt" , "fitness"+str(self.id)+".txt")

