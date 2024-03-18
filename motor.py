import numpy as np
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyro

class MOTOR:
    def __init__(self, j_n) -> None:
        self.jointName = j_n
        self.Prepare_Motor()

    def Prepare_Motor(self):
        self.values = np.zeros(c.duration)
        self.frequency = c.BLfrequency
        self.amplitude = c.BLamplitude
        self.phase = c.BLphaseOffset
        sinx = np.linspace(0, 2*np.pi, c.duration)
        if self.jointName == "Torso_BackLeg":
            self.target_angles = np.sin(self.frequency*sinx + self.phase) * self.amplitude
        else:
            self.target_angles = np.sin(self.frequency*sinx/2 + self.phase) * self.amplitude
        #np.save("data/" + self.jointName + "_targets", self.target_angles)

    def Set_Value(self, angle, id):
        pyro.Set_Motor_For_Joint(
                bodyIndex = id,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = angle,
                maxForce = c.maxMotorForce)
    