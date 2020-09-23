#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a=input("Enter value for a")
b=input("Enter value for b")
c=input("Enter value for c")

a=float(a)
b=float(b)
c=float(c)

answer= (c-b)/a
answer=float(answer)

print("x = " ,end="")
print(answer)
