from queue import PriorityQueue
from collections import defaultdict

data = defaultdict(list)
data['Arad'] = ['Sibiu', 'Timisoara', 'Zerind', 366]
data['Sibiu'] = ['Arad', 'Fagaras', 'Oradea', 'Rimimicu Vilcea', 253]
data['Fagaras'] = ['Sibiu', 'Bucharest', 176]
data['Zerind'] = ['Arad', 'Oradea', 374]
data['Timisoara'] = ['Arad', 'Lugoj', 329]
data['Lugoj'] = ['Timisoara', 'Mehadia', 244]
data['Mehadia'] = ['Lugoj', 'Dobreta', 241]
data['Dobreta'] = ['Mehadia', 'Craiova', 242]
data['Craiova'] = ['Dobreta', 'Rimimicu Vilcea', 'Pitesti', 160]
data['Rimimicu Vilcea'] = ['Craiova', 'Sibiu', 'Pitesti', 193]
data['Pitesti'] = ['Rimimicu Vilcea', 'Craiova', 'Bucharest', 10]
data['Bucharest'] = ['Giurgiu', 'Urziceni', 0]
data['Urziceni'] = ['Bucharest', 'Vaslui', 'Hirsova', 80]
data['Vaslui'] = ['Urziceni', 'Iasi', 199]
data['Iasi'] = ['Vaslui', 'Neamt', 226]
data['Neamt'] = ['Iasi', 234]
data['Hirsova'] = ['Urziceni', 'Eforie', 151]
data['Eforie'] = ['Hirsova', 161]
data['Giurgiu'] = ['Bucharest', 77]

class note:
    def __init__(self, name, par=None, h=0):
        self.name = name
        self.par = par
        self.h = h

    def display(self):
        print(self.name, self.h)

    def __lt__(self, other):
        if other is None:
            return False
        return self.h < other.h

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name

def equal(O, G):
    if O.name == G.name:
        return True
    return False

def checkInPriority(tmp, c):
    if tmp is None:
        return False
    return tmp in c.queue

def get_paths(O, distance):
    print(O.name, end=" ")
    distance += O.h
    if O.par is not None:
        get_paths(O.par, distance)
    else:
        print('distance:', distance)

# THU NGHIEM
def GreedyBestFirstSearch(S=note(name='Arad'), G=note(name='Bucharest')):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
    while True:
        if Open.empty():
            print('tim kiem that bai')
            return
        O = Open.get()
        Closed.put(O)
        print('duyet:', O.name, O.h)
        if equal(O, G):
            print('tim kiem thanh cong')
            distance = 0
            get_paths(O, distance)
            return

        i = 0
        while i < len(data[O.name]) - 1:
            name = data[O.name][i]
            if i + 1 < len(data[name]):
                h = data[name][-1]
                tmp = note(name=name, h=h)
                tmp.par = O

                ok1 = checkInPriority(tmp, Open)
                ok2 = checkInPriority(tmp, Closed)

                if not ok1 and not ok2:
                    Open.put(tmp)

            i += 1

# Test the code
GreedyBestFirstSearch()
