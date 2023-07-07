#change counter

def main():
    print("Change Counter")
    print("Please enter the count of each coin type")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print("The total value of your change is: $",total)
    if total < 5.0:
        print("Looks like your broke.")

    if total > 5.0:
        print("Wow you are actually rich.")

    if total == 5.0:
        print("Wow right on $5, good job.")


main()