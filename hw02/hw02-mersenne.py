def mersenne(n):
    """returns the mersenne number based off of the user inputted number (n)

    Number -> Number"""
    return(str((2**n) -1))

#asks for users inputs
x = int(input("Input your first number: "))
y = int(input("Input your second number: "))
z = int(input("Input your third number: "))

#prints results
print("Your Mersenne numbers are", mersenne(x), ",", mersenne(y), ", and", mersenne(z), ".")  


