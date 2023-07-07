#BMI 

output = ["Enter your ", "Please follow directions.", "Your BMI is "]


import math 

def main():
    print("This is a BMI calculator with inches and pounds.")
    print("To calculate your height in inches, multiply your feet x 12 and add the rest of the inches. For example, a 5'10 person would be 70 inches tall.")
    height = None
    weight = None

    while height is None:
        try:
             height = float(input(output[0] + "height: "))
        except ValueError:
            print(output[1])

    while weight is None:
        try:
             weight = float(input(output[0] + "weight: "))
        except ValueError:
            print(output[1])

    if height == 0:
        print("Nice try bucko.")
        print("Try again")
        exit()

    if weight == 0:
        print("Nice try bucko.")
        print("Try again")
        exit()



    bmi = 703 * weight // (height ** 2)

    

    print("------")
    print(output[2], bmi)
    print("------")
    print("The BMI says that you are underweight if your BMI is below 19, and you are healthy if you are 19 through 24. You are considered overweight if your BMI is 25 or above.")
    print("------")


main()

