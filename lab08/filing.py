##Alex Hicks
##C200 / Spring 2025 
##lab08
##hicksas

import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()




def readingEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("/Users/ahick/OneDrive/C200/lab08/blank.txt", "r") as someFile:
        contents = someFile.read()
        return contents
    
def readingEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("/Users/ahick/OneDrive/C200/lab08/blank.txt", "r") as someFile:
        contents = someFile.readlines()
    print(contents)


def writeEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    stuff = ["a" ,"b","c","d"]
    with open("/Users/ahick/OneDrive/C200/wrong.txt", "w") as fileToWrite:
        for s in stuff:
            fileToWrite.write(s)


def writeEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("/Users/ahick/OneDrive/C200/lab08/wrong.txt", "w") as fileToWrite:
        for s in range(4):
            fileToWrite.write("more\n")



def FileIO_example(filePath, newFile): 
    '''
    Given a file path, we want to open the file, read each line and count
    the number of vocabs in each line. We will write to
    the newFile the lines that have more than 5 vocabs and clean them up
    (use strip). You are provided the path to the file we want to write.

    Return number of all lines that has less than or equal to 5 vocabs.
    '''
    count = 0
    with open(filePath) as theFile:
        origionalContents = theFile.read()

    splitted_lines = origionalContents.split("\n")

    goodLines = []

    for line in splitted_lines:
        splitted_vocabs = line.split(" ")
        if len(splitted_vocabs) <= 5:
            count += 1
        else:
            goodLines.append(line.strip())

    with open(newFile, "w") as toWrite:
        for line in goodLines:
            toWrite.write(line)
            toWrite.write("\n")
        return count
            


if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readex1 = readingEx1()
    print("~"*30)
    print(readex1, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    
    readex2 = readingEx2()
    print("~"*30)
    print(readex2, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    print()

    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(FileIO_example("/Users/ahick/OneDrive/C200/lab08/testing.data",
                                                    "/Users/ahick/OneDrive/C200/lab08/clean.txt")))

    
