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