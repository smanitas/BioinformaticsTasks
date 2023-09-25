import collections

def reconstruct_string(k, d, paired_reads):
    def create_debruijn_graph(paired_reads, k):
        graph = {}
        for pair in paired_reads:
            kmer1, kmer2 = pair.split('|')
            prefix = kmer1[:k - 1] + '|' + kmer2[:k - 1]
            suffix = kmer1[1:] + '|' + kmer2[1:]
            if prefix in graph:
                graph[prefix].append(suffix)
            else:
                graph[prefix] = [suffix]
        return graph

    def eulerian_path(graph):
        indegree = collections.defaultdict(int)
        outdegree = collections.defaultdict(int)
        for node in graph:
            if graph[node]:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
                    outdegree[node] += 1

        start_node = None
        for node in indegree:
            if indegree[node] < outdegree[node]:
                start_node = node
                break

        path = []
        stack = [start_node]

        while stack:
            current_node = stack[-1]
            if graph[current_node]:
                next_node = graph[current_node].pop()
                stack.append(next_node)
            else:
                path.append(stack.pop())

        path.reverse()
        return path

    def string_spelled_by_gapped_patterns(patterns, k, d):
        prefixes = [pattern.split('|')[0] for pattern in patterns]
        suffixes = [pattern.split('|')[1] for pattern in patterns]

        prefix_string = prefixes[0] + ''.join([pattern[-1] for pattern in prefixes[1:]])
        suffix_string = suffixes[0] + ''.join([pattern[-1] for pattern in suffixes[1:]])

        for i in range(k + d + 1, len(prefix_string)):
            if prefix_string[i] != suffix_string[i - (k + d + 1)]:
                return "There is no string spelled by the gapped patterns."

        return prefix_string + suffix_string[-(k + d + 1):]

    graph = create_debruijn_graph(paired_reads, k)
    path = eulerian_path(graph)
    result = string_spelled_by_gapped_patterns(path, k, d)
    return result

# Read input from file
with open('dataset_204_16.txt', 'r') as file:
    k, d = map(int, file.readline().strip().split())
    paired_reads = file.readline().strip().split()

# Reconstruct the string
result = reconstruct_string(k, d, paired_reads)

# Write output to file
with open('output.txt', 'w') as file:
    file.write(result)
