def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] < s[j]:
            return False    

        i += 1
        j -= 1
    return True
        
print(is_palindrome("banana"))
print(is_palindrome("racecar"))


def unique_elements(lst):

    outputList = []

    for i in lst:
        if i not in outputList:
            outputList.append(i)

    return outputList

print(unique_elements([1,1,2,2,3,4,5,5,5,1,2,3,2,1]))


def sum_even_numbers(lst):

    even_numbers = []
    x = 0

    for i in lst:
        if (i % 2) == 0:
            even_numbers.append(i)

    for j in even_numbers:
        x += j

    return x

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))


def remove_duplicates(lst):

    outputList = []

    for i in lst:
        if i not in outputList:
            outputList.append(i)

    return outputList

print(remove_duplicates([1,1,2,2,3,4,5,5,5,1,2,3,2,1]))


def find_largest(lst):

    biggest = 0

    for n in lst:
        if n > biggest:
            biggest = n
    return biggest

    
print(find_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28976, 87654, 54657, 7865746, 97]))
    

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']

    n = 0

    for char in s:
        if char in vowels:
            n += 1
    return n
print(count_vowels("Hello World"))
print(count_vowels("hi omg blah blah blah"))


def unique_chars(s):

    used_chars = []

    for i in s:
        
        if i in used_chars:
            return False

        if i not in used_chars:
            used_chars.append(i)
            
    return True


print(unique_chars("abcdefg"))
print(unique_chars("hello"))
