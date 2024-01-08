from queue import PriorityQueue
from collections import defaultdict

#khởi tạo một data set
data = defaultdict(list)
data['tien giang'] = ['long an', 'dong thap', 'vinh long', 'ben tre', 74]
data['ben tre'] = ['vinh long', 'tra vinh', 'tien giang', 34]
data['vinh long'] = ['dong thap', 'tien giang', 'tra vinh', 'ben tre', 'can tho', 54]
data['dong thap'] = ['vinh long', 'tien giang', 'long an', 'can tho', 'an giang', 123]
data['an giang'] = ['dong thap', 'can tho', 'kien giang', 111]
data['can tho'] = ['an giang', 'dong thap', 'kien giang', 'hau giang', 'vinh long', 62]
data['kien giang'] = ['can tho', 'an giang', 'hau giang', 'ca mau', 'bac lieu', 120]
data['ca mau'] = ['kien giang', 'bac lieu', 155]
data['bac lieu'] = ['ca mau', 'kien giang', 'hau giang', 'soc trang', 99]
data['soc trang'] = ['bac lieu', 'hau giang', 'tra vinh', 56]
data['long an'] = ['dong thap', 'tien giang', 74]
data['hau giang'] = ['can tho', 'kien giang', 'bac lieu', 'soc trang', 96]
data['tra vinh'] = ['vinh long', 'ben tre', 'soc trang', 0]

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
