def is_valid(v, pos, path, graph):
    # Check if vertex v can be added to the path
    if not graph[path[pos - 1]][v]:
        return False

    # Check if vertex v has already been visited
    if v in path[:pos]:
        return False

    return True


def hamiltonian_cycle_util(graph, pos, path):
    if pos == len(graph):
        # Check if the last vertex is connected to the starting vertex
        if graph[path[pos - 1]][path[0]]:
            return True
        else:
            return False

    # Try all vertices as the next vertex
    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v

            # Recursively find the Hamiltonian cycle
            if hamiltonian_cycle_util(graph, pos + 1, path):
                return True

            # Backtrack if the current vertex does not lead to a solution
            path[pos] = -1

    return False


def find_hamiltonian_cycles(graph):
    n = len(graph)

    # Create an array to store the path
    path = [-1] * n

    # Start from vertex 1
    path[0] = 1

    # Find the Hamiltonian cycles starting from vertex 1
    cycles = []
    hamiltonian_cycle_util(graph, 1, path)

    # Check if any Hamiltonian cycle was found
    for i, v in enumerate(path):
        if v == -1:
            break
        if i == n - 1 and graph[v][path[0]]:
            cycle = '>'.join(map(str, path + [path[0]]))
            cycles.append(cycle)

    return cycles


# Given adjacency list representation
adjacency_list = [
    [],
    [2, 3, 5],
    [4, 5],
    [1, 2, 5],
    [1, 3],
    [2, 4]
]

# Construct the adjacency matrix
num_vertices = len(adjacency_list)
graph = [[False] * num_vertices for _ in range(num_vertices)]
for i in range(1, num_vertices):
    for j in adjacency_list[i]:
        graph[i][j] = True

# Find and print all Hamiltonian cycles
cycles = find_hamiltonian_cycles(graph)
for cycle in cycles:
    print(cycle)