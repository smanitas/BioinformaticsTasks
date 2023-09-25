"""
Code Challenge: Solve the Overlap Graph Problem (restated below).

    Input: A collection Patterns of k-mers.
    Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)

Sample Input:
ATGCG GCATG CATGC AGGCA GGCAT GGCAC

Sample Output:
CATGC: ATGCG
GCATG: CATGC
GGCAT: GCATG
AGGCA: GGCAC GGCAT
"""

from collections import defaultdict

def overlap(patterns):
    adjacency_list = defaultdict(set)
    for pattern in patterns:
        adjacency_list[pattern[:-1]].add(pattern)
    with open("output2.txt", "w") as output_file:
        for pattern in patterns:
            suffixes = adjacency_list[pattern[1:]]
            if suffixes:
                output_file.write(pattern + ": " + " ".join(suffixes) + "\n")

# Read input from a file
filename = "dataset_198_10.txt"  # Specify the filename
with open(filename, 'r') as file:
    patterns = file.readline().strip().split()

overlap(patterns)