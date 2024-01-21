import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

hMod = 0
lMod = 0
wMod = 0
sMod = 1.0

for c in range (0, 5):
    for r in range (0, 5):
        for i in range (0, 10):
            pyrosim.Send_Cube(name="Box"+str(c)+"-"+str(r)+"-"+str(i), 
                              pos=[x+lMod,y+wMod,z+hMod] , 
                              size=[length*sMod,width*sMod,height*sMod])
            hMod = hMod + 1
            sMod = sMod * 0.9
        hMod = 0
        sMod = 1.0
        wMod = wMod + 1
    wMod = 0
    lMod = lMod + 1



pyrosim.End()
