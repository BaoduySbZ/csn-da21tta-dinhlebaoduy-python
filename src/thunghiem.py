from queue import PriorityQueue

def greedy_best_first_search(start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put((heuristic(start), start))
    closed_set = set()

    while not open_set.empty():
        current_node = open_set.get()[1]

        if current_node == goal:
            return "Path found"

        closed_set.add(current_node)

        for neighbor in get_neighbors(current_node):
            if neighbor not in closed_set:
                open_set.put((heuristic(neighbor), neighbor))
                closed_set.add(neighbor)

    return "No path found"

def heuristic(node):
    # Example heuristic: distance to goal (assuming nodes are cities)
    # You need to customize this based on your problem
    distances = {
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
        # ... add distances for other cities ...
    }
    return distances[node]

def get_neighbors(node):
    # Example: Return neighbors of a node (assuming nodes are cities)
    # You need to customize this based on your problem
    neighbors = {
        'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
        'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimimicu Vilcea'],
        'Fagaras':['Sibiu', 'Bucharest'],
        
        # ... add neighbors for other cities ...
    }
    return neighbors[node]

# Example usage
start_node = 'Arad'
goal_node = 'Bucharest'
result = greedy_best_first_search(start_node, goal_node, heuristic)
print(result)
