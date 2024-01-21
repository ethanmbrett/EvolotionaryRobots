import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for i in range (0, 2000):
    p.stepSimulation()
    t.sleep(0.016)
    print (i)
p.disconnect()
