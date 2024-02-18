import numpy as np
import matplotlib.pyplot as mp

backlegSensorValues = np.load("data/backleg_vals.npy")
frontlegSensorValues = np.load("data/frontleg_vals.npy")
mp.plot(backlegSensorValues, label="Back Leg", linewidth = 3)
mp.plot(frontlegSensorValues, label="Front Leg", linewidth = 1)
mp.legend()
mp.show()