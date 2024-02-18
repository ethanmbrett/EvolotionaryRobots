import pybullet as p
import time as t
import pyrosim.pyrosim as pyro
import numpy as numpy
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyro.Prepare_To_Simulate(bodyID=robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

for i in range (0, 1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyro.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyro.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    t.sleep(0.016)
numpy.save("data/backleg_vals", backLegSensorValues)
numpy.save("data/frontleg_vals", frontLegSensorValues)
p.disconnect()
