from collections import defaultdict

def debruijn_graph(kmers):
    adjacency_list = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        adjacency_list[prefix].append(suffix)
    return adjacency_list

# Read the input from a file
with open('dataset_200_8.txt', 'r') as file:
    kmers = file.read().split()

# Generate the De Bruijn graph
graph = debruijn_graph(kmers)

# Write the output to a file
with open('output_4.txt', 'w') as file:
    for prefix, suffixes in graph.items():
        file.write(prefix + ': ' + ' '.join(suffixes) + '\n')