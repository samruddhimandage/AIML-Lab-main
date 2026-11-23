

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 2},
    'F': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 0
}


def a_star(start, goal):

    open_list = [start]

    cost = {
        start: 0
    }

    while open_list:

        # Assume first node is the best
        current = open_list[0]

        # Find node with lowest f(n) = g(n) + h(n)
        for node in open_list:
            if cost[node] + heuristic[node] < cost[current] + heuristic[current]:
                current = node

        # Check if goal is reached
        if current == goal:
            print("Goal Reached")
            print("Cost =", cost[current])
            return

        # Remove current node from open list
        open_list.remove(current)

        # Check all neighbours
        for neighbor in graph[current]:

            new_cost = cost[current] + graph[current][neighbor]

            # If neighbour is new OR we found a cheaper path
            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                if neighbor not in open_list:
                    open_list.append(neighbor)


a_star('A', 'F')
     
