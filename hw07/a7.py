import matplotlib.pyplot as plt

########################
# PROBLEM 1
########################
def encode(msg, shift):
    """Encodes a message by shifting each letter in the message by a given amount
    
    (String, Number) -> String
    """
    
    # Define the alphabet and the special character '{' for space
    alph = "abcdefghijklmnopqrstuvwxyz{"  # '{' represents space
    encoded_msg = ""

    for i in msg:
        # Turn space into '{'
        if i == " ":
            encoded_msg += "{"
        # If the character is in the alphabet, apply shift
        elif i in alph:
            # Get the current index of the character
            index = alph.index(i)
            # Apply the shift with modulo to ensure wraparound
            new_index = (index + shift) % 27
            encoded_msg += alph[new_index]
        else:
            # Just append characters that aren't in the alphabet (e.g., punctuation)
            encoded_msg += i

    return encoded_msg


def decode(msg, shift):
    """Decodes a message by shifting each letter in the message back by a given amount
    
    (String, Number) -> String
    """
    
    # Define the alphabet and the special character '{' for space
    alph = "abcdefghijklmnopqrstuvwxyz{"  # '{' represents space
    decoded_msg = ""

    for i in msg:
        # Turn '{' back into a space
        if i == "{":
            decoded_msg += " "
        # If the character is in the alphabet, apply reverse shift
        elif i in alph:
            # Get the current index of the character
            index = alph.index(i)
            # Apply the reverse shift with modulo to ensure wraparound
            new_index = (index - shift) % 27
            decoded_msg += alph[new_index]
        else:
            # Just append characters that aren't in the alphabet (e.g., punctuation)
            decoded_msg += i

    return decoded_msg

########################
# PROBLEM 2
########################
def tiles(n, v, lst):
    """returns all valid combinations of tiles that sum up to n using values from v with the results flattened
    
    (Number, List, List) -> List of Lists
    """

    #flatten lst if elements are lists
    if len(lst) > 0 and type(lst[0]) == list:
        result = []

        #go through items in lst
        for item in lst:
            s = 0

            #sum elements in item
            for x in item:
                s = s + x

            result = tiles(n - s, v, item) + result

        return result

    #base case
    if n == 0:
        return [lst]
    
    #base case
    if n < 0:
        return []

    #list to store combinations
    output_list = []

    #main loop
    for i in v:
        output_list = tiles(n - i, v, lst + [i]) + output_list
        
    return output_list
            

########################
# PROBLEM 3
########################

def secdec_dec(n):
    """converts a base-17 number (with letters A-G representing values 10-16) to decimal
    
    (String) -> Number
    """

    #dictionary
    digits = { 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16 }

    #defining variables
    decimal_value = 0
    n = n.upper()

    #main for loop
    for i in range(len(n)):
        chars = n[-(i + 1)]

        #checks what the letter is
        if '0' <= chars <= '9':
            digit_value = int(chars)
        #use dictionary if letter
        else:
            digit_value = digits[chars]


        decimal_value += digit_value * (17 ** i)

    return decimal_value
            

########################
# PROBLEM 4
########################

def intersection(x, y):
    """returns a list of points that are in both lists x and y
    
    (List, List) -> List
    """
    result = []
    for i in x:
        if i in y:
            result.append(i)
    return result

def block_distance(p0, p1):
    """returns the city block distance between two points p0 and p1
    
    (Tuple, Tuple) -> Number
    """
    
    dist = 0
    if p0[0] > p1[0]:
        dist += p0[0] - p1[0]
    else:
        dist += p1[0] - p0[0]
    if p0[1] > p1[1]:
        dist += p0[1] - p1[1]
    else:
        dist += p1[1] - p0[1]
    return dist


def get_points(center, bd):
    """returns a list of points within a given city block distance from the center
    
    (Tuple, Number) -> List of Tuples
    """
    points = []
    for x in range(center[0] - bd, center[0] + bd + 1):
        for y in range(center[1] - bd, center[1] + bd + 1):
            if block_distance(center, (x, y)) <= bd:
                points.append((x, y))
    return points


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file,
    please put any print statements you want to try in
    this if statement.
    """

    #problem 1
data = ["abc xyz","the cat", "i love ctwohundred"]
for i,j in enumerate(data,start=2):
    print(f"original msg {j}")
    print(f"encoded  msg {encode(j,i)}")
    print(f"decoded  msg {decode(encode(j,i),i)}")

secret_msg = encode("the quick brown fox jumps over the lazy dog", 24)
print(secret_msg)
print(decode(secret_msg,24))

##    # Problem 2
##n = 6
##v = [1,2,3]
##print(tiles(n,v,[[i] for i in v]))
##for i in tiles(n,v,[[i] for i in v]):
##    print(sum(i), end="")
##
##n = 4
##v = [1,2]
##print(tiles(n,v,[[i] for i in v]))
##for i in tiles(n,v,[[i] for i in v]):
##    print(sum(i), end="")

    # problem 3
##data4 = ["G2","100","10","GA3","G","E2"]
##for d in data4:
##    print(secdec_dec(d), int(d,17))

    # Problem 4 
##    A = ((0,-1),2)
##    B = ((0,1),1)
##    C = ((4,4),1)
##    p = get_points(*A)
##    q = get_points(*B)
##    r = intersection(p,q)
##    s = get_points(*C)
##    t = intersection(s,q)
##
##    for points in p,q,r,s:
##        print(points)

    # # uncomment to see visualization
##    color = 'rgbmy'
##
##    for i,pts in enumerate([p,q,r,s,t]):
##        plt.plot([x for x,_ in pts],[y for _,y in pts],color[i] + 'o')
##
##    plt.gca().legend(("A: ((0,-1),2)", "B: ((0,1),1)", r"$\mathsf{A}\cap\mathsf{B}$","C: ((4,4),1)", r"$\mathsf{B}\cap\mathsf{C}$"))
##    plt.axis([-7, 7, -7, 7])
##    plt.grid()
##    plt.gca().set_aspect("equal")
##
##    plt.grid(True)
##    plt.title("City with square streets.")
##    plt.show()

print()
