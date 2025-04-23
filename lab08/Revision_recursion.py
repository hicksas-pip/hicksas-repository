##Alex Hicks
##C200 / Spring 2025 
##lab08
##hicksas

def fibonacci(n):
    """
    Recursive function to return the nth number in the fibonacci sequence
    The fibonacci sequence is a series of numbers where each number is the sum of the two numbers before it (starting with 0, 1)
    So 0, 1, 1, 2, 3, 5, 8, 13...

    Input:
        n (integer >=0)
    
    Returns:
        int: nth number in fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    returnValue = fibonacci(n - 1) + fibonacci(n - 2)
    return returnValue

def fibonacci_tail(n):
    """
    Recursive function to return the nth number in the fibonacci sequence
    The fibonacci sequence is a series of numbers where each number is the sum of the two numbers before it (starting with 0, 1)
    So 0, 1, 1, 2, 3, 5, 8, 13...

    Input:
        n (integer >=0)
    
    Returns:
        int: nth number in fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    returnValue = fibonacci(n - 1) + fibonacci(n - 2)
    return returnValue


if __name__ == "__main__":
    #simple tests
    answers=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    print("~~~Testing recursive fibonacci~~~")
    for i in range(13):
        test=fibonacci(i)
        print(f"Your answer: {test} Correct Answer: {answers[i]} Same: {test==answers[i]}")

    print("\n~~~Testing tail recursive fibonacci~~~")
    for i in range(13):
        test=fibonacci_tail(i)
        print(f"Your answer: {test} Correct Answer: {answers[i]} Same: {test==answers[i]}")
