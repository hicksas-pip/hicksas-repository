def square(n):
    """returns the square of n
      
    Number -> Number"""
    return n*n

def square2(num):
  """returns the square of num
      
    Number -> Number"""    # defines the local variable num
  result = num * num       # defines the local variable result
  return result

def square3(num):
    """returns the square of num
      
    Number -> Number"""
    return num * num

result = 100
def square4(num):
    """returns the square of num
      
    Number -> Number"""
    result = num * num
    
    print("We're inside the function square4.")
    print("Here, the variable result has the value " + str(result))

    return result

print("Currently, the variable result has the value " + str(result))
print("We're about to call the function square4.")
print("square4(1.5) is " + str(square4(1.5)))
print("We've just finished calling square4.")
print("Now, result has the value " + str(result))

def double_dash(text):
    """returns input twice with a dash inbetween
      
    String -> String"""
    return text + "-" + text

# the following function takes a width, a height, and a depth and calculates
# the volume of a box with those dimensions.
# number, number, number -> number
def box_volume(width,height,depth):
    """returns the volume of a box given the inputs
      
    Number, Number, Number -> Number"""
    return width * height * depth
