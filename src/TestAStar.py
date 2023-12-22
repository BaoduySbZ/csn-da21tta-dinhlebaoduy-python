from queue import PriorityQueue

def a_star_search(start, goal, heuristic_costs, actual_costs):
    open_set = PriorityQueue()
    open_set.put((heuristic_costs[start] + actual_costs[start], start, actual_costs[start]))
    closed_set = set()

    while not open_set.empty():
        current_node = open_set.get()[1]

        print(f'Duyệt: {current_node}, Tọa độ: {actual_costs[current_node] + heuristic_costs[current_node]}')

        if current_node == goal:
            return "Tìm kiếm thành công"

        closed_set.add(current_node)

        for neighbor in get_neighbors(current_node):
            new_cost = actual_costs[current_node] + 1  # Giả sử chi phí từ một nút đến nút lân cận của nó là 1

            if neighbor not in closed_set:
                open_set.put((new_cost + heuristic_costs[neighbor], neighbor, new_cost))
                closed_set.add(neighbor)

    return "Tìm kiếm thất bại"

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


heuristic_costs = {
   
    
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


actual_costs = {

 
    'Arad': 0,
    'Sibiu': 140,
    'Timisoara': 118,
    'Zerind': 75,
    'Oradea': 146,
    'Fagaras': 239,
    'Rimimicu Vilcea': 220,
    'Pitesti': 317,
    'Craiova': 292,
    'Bucharest': 418,
    'Giurgiu': 90,
    'Urziceni': 414,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 509,
    'Iasi': 406,
    'Neamt': 563,
    'Lugoj': 229,
    'Mehadia': 299,
    'Dobreta': 242,
}

start_node = 'Arad'
goal_node = 'Bucharest'
result = a_star_search(start_node, goal_node, heuristic_costs, actual_costs)
print(result)
