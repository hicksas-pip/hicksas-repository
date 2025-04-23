import math

############
# Problem 1
###########

class Queue:
    def __init__(self):
        self.q = []
    
    def empty(self):
        return len(self.q) == 0
    
    def enqueue(self,data):
        self.q.append(data)
    
    def dequeue(self):
        return self.q.pop(0)

    def __str__(self): 
        return str(self.q)

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self,pair):
        start, end = pair
        self.edges[start].append(end)

    def children(self, node):
        return self.edges[node]

    def nodes(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.edges)
    
    def bfs(self, queue, visited = []):
        """
        takes a queue of nodes and a list of visited nodes
        and returns a list of visited nodes using BFS

        Queue, list -> list
        """
        if queue.empty():
            return visited
        
        x = queue.dequeue()
        
        if x not in visited:
            visited.append(x)
            for y in self.children(x):
                if y not in visited:
                    queue.enqueue(y)
        
        return self.bfs(queue, visited)
    
############
# Problem 2
############
def hd(l1,l2):
    """
    takes two points (lat1, lon1), (lat2, lon2) and returns the
    distance in miles using the haversine formula

    tuple -> float
    """
    lat1 = math.radians(l1[0])
    lon1 = math.radians(l1[1])
    lat2 = math.radians(l2[0])
    lon2 = math.radians(l2[1])
    
    lat_diff = (lat2 - lat1) / 2
    lon_diff = (lon2 - lon1) / 2

    a = math.sin(lat_diff)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff)**2
    r = 3961
    d = 2 * r * math.asin(math.sqrt(a))
    
    return d

###########
# Problem 3
###########
def queue_it(bandAndSong, genres, q):
    """
    takes band and song info, and genre list, returns a queue of songs
    ordered by genre and listener count

    dict, list, Queue -> Queue
    """
    def get_listener_count(entry):
        return entry[1][1]

    for genre in genres:
        genre_songs = []
        for band in bandAndSong:
            for song in bandAndSong[band]:
                if song[2] == genre:
                    genre_songs.append([band, song])
        
        genre_songs.sort(key=get_listener_count, reverse=True)

        for item in genre_songs:
            q.enqueue(item)

    return q

#########
# Problem 4
#########
# Use the Stack Created in Lab11
class Stack:
    def __init__(self):
        self.s = []
    
    def pop(self):
        pass
    
    def push(self, item):
        pass

    def isEmpty(self):
        pass
    
    def peek(self):
        pass

    def __str__(self):
        return str(self.s)


def editor(lst):
    pass

########
# Problem 5
#######

def d(point, line):
    """
    takes a point (x', y') and a line (ax + by + c) and returns the 
    distance from the point to the line using the formula:

    tuple, tuple -> float
    """
    x_prime, y_prime = point
    a, b, c = line

    numerator = abs(a * x_prime + b * y_prime + c)
    denominator = math.sqrt(a**2 + b**2)
    
    distance = numerator / denominator
    
    return round(distance, 3)


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file,
    please put any print statements you want to try in
    this if statement.

    Make sure you comment all test cases when submitting to the
    autograder
    """


    ##### Problem 1 
    # nodes = [1,2,3,4,5,6,7,8]
    # g = Graph(nodes)
    # elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,7),(6,4)]
    # for e in elst:
    #     g.add_edge(e)
    
    # q = Queue()
    # q.enqueue(5)
    # print(g.bfs(q))


    ##### Problem 2
    #Lindley Hall 
    # south side of campus
    # l1 = (39.165341,-86.523588)
    #
    # #Luddy Hall
    # #on northside of campus
    # l2 = (39.172725,-86.523295)
    # print("haversine", hd(l1,l2), "mi")

    ##### Problem 3
    # genres = ["Pop", "Rock", "Jazz"]
    # bandAndSong = {"Beatles": [("Hey Jude", 100, "Pop"), ("Across the Universe", 200, 'Rock')],
    # "Queen": [("Bohemian Rhapsody", 300, "Pop"), ("Don't Stop Me Now", 150, "Rock")],
    # "Miles Davis": [("So What", 400, "Jazz"), ("Freddie Freeloader", 350, "Jazz")],
    # }
    # q = Queue()
    # songQueue = queue_it(bandAndSong, genres, q)
    # print(songQueue)
    # print(f"\nFirst Song: {songQueue.dequeue()}")
    # print(f"Second Song: {songQueue.dequeue()}")
    # print(f"Third Song: {songQueue.dequeue()}")


    ##### Problem 4
    # print(editor(["TYPE a", "TYPE b", "TYPE c", "UNDO", "UNDO", "REDO"]))  # ab
    # print(editor(["TYPE x", "TYPE y", "UNDO", "TYPE z", "REDO"]))          # xz
    # print(editor(["UNDO", "REDO", "TYPE a"]))                              # a
    # print(editor(["TYPE h", "TYPE i", "UNDO", "REDO", "TYPE !"]))          # hi!


    ###### Problem 5
    # line = (4,6,-26)
    # point = (2,-4)
    # print(d(point,line))
    # line = (3, 4, -10)
    # point = (1, 2)

    # print(d(point, line))
