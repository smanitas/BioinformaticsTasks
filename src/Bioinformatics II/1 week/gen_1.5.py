"""
Code Challenge: Solve the De Bruijn Graph from a String Problem.

    Input: An integer k and a string Text.
    Output: DeBruijnk(Text), in the form of an adjacency list.

Sample Input:
4
AAGATTCTCTAAGA

Sample Output:
AAG: AGA AGA
AGA: GAT
ATT: TTC
CTA: TAA
CTC: TCT
GAT: ATT
TAA: AAG
TCT: CTA CTC
TTC: TCT
"""

def debruijn_graph(k, text):
    adjacency_list = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k-1]
        next_pattern = text[i+1:i+k]
        if pattern in adjacency_list:
            adjacency_list[pattern].append(next_pattern)
        else:
            adjacency_list[pattern] = [next_pattern]
    return adjacency_list

# Read the input from a file
with open('dataset_199_6.txt', 'r') as file:
    k = int(file.readline().strip())
    text = file.readline().strip()

# Generate the De Bruijn graph
graph = debruijn_graph(k, text)

# Write the output to a file
with open('output3.txt', 'w') as file:
    for pattern, next_patterns in graph.items():
        file.write(pattern + ': ' + ' '.join(next_patterns) + '\n')