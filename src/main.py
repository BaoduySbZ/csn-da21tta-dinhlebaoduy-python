from queue import PriorityQueue

def greedy_best_first_search(start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put((heuristic(start), start))
    closed_set = set()

    while not open_set.empty():
        current_node = open_set.get()[1]

        print(f'Duyệt: {current_node}, Tọa Độ: {heuristic(current_node)}')

        if current_node == goal:
            return "Tìm kiếm thành công"

        closed_set.add(current_node)

        for neighbor in get_neighbors(current_node):
            if neighbor not in closed_set:
                open_set.put((heuristic(neighbor), neighbor))
                closed_set.add(neighbor)

    return "Tìm kiếm thất bại"


def heuristic(node):
     # heuristic: khoảng cách đến mục tiêu (giả sử các nút là thành phố)
     # chúng ta cần tùy chỉnh điều này dựa trên mọi vấn đề đã đặt ra

    distances = {
     # thêm khoảng cách cho các thành phố khác
     
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Dobreta': 242,
        'Eforie': 161,
        'Fagaras': 176,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 10,
        'Rimimicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374,
    }
    return distances[node]

def get_neighbors(node):
    

    neighbors = {
        'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
        'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimimicu Vilcea'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Craiova': ['Dobreta', 'Rimimicu Vilcea', 'Pitesti'],
        'Dobreta': ['Mehadia', 'Craiova'],
        'Eforie': ['Hirsova'],
        'Giurgiu': ['Bucharest'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Dobreta'],
        'Neamt': ['Iasi'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Pitesti': ['Rimimicu Vilcea', 'Craiova', 'Bucharest'],
        'Rimimicu Vilcea': ['Craiova', 'Sibiu', 'Pitesti'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Zerind': ['Arad', 'Oradea'],
        'Bucharest' : ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    }
    return neighbors[node]


start_node = 'Arad'
goal_node = 'Bucharest'
result = greedy_best_first_search(start_node, goal_node, heuristic)
print(result)
