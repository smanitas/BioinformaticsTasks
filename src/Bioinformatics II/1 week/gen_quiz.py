def reconstruct_string(k, d, paired_reads):
    prefixes = []
    suffixes = []

    # Extract prefixes and suffixes from paired reads
    for read in paired_reads:
        prefix, suffix = read.split('|')
        prefixes.append(prefix)
        suffixes.append(suffix)

    # Reconstruct the string
    initial_string = prefixes[0] + suffixes[0][-k+d:]
    for i in range(1, len(prefixes)):
        initial_string += suffixes[i-1][-1] + prefixes[i][-k+d:]

    return initial_string

# Parse the input
k, d = map(int, input().split())
paired_reads = [input() for _ in range(9)]

# Reconstruct the string
reconstructed_string = reconstruct_string(k, d, paired_reads)

# Print the reconstructed string
print(reconstructed_string)