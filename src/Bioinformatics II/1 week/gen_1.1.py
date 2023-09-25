"""
Code Challenge: Solve the String Composition Problem.

    Input: An integer k and a string Text.
    Output: Compositionk(Text) (the k-mers can be provided in any order).

Sample Input:
5
CAATCCAAC

Sample Output:
CAATC AATCC ATCCA TCCAA CCAAC
"""


def string_composition(k, text):
    composition = []
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        composition.append(kmer)
    return composition

# Read input from a file
filename = "dataset_197_3.txt"  # Specify the filename
with open(filename, 'r') as file:
    k = int(file.readline().strip())
    text = file.readline().strip()

result = string_composition(k, text)
output = ' '.join(result)

# Write the output to a file
output_filename = "output_gen.txt"
with open(output_filename, 'w') as output_file:
    output_file.write(output)