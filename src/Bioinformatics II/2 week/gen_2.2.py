"""
Code Challenge: Solve the Eulerian Path Problem.

    Input: The adjacency list of a directed graph that has an Eulerian path.
    Output: An Eulerian path in this graph.

Debug Datasets

Sample Input:
0: 2
1: 3
2: 1
3: 0 4
6: 3 7
7: 8
8: 9
9: 6

Sample Output:
6 7 8 9 6 3 0 2 1 3 4
"""

def load_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            node, edges = line.strip().split(':')
            edges = [int(edge) for edge in edges.split()]
            adjacency_list[int(node)] = edges
    return adjacency_list


def find_eulerian_path(adj_list):
    total_edges = sum(len(adj_list[node]) for node in adj_list)
    start_node = find_start_node(adj_list)
    stack = [start_node]
    path = []

    while stack:
        current_node = stack[-1]
        if adj_list[current_node]:
            next_node = adj_list[current_node].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())

    path.reverse()
    if len(path) == total_edges + 1:
        return path
    return None


def find_start_node(adj_list):
    in_degree = {}
    out_degree = {}

    for node in adj_list:
        out_degree[node] = len(adj_list[node])
        if node not in in_degree:
            in_degree[node] = 0

        for neighbor in adj_list[node]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 1
            else:
                in_degree[neighbor] += 1

            if neighbor not in out_degree:
                out_degree[neighbor] = 0

    start_node = None
    for node in adj_list:
        if in_degree[node] < out_degree[node]:
            return node
        else:
            start_node = node

    return start_node


file_path = 'dataset_203_6.txt'  # Укажите путь к вашему файлу с данными
adjacency_list = load_adjacency_list(file_path)

eulerian_path = find_eulerian_path(adjacency_list)
if eulerian_path:
    print("Eulerian Path:")
    print(" ".join(str(node) for node in eulerian_path))
else:
    print("No Eulerian Path found.")