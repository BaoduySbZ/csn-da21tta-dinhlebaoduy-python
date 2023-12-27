from queue import PriorityQueue
from collections import defaultdict

#khởi tạo một data set
data = defaultdict(list)
data['arad'] = ['sibiu', 'timisoara', 'zerind', 366]
data['sibiu'] = ['arad', 'fagaras', 'oradea', 'rimimicu vilcea', 253]
data['fagaras'] = ['sibiu', 'bucharest', 176]
data['craiova'] = ['dobreta', 'rimimicu Vilcea', 'pitesti', 160]
data['dobreta'] = ['mehadia', 'craiova', 242]
data['eforie'] = ['hirsova', 161]
data['giurgiu'] = ['bucharest', 77]
data['hirsova'] = ['urziceni', 'eforie', 151]
data['iasi'] = ['vaslui', 'neamt', 226]
data['lugoj'] = ['timisoara', 'mehadia', 244]
data['mehadia'] = ['lugoj', 'dobreta', 241]
data['neamt'] = ['iasi', 234]
data['oradea'] = ['zerind', 'sibiu', 380]
data['pitesti'] = ['rimimicu vilcea', 'craiova', 'bucharest', 10]
data['Rimimicu Vilcea'] = ['craiova', 'sibiu', 'pitesti', 193]
data['timisoara'] = ['arad', 'lugoj', 329]
data['urziceni'] = ['bucharest', 'vaslui', 'hirsova', 80]
data['vaslui'] = ['urziceni', 'iasi', 199]
data['zerind'] = ['arad', 'oradea', 374]
data['bucharest'] = ['fagaras', 'pitesti', 'giurgiu', 'urziceni', 0]

class note:
    
#hàm khởi tạo
    def __init__(self, name, par=None, h = 0): 
        self.name = name
        self.par = par
        self.h = h

#hàm hiển thị
    def display(self): 
        print(self.name, self.h)

#hàm so sánh, so sánh các nút với nhau.
    def __lt__(self, other):  
        if other is None:
            return False
        return self.h < other.h #duyệt nút nhỏ nhất.

#hàm kiểm tra xem đỉnh hiện tại có phải là đỉnh đích không.
def equal(O, G): #so sánh hai đỉnh O và G. Nếu tên của hai đỉnh này giống nhau, thì được coi là bằng nhau và hàm trả về True, ngược lại trả về False.
    if O.name == G.name:
        return True
    return False

#hàm kiểm tra xem một đỉnh nào đó đã tồn tại trong hàng đợi ưu tiên hay chưa.
def checkInPriority(tmp, c):
    if tmp is None:
        return False
    return tmp in c.queue

start = input("Nhập điểm bắt đầu: ")
goal = input("Nhập điểm đích: ")

S = note(name = start)
G = note(name = goal)

def GreedyBestFirstSearch(S, G):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
    while True:
        if Open.empty():
            print('tìm kiếm thất bại')
            return
        O = Open.get()
        Closed.put(O)
        print('duyệt:', O.name, O.h)
        if equal(O, G):
            print('tìm kiếm thành công')
            return

        i = 0
        while i < len(data[O.name]):
            if data[O.name]:  
                name = data[O.name][i]
                if data[name]:  
                    h = data[name][-1]

                    tmp = note(name=name, h=h)
                    tmp.par = O

                    ok1 = checkInPriority(tmp, Open)
                    ok2 = checkInPriority(tmp, Closed)

                    if not ok1 and not ok2:
                        Open.put(tmp)

                i += 1
            else:
                print(f"Danh sách data['{O.name}'] rỗng.")
                return
 

GreedyBestFirstSearch(S, G)
