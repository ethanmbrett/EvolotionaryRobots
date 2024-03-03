import pybullet as p
import pyrosim.pyrosim as pyro
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self) -> None:
        self.robotId = p.loadURDF("body.urdf")
        pyro.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
            self.motors[m].Set_Value(index, self.robotId)