#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi
# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 84.8230016469

import math
Fsphere= "V=(4/3)math.pi*r**3"
print("The volume of the sphere is"+ Fsphere)
radius= input("Enter the radius of the sphere")
radius=float(radius)
Vsphere= 4/3*math.pi*radius**3
print(Vsphere)