#Futurevalue

def futurevalue():
        print("This is a program to predict the value of an investment in x amount of years. Please fill in the following values:")
        
        principal = eval(input("Enter the initial principal: "))
        apr = eval(input("Enter the apr: "))
        years = eval(input("Enter the amount of years you expect to keep the investment: 100"))
        
        for i in range(years):
            principal = principal * (1 + apr)
        print("The value in",years,"years is:", principal) 
futurevalue()
                    