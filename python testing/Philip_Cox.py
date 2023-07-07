#Calculator
import math

def main():
    print("1-Addition, 2-Subtraction, 3-Multiplication, 4-Division, 5-Square Root, 6-Exponent")
    print("DO NOT TYPE LETTERS!")
    operation = input("Type the number of an operation from the list and press enter: ")

  

    if int(operation) ==1:
        print("You chose Addition.")
        firstnumber = eval(input("What is the first number? "))
        secondnumber = eval(input("What is the second number? "))
        print("------")
        answer = firstnumber + secondnumber 
        print("The answer is:", answer)
        print("------")

    elif int(operation) ==2:
        print("You chose Subtraction.")
        firstnumber = eval(input("What is the first number? "))
        secondnumber = eval(input("What is the second number? "))
        print("------")
        answer = firstnumber - secondnumber 
        print("The answer is:", answer)
        print("------")

    elif int(operation) ==3:
        print("You chose Multiplication.")
        firstnumber = eval(input("What is the first number? "))
        secondnumber = eval(input("What is the second number? "))
        print("------")
        answer = firstnumber * secondnumber 
        print("The answer is:", answer)
        print("------")

    elif int(operation) ==4:
        print("You chose Division.")
        firstnumber = eval(input("What is the first number? "))
        secondnumber = eval(input("What is the second number? "))
        print("------")
        answer = firstnumber / secondnumber 
        print("The answer is:", answer)
        print("------")

    elif int(operation) ==5:
        print("You chose Sqaure Root.")
        firstnumber = eval(input("What is the first number? "))
        print("------")
        answer = math.sqrt(firstnumber)
        print("The answer is:", answer)
        print("------")

    elif int(operation) ==6:
        print("You chose Exponent.")
        firstnumber = eval(input("What is the first number? "))
        secondnumber = eval(input("What is the second number? "))
        print("------")
        answer = firstnumber ** secondnumber 
        print("The answer is:", answer)
        print("------")
    
    else:
        print("Please type a number from the list!")

    
    
    restart = input("Do you want to do another operation (Y/N)?")

    if restart =="Y":
        print("-------")
        print("-------")
        main()
    elif restart =="N":
        print("Ok, Goodbye!")
    else:
        print("Please type either Y or N!")


    
main()