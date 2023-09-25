def reconstruct_string_from_path(patterns):
    reconstructed_string = patterns[0]
    k = len(patterns[0])
    for i in range(1, len(patterns)):
        reconstructed_string += patterns[i][-1]
    return reconstructed_string

# Read input from a file
filename = "dataset_198_3(1).txt"  # Specify the filename
with open(filename, 'r') as file:
    patterns = file.readline().strip().split()

result = reconstruct_string_from_path(patterns)
print(result)