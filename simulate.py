import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)
for i in range (0, 1000):
    p.stepSimulation()
    t.sleep(0.016)
    print (i)
p.disconnect()
