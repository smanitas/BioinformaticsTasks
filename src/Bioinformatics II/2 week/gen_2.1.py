"""
Code Challenge: Solve the Eulerian Cycle Problem.

         Input: The adjacency list of an Eulerian directed graph.
         Output: An Eulerian cycle in this graph.

 Sample Input:
0: 3
1: 0
2: 1 6
3: 2
4: 2
5: 4
6: 5 8
7: 9
8: 7
9: 6

Sample Output:
6 8 7 9 6 5 4 2 1 0 3 2 6
"""





def load_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            node, edges = line.strip().split(':')
            edges = [int(edge) for edge in edges.split()]
            adjacency_list[int(node)] = edges
    return adjacency_list


def find_eulerian_cycle(adj_list):
    total_edges = sum(len(adj_list[node]) for node in adj_list)
    stack = [0]
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

file_path = 'dataset_203_2.txt'  # Укажите путь к вашему файлу с данными
adjacency_list = load_adjacency_list(file_path)

eulerian_cycle = find_eulerian_cycle(adjacency_list)
if eulerian_cycle:
    print("Eulerian Cycle:")
    print(" ".join(str(node) for node in eulerian_cycle))
else:
    print("No Eulerian Cycle found.")