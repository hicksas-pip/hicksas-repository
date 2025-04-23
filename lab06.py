def even_number(lst):
    '''
    Given a list of integer as an input, return a new list contains all integers in lst that are even number.
    
    input:
    lst - a list of integer numbers

    output:
    a new list contains all of the even numbers in the input list. 
    '''
    
    outputList = []
    
    for n in lst:
        if n%2 == 0:
            outputList.append(n)

    return outputList


def star_patern(n):
    '''
    given an integer n, write a function to print the bellow  
    note to do this operation you can't use the .append method for lists

    given n as an input, write a function that prints the bellow pattern:
    for example for n = 5:
    *
    **
    ***
    ****
    *****
    '''

    counter = 0
    star = "*"
    
    while counter < n :
        counter = counter + 1
        print(star * counter)
        

def print_num(n):
    '''
    given an input integer n, print numbers from n to 0 using while loops.

    for example for n = 5:
    5
    4
    3
    2
    1
    0

    input:
    n-integr number
    '''

    print(n)
    while n > 0 :
        n = n - 1
        print(n)


def dict_example(dict):
    '''
    we have a dict as an input that contains names of the candidate as a key 
    and the number of votes for that candidate as a value for that key. Please
    return the name of a peson who has the maximum votes.
    example:
    dict = {
        'john': 3
        'mike': 32
        'anna': 34
        'leo': 16
    }

    expected ouput: 'anna'
    '''
    largestKeyValue = max(dict, key = dict.get)
    return(largestKeyValue)


if __name__ == '__main__':
    # TODO:
    # implement testing
    print(even_number([3, 6, 2, 99, 32]))

    star_patern(5)

    print_num(5)

    dict = {
        'john': 3,
        'mike': 32,
        'anna': 34,
        'leo': 16 }
    print(dict_example(dict))
