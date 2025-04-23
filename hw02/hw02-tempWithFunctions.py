#Celsius to fahrehneit and fahrehneit to celsius function definitions
def CtoF(n):
    """takes a temperature in fahrehneit and converts to celsius

    Number -> Number"""
    return((9/5)*(n) +32)

def FtoC(n):
    """takes a temperature in celsius and converts to fahrehneit

    Number -> Number"""
    return((n-32)*(9/5))


#user inputs the temperature
userInput = int(input("Please enter a temperature: "))
#prints out the calculations
print("The converted temperature is:")
print(str(userInput), "Fahrehneit ->", FtoC(userInput), "Celsius") 
print(str(userInput), "Celsius ->", CtoF(userInput), "Fahrehneit") 
