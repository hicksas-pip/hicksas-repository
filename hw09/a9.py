import math

###############
# Problem 1
##############

class Vector:
    def __init__(self, *x):
        self.__v = x

    def __str__(self):
        return f"<{', '.join(str(i) for i in self.__v)}>"

    def get_tuple(self):
        """
        returns vector as tuple

        Vector -> tuple
        """
        return self.__v

    def __add__(self, other):
        """
        adds two vectors

        Vector -> Vector
        """
        return Vector(*[self.__v[i] + other.__v[i] for i in range(len(self.__v))])

    def __sub__(self, other):
        """
        subtracts two vectors

        Vector -> Vector
        """
        return Vector(*[self.__v[i] - other.__v[i] for i in range(len(self.__v))])

    def __mul__(self, other):
        """
        multiplies two vectors

        Vector -> int
        """
        return round(sum([self.__v[i] * other.__v[i] for i in range(len(self.__v))]), 3)

    def __rmul__(self, scalar):
        """
        multiplies scalar with vector

        int -> Vector
        """
        return Vector(*[scalar * i for i in self.__v])

    def __abs__(self):
        """
        returns magnitude of vector

        Vector -> float
        """
        return round(math.sqrt(sum(i * i for i in self.__v)), 3)

    def __neg__(self):
        """
        negates vector

        Vector -> Vector
        """
        return Vector(*[-i for i in self.__v])

    def __eq__(self, other):
        """
        checks if vectors are equal

        Vector -> bool
        """
        return self.__v == other.__v

################
# Problem 2
################

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class fraction:
    def __init__(self, x, y):
        self.n = x
        self.d = y
        self.reduce()

    def reduce(self):
        """
        reduces the fraction

        None -> None
        """
        g = gcd(abs(self.n), abs(self.d))
        self.n = self.n // g
        self.d = self.d // g
        if self.d < 0:
            self.n *= -1
            self.d *= -1
        # flip if numerator is negative and denominator is positive
        # but fraction like 50/-50 becomes 1/-1
        if self.n < 0 and self.d > 0 and abs(self.n) == abs(self.d):
            self.n = abs(self.n)
            self.d = -abs(self.d)

    def __str__(self):
        return f"({self.n}/{self.d})"

    def get_numerator(self):
        """
        gets numerator

        fraction -> int
        """
        return self.n

    def get_denominator(self):
        """
        gets denominator

        fraction -> int
        """
        return self.d

    def __add__(self, other):
        """
        adds two fractions

        fraction -> fraction
        """
        top = self.n * other.d + other.n * self.d
        bottom = self.d * other.d
        return fraction(top, bottom)

    def __mul__(self, other):
        """
        multiplies two fractions

        fraction -> fraction
        """
        top = self.n * other.n
        bottom = self.d * other.d
        return fraction(top, bottom)

################
# Problem 3
################

class MeansClass:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        """
        returns length of list

        list -> int
        """
        return len(self.lst)

    def arithmetic_mean(self):
        """
        returns arithmetic mean

        list -> float or str
        """
        if len(self) == 0:
            return "Data Error: 0 values"
        return sum(self.lst) / len(self)

    def geo_mean(self):
        """
        returns geometric mean

        list -> float or str
        """
        if len(self) == 0:
            return "Data Error: 0 values"
        s = sum([math.log10(i) for i in self.lst])
        return 10 ** (s / len(self))

    def har_mean(self):
        """
        returns harmonic mean

        list -> float or str
        """
        if len(self) == 0:
            return "Data Error: 0 values"
        if 0 in self.lst:
            return "Data Error: 0 in data"
        return len(self) / sum([1 / i for i in self.lst])

    def RMS_mean(self):
        """
        returns root mean square

        list -> float or str
        """
        if len(self) == 0:
            return "Data Error: 0 values"
        return math.sqrt(sum([i*i for i in self.lst]) / len(self))



################
# Problem 4
################
def c_2(n, k):
    if k == 0 or k == n:
        return 1
    return c_2(n-1, k-1) + c_2(n-1, k)

def B(n):
    """
    recursive function to compute B(n)

    int -> float
    """
    if n == 0:
        return 1
    return round(-1 * sum([c_2(n+1, k) * B(k) for k in range(n)]) / (n + 1), 14)

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file,
    please put any print statements you want to try in
    this if statement.

    Make sure you comment all test cases when submitting to the
    autograder
    """

    ######
    # Problem 1
    #####
    x,y,w = Vector(1,2), Vector(3,-1), Vector(*(10,10))  
    z,a = Vector(0,3,2),Vector(-1,-1,-1) 
    print(x,y,z,a)
    print(x+y,z+a)
    print(x*y,z*a)
    print(5*x,5*z)
    print(abs(x),abs(z))
    print(-x,-z)
    print(x - y + y == x, 2 * z == z + z)


    ######
    # Problem 2
    ######
    x = fraction(2*3*4,4*3*5)
    y = fraction(2*7,-7*2)
    z = fraction(-13,-14)
    a = fraction(-13*2*7,14)
    print(x, y, z, a)
    print(f"{x} + {y} == {x + y}")
    print(f"{x}*{y} == {x * y}")
    b,c = fraction(1,2),fraction(3,5)
    print(f"{b} + {c} == {b + c}")


    ######
    # Problem 3
    ######
    lst = [1,2,3,4]
    print(len(MeansClass(lst)))    
    print(MeansClass([]).arithmetic_mean())
    print(MeansClass([1,2,3]).arithmetic_mean())
    print(MeansClass([]).geo_mean())
    print(MeansClass([2,4,8]).geo_mean())
    print(MeansClass([]).har_mean())
    print(MeansClass([1,2,3]).har_mean())
    print(MeansClass([1,2,0]).har_mean())
    print(MeansClass([1,3,4,5,7]).RMS_mean())

    ######
    # Problem 4
    ######
    for i in range(6):
        print(f"B({i}) == {B(i)}")
    """
    Output:

    Do not uncomment below
    """
    # B(0) = 1
    # B(1) = -0.5
    # B(2) = 0.16666666666666666
    # B(3) = -0.0
    # B(4) = -0.033333333333333305
    # B(5) = -7.401486830834377e-17
