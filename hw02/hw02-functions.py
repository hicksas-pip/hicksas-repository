def toThePower(x, y):
    """returns the value of x to the power of y
      
    Number,Number -> Number"""
    return(float((x**y)))

def quadruplicate(x):
    """returns a string consisting of four copies of a user input string
      
    String -> String"""
    return(str((x*4)))

def subtract(x,y):
    """finds the difference between to given numbers
      
    Number, Number -> Number"""
    return(x-y)

def multiplicate(x,y):
    """returns a string multiplied by a given number consisting of a user inputted string
      
    String, Number -> String"""
    return(str(x*y))

def mersenne(n):
    """returns the mersenne number based off of the user inputted number (n)

    Number -> Number"""
    return((2**n) -1)

def avgOfThree(x,y,z):
    """returns the average of three given numbers

    Number, Number, Number -> String"""
    return((x + y + z) / 3)

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def how_many_vowels(x):
    """takes a string and returns the number of vowels in the string

    String -> String"""
    index = 0
    counter = 0
    while index < len(x):
        if x[index] in 'aeiouAEIOU':
           counter += 1
        index += 1

    return counter

#avgOfThree user inputs and calculations
print("This program will calculate the force of three numbers")
d1 = int(input("Input your first number: "))
d2 = int(input("Input your second number: "))
d3 = int(input("Input your third number: "))
print("The average of your three numbers is:", str(avgOfThree(d1, d2, d3)))

    
