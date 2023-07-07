#Quadratuc Equation

import math 

def main():
    print("This program finds the real solutions to a quadrtaic equation.")
    print("The eqaution has three coeffecients: a, b, and c. Please fill in each of these from the equation in question.")
    a = eval(input("Pleasse enter the coeffecient a: "))
    b = eval(input("Please enter the coeffecient b: "))
    c = eval(input("Please enter the coeffecient c: "))

    discroot = math.sqrt(b * b - 4 * a * c)
    root1 = ((-b + discroot) / (2 * a) )
    root2 = ((-b - discroot) / (2 * a) )
    print("-----------")

    print( "The solutions to this quadratuc equations are:", root1, root2)

    print("-----------")  

main()