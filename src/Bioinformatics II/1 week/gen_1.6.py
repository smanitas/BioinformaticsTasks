"""
DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.

    Input: A collection of k-mers Patterns.
    Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).

Code Challenge: Solve the de Bruijn Graph from k-mers Problem.

Sample Input:
GAGG CAGG GGGG GGGA CAGG AGGG GGAG

Sample Output:
AGG: GGG
CAG: AGG AGG
GAG: AGG
GGA: GAG
GGG: GGA GGG
"""

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