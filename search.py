import os
from parallel_hillclimber import PARALLEL_HILLCLIMBER

#for i in range (0, 5):
#    os.system("python generate.py")
#    os.system("python simulate.py")

hc = PARALLEL_HILLCLIMBER()
hc.Evolve()
hc.ShowBest()