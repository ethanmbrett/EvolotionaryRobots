import numpy as np
import constants as c
import pyrosim.pyrosim as pyro

class SENSOR:
    def __init__(self, l_n) -> None:
        self.linkName = l_n
        self.values = np.zeros(c.duration)

    def Get_Value(self, index):
        self.values[index] = pyro.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if (index >= c.duration - 1):
            print(self.values)
            #np.save("data/" + self.linkName + "_vals", self.values)
    