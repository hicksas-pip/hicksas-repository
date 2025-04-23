import math

########################
# PROBLEM 1
######################## 
def s(n):
    """Returns the sum of all numbers from 0 to n

    Number -> Number
    """

    if n == 0:
        returnValue = 0
        return returnValue

    returnValue = n + s(n - 1)
    return returnValue


ds1 = {}
def s_memo(n):
    """Returns the sum of all numbers from 0 to n using memoization

    Number -> Number
    """
    
    if n in ds1:
        return ds1[n]
    
    if n == 0:
        ds1[n] = 0
        
    else:
        ds1[n] = n + s_memo(n - 1)
        
    return ds1[n]

def p(n):
    """Returns the population value after n steps, growing by 2% per step from 10,000

    Number -> Number
    """
    if n == 0:
        return 10000

    returnValue = p(n - 1) * 1.02
    return returnValue


def p_tail(n, acc=10000):
    """Returns the population value after n steps using tail recursion

    Number, Number -> Number
    """

    if n == 0:
        return acc

    returnValue = p_tail(n - 1, acc * 1.02)
    return returnValue

def c(n):
    """Returns the value calculated using the formula c(n) = 9 * c(n-1) + 10^(n-1) - c(n-1)

    Number -> Number
    """

    if n == 1:
        return 9

    returnValue = 9 * c(n - 1) + 10 ** (n - 1) - c(n - 1)
    return returnValue

def c_tail(n, acc1=9, acc2=0):
    """Returns the value of c(n) using tail recursion

    Number, Number -> Number
    """

    if n == 1:
        return acc1

    returnValue = c_tail(n - 1, 9 * acc1 + 10 ** (n - 1) - acc1)
    return returnValue

def c_while(n):
    """Returns the value of c(n) using a while loop instead of recursion

    Number -> Number
    """

    acc = 9
    i = 2

    while i <= n:
        acc = 9 * acc + 10 ** (i - 1) - acc
        i += 1

    return acc
    
########################
# PROBLEM 2
########################
def m(lst):
    """Makes a pyramid by adding pairs of numbers.
    
    List -> List
    """

    new_lst = []
    
    if len(lst) < 2:
        return []
    
    
    for i in range(len(lst) - 1):
        new_lst.append(lst[i] + lst[i + 1])
    
    return [new_lst] + m(new_lst)

########################
# PROBLEM 3
########################
def d_1(x, y):
    """Finds the biggest number that divides both x and y.
    
    int, int -> int
    """
    
    if x == 1:
        return 1
    
    if x == 0:
        return y

    returnValue = d_1(y % x, x)
    return returnValue

def e_1(x, y):
    """Uses d_1 to find a special number from x and y.
    
    int, int -> int
    """
    
    z = d_1(x, y)
    
    if z == 1:
        return x * y

    returnValue = z * e_1(x // z, y // z)
    return returnValue

########################
# PROBLEM 4
########################
def dollars(tot):
    """Takes an amount in dollars and returns the fewest number of coins.
    
    Float -> List
    """
    
    tot = round(tot * 100)
    
    q = tot // 25
    tot = tot % 25
    
    d = tot // 10
    tot = tot % 10
    
    n = tot // 5
    tot = tot % 5
    
    p = tot

    returnValue = [q, d, n, p]
    return returnValue

########################
# PROBLEM 5
########################
def D(f):
    """Returns the derivative of the function f using a small value h."""
    
    h = 0.00001

    returnValue = lambda x: (f(x + h) - f(x - h)) / (2 * h)
    return returnValue 

def newton(f, x, tau):
    """Finds the root of the function f starting from the initial guess x."""
    
    fx = f(x)
    dfx = D(f)(x)
    
    if abs(fx) <= tau:
        return x
    
    x_new = x - fx / dfx

    returnValue = newton(f, x_new, tau)
    return returnValue

########################
# PROBLEM 6
########################
def prime(p):
    """Checks if p is prime. A prime number can only be divided by 1 and itself.
    
    Integer -> Boolean
    """
    
    if p == 2:
        return True
    
    if p < 2 or p % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(p)) + 1, 2):

        if p % i == 0:
            return False

        
    return True

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    ## Problem 1
for i in range(4):
    print(f"n = {i}")
    print(f"s(n) = {s(i)} s_memo(n) = {s_memo(i)}")
    print(f"p(n) = {p(i)} p_tail(n) = {p_tail(i)}")
print()
for i in range(1,5):
    print(f"n = {i}")
    print(f"c(n) = {c(i)} c_tail(n) = {c_tail(i)} c_while(n) = {c_while(i)}")

    ## Problem 2
x = [[1,2,3,4,5], [1], [3,4], [5,10,22], [1,2,3,4,5,6]]
for i in x:
    print(m(i))

    ## Problem 3
data = [[15,25], [6,7], [1,1], [1,2],[0,4], [210, 2310]]
for i in data:
    print(e_1(*i))

    ## Problem 4
data5 = [2.24,1.19,4.16,1.01,1.10,2.00]
for i in data5:
    print(dollars(i))


    ## Problem 5
p1 = [[lambda x:x**2 - 2, 100],[lambda x:x**6-x-1,1.5], [lambda x:x**3-(100*(x**2))-x + 100,0]]
tau = 0.0001

for f,g in p1:
    root = newton(f,g,tau)
    print(root,f(root))


    # #problem 6
ps = []
for p in range(2,100):
    if prime(p):
        ps.append(p)
        print(ps)

    print()
