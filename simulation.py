from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import time as t
import pyrosim.pyrosim as pyro
import pybullet_data


class SIMULATION:

    def __init__(self, directOrGUI) -> None:
        if(directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
            self.timescale = 0.0
        else:
            self.physicsClient = p.connect(p.GUI)
            self.timescale = c.timeStep
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.gravScaleX,c.gravScaleY,c.gravScaleZ)
        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range (0, c.duration):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            """backLegSensorValues[i] = pyro.Get_Touch_Sensor_Value_For_Link("BackLeg")
            frontLegSensorValues[i] = pyro.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            
            pyro.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = "Torso_FrontLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = FLtargetAngles[i],
                maxForce = c.maxMotorForce)"""
            t.sleep(self.timescale)

    def Get_Fitness(self):
        self.robot.Get_Fitness()