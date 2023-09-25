import networkx as nx

def reconstruct_string(k, patterns):
    def Graph(patterns, k):
        graph = {}
        for string in patterns:
            prefix = string[:-1]
            suffix = string[1:]
            if prefix in graph:
                graph[prefix].append(suffix)
            else:
                graph[prefix] = [suffix]
        return graph

    G = nx.DiGraph(Graph(patterns, k))

    def EulerPath(G):
        nodes = list(G.nodes())
        for node in nodes:
            if G.in_degree(node) < G.out_degree(node):
                path = list(nx.dfs_edges(G, node))
                break

        string = path[0][0]
        for i in range(len(path)):
            string += path[i][1][-1]
        return string

    return EulerPath(G)

# Read input from file
with open('dataset_203_7.txt', 'r') as file:
    k = int(file.readline())
    patterns = file.readline().split()

# Reconstruct the string
result = reconstruct_string(k, patterns)

# Write output to file
with open('output.txt', 'w') as file:
    file.write(result)
