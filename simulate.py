import pybullet as p
import time as t
import pyrosim.pyrosim as pyro
import numpy as numpy
import pybullet_data
import random

BLamplitude = numpy.pi/8
BLfrequency = 8
BLphaseOffset = 0

FLamplitude = numpy.pi/9
FLfrequency = 8
FLphaseOffset = numpy.pi/2

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyro.Prepare_To_Simulate(bodyID=robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

sinx = numpy.linspace(0, 2*numpy.pi, 1000)
BLtargetAngles = numpy.sin(BLfrequency*sinx + BLphaseOffset) * BLamplitude
FLtargetAngles = numpy.sin(FLfrequency*sinx + FLphaseOffset) * FLamplitude
#numpy.save("data/Fsins", FLtargetAngles)
#numpy.save("data/Bsins", BLtargetAngles)
#exit()

for i in range (0, 1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyro.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyro.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyro.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = BLtargetAngles[i],
        maxForce = 500)
    pyro.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = FLtargetAngles[i],
        maxForce = 500)
    t.sleep(0.016)
numpy.save("data/backleg_vals", backLegSensorValues)
numpy.save("data/frontleg_vals", frontLegSensorValues)
p.disconnect()
