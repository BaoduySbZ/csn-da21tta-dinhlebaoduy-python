from queue import PriorityQueue
from collections import defaultdict

data = defaultdict(list)
data['A'] = ['B', 'C', 'D', 6]
data['B'] = ['E', 'F', 3]
data['C'] = ['G', 'H', 4]
data['D'] = ['I', 'J', 5]
data['E'] = [3]
data['F'] = ['K', 'L', 'M', 1]
data['G'] = [6]
data['H'] = ['N', 'O', 2]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]

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

def BestFirstSearch(S=note(name='A'), G=note(name='N')):
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
            h = data[name][-1]

            tmp = note(name=name, h=h)
            tmp.par = O

            ok1 = checkInPriority(tmp, Open)
            ok2 = checkInPriority(tmp, Closed)

            if not ok1 and not ok2:
                Open.put(tmp)

            i += 1

# Test the code
BestFirstSearch()
