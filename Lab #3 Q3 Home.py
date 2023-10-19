import math
length=int(input("Enter the length of the ladder: "))
angle=int(input("Enter the angle of the ladder: "))
ang_rad=(3.142*angle/180)
from math import sin
height_ladder=length*sin(angle)
print("The height of the ladder is: ",height_ladder)