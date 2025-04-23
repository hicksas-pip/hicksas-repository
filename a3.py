# We have added import math
import math

# Problem 1
#input radius r, height h
#return volume

pi = math.pi
def cone_volume(radius,height):
    """returns the volume of a cone given the radius and height 

    Number,Number -> Number"""
    volume = round(((1/3) * pi * (radius**2) * height), 2)
    return(volume)


# Problem 2
#input t hours
#return percent watching tv
def tv_watching_percent(hours_past_4pm):
    """returns the percent watching tv given how many hours watched past 4pm

    Number -> Number"""
    percent = round( ((hours_past_4pm / 8) * 100) , 2)
    return(percent)

# Problem 3
#input number of susceptible, but healthy children
#output number of the infected children
# use math.ceil() before returning your final answer.
def infected_children(susceptible_children):
    """takes the number of susceptible children and returns the number of infected children

    Number -> Number"""
    infected = (192 * (math.log(susceptible_children / 762 , 2)) - susceptible_children + 763)
    infected = math.ceil(infected)
    return(infected)


# Problem 4
#input months t=0,...,11
#output items sold x 1000
def sales_model(months):
    """takes the number of months and returns the number of items sold x 1000

    Number -> Number"""
    ducks = math.floor( 532 / ( 1 + 869 * math.exp(-1.33 * months)) ) 
    ducks = math.ceil(ducks)
    return(ducks)


# Problem 5
#input time seconds
#output feet
def height(seconds):
    """takes the number of seconds and returns the height fallen in feet

    Number -> Number"""
    height = (-16 * (seconds ** 2) + (64 * seconds) + 80)
    height = round(height, 2)
    return(height)

# Problem 6
#input coefficients for quadratic and value
#output True if value is root, False otherwise
def quad(a,b,c,x):
    """takes the  coefficients for quadratic and value and returns True if value is root, False otherwise

    Number, Number, Number, Number -> Number"""
    q_func = (a * (x ** 2)) + (b * x) + c
    return(q_func == 0)

# Problem 7
#input P principle, n times per year, t years, r rate
#output dollars
def R(principle,rate,times_per_year,years):
    """takes the principle, rate, times_per_year, and years and returns money in dollars

    Number, Number, Number, Number -> Number"""
    fund = principle * math.floor(((1 + (rate / times_per_year)) ** (times_per_year * years) - 1) / (rate / times_per_year))
    fund = round(fund, 2)
    return(fund)


#Problem 8
#input dimensions w,l,h for width, length, height of a
# rectangular solid
#output total surface area
def surface_area(width,length,height):
    """takes the dimensions w,l,h for width, length, height of a rectangular solid and returns total surface area

    Number, Number, Number -> Number"""
    surface =  2 * (length * width + width * height + height * length)
    return(surface)

#problem 9
#input temperature (F), wind speed (mph)
#output wind chill
def T_wc(temp,wind_speed):
    """takes the temperature (F), wind speed (mph) and returns the wind chill

    Number -> Number"""
    wc = math.floor((35.74 + (0.6215 * temp)) - ((35.75 * (wind_speed ** .16)) + ((0.4275 * temp * (wind_speed ** .16)))))
    return(wc)

#problem 10
#input sphere volune
#output radius of the sphere
def volume_to_radius(volume):
    """takes the sphere volune and returns the radius of the sphere

    Number -> Number"""
    vol = math.cbrt((3 * volume)/(4 * pi))
    vol = round(vol,2)
    return(vol)

def side_max_square(v):
    """takes the sphere volune and returns the side of the largest cube inscribed

    Number -> Number"""
    vol2 = (2 / (math.sqrt(3)))
    f_vol = volume_to_radius(v) * vol2
    f_vol = round(f_vol,2)
    return(f_vol)

#problem 11
#input list of market prices per share
#output a tuple containing average price and the last price
def app(market):
    """takes the list of market prices per share and returns a tuple containing average price and the last price

    list -> Number, Number"""
    avg = round(sum(market) / len(market) , 2)
    last = market[-1]
    return(avg,last)


if __name__ == "__main__":
    """
    The following tests are given by us. For example, after completing problem 1,
    you can uncomment the tests for problem 1 and run the a1.py file to see the output.
    Similarly, you can uncomment the tests for other problems as you complete them.

    If you want to do some of your own testing, you can also add them, for example if you want to
    test problem 1 then you can add another print statement and call c() function with your own
    input value to see the output of c() on that value -- print(c(5, 7)) or print(c(4, 47)) etc.

    Please remember to comment the test cases before submitting to the Autograder. You can use them
    as long as you want while testing on your system, but please comment the below test cases before
    submitting to the Autograder.
    """


    #problem 1
    #volume of cone
    # print(cone_volume(2,5))
    # print(cone_volume(3,7))

    #problem 2
    #tv watching
    # print(tv_watching_percent(0))
    # print(tv_watching_percent(3))
    # print(tv_watching_percent(8))

    #problem 3
    #flu outbreak
    # S_6 = 100
    # print(infected_children(S_6))
    # S_6 = 300
    # print(infected_children(S_6))

    #problem 4
    # print(sales_model(0))
    # print(sales_model(5))
    # print(sales_model(10))

    #problem 5
    # print(height(5))

    #problem 6
    #quadratic roots
    # print(quad(2,5,-12,-4))
    # print(quad(2,5,-12,3/2))
    # print(quad(2,5,-12,1))

    # problem 7
    # Sinking Fund
    # P = 22000
    # n = 1
    # t = 7
    # r = 6/100
    # print(R(P,r,n,t))
    # P = 500
    # n = 12
    # t = 20
    # r = 4/100
    # print(R(P,r,n,t))
    # P = 1200
    # n = 4
    # t = 10
    # r = 8/100
    # print(R(P,r,n,t))

    #problem 8
    #make your own inputs/outputs

    #problem 9
    # temp_15, wind_speed_15 = 2, 5
    # print(T_wc(temp_15, wind_speed_15))

    #problem 10
    # v = 268.08
    # print(volume_to_radius(v), side_max_square(v))

    #problem 11
    # market = [40 ,35 ,34 ,38 ,50]
    # print(app(market))
