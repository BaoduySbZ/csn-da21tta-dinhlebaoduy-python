from queue import PriorityQueue
from collections import defaultdict

#khởi tạo một data set
#dùng hàm .extend() để thêm nhiều phần tử vào một danh sách.
data = defaultdict(list)
data['arad'].extend(['sibiu', 140, 'timisoara', 118, 'zerind', 75, 366]) 
data['sibiu'].extend(['arad', 140, 'fagaras', 99, 'oradea', 151, 'rimimicu vilcea', 80, 253]) 
data['fagaras'].extend(['sibiu', 99, 'bucharest', 211, 176]) 
data['craiova'].extend(['dobreta', 120, 'rimimicu Vilcea', 146, 'pitesti', 138, 160]) 
data['dobreta'].extend(['mehadia', 75, 'craiova', 120, 242]) 
data['eforie'].extend(['hirsova', 161]) 
data['giurgiu'].extend(['bucharest', 86, 77]) 
data['hirsova'].extend(['urziceni', 98, 'eforie', 86, 151]) 
data['iasi'].extend(['vaslui', 92, 'neamt', 87, 226]) 
data['lugoj'].extend(['timisoara', 111, 'mehadia', 70, 244]) 
data['mehadia'].extend(['lugoj', 70, 'dobreta', 75, 241]) 
data['neamt'].extend(['iasi', 87, 234]) 
data['oradea'].extend(['zerind', 71, 'sibiu', 151, 380]) 
data['pitesti'].extend(['rimimicu vilcea', 97, 'craiova', 138, 'bucharest', 101, 10]) 
data['Rimimicu Vilcea'].extend(['craiova', 146, 'sibiu', 80, 'pitesti', 97, 193]) 
data['timisoara'].extend(['arad', 118, 'lugoj', 111, 329]) 
data['urziceni'].extend(['bucharest', 85, 'vaslui', 142, 'hirsova', 98, 80]) 
data['vaslui'].extend(['urziceni', 142, 'iasi', 92, 199]) 
data['zerind'].extend(['arad', 75, 'oradea', 71, 374]) 
data['bucharest'].extend(['fagaras', 211, 'pitesti', 101, 'giurgiu', 90, 'urziceni', 85, 0]) 


class note:
    
#hàm khởi tạo
    def __init__(self, name, par = None, g = 0, h = 0): 
        self.name = name
        self.par = par
        self.g = g
        self.h = h

#hàm hiển thị
    def display(self): 
        print(self.name, self.g, self.h)

#hàm so sánh, so sánh các nút với nhau.
    def __lt__(self, other):  
        if other is None:
            return False
        return self.g + self.h < other.g + other.h #duyệt nút có chi phí nhỏ nhất.

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

def AStar(S, G):
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
        print('duyệt:', O.name, O.g, O.h)
        if equal(O, G):
            print('tìm kiếm thành công')
            return

        i = 0
        while i < len(data[O.name]):
            # kiểm tra danh sách có phần tử không
            if data[O.name]:  
                name = data[O.name][i]
                if data[name]:  
                    g =  O.g + data[O.name][i + 1]
                    h = data[name][-1]

                    tmp = note(name = name, g = g,  h = h)
                    tmp.par = O

                    ok1 = checkInPriority(tmp, Open)
                    ok2 = checkInPriority(tmp, Closed)

                    if not ok1 and not ok2:
                        Open.put(tmp)

                i += 2
            else:
                print(f"Danh sách data['{O.name}'] rỗng.")
                return

AStar(S, G)
