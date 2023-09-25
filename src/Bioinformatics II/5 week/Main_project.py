def calculate_N50_N75(list_of_lengths):
    """Calculate N50 and N75 for a sequence of numbers.

    Args:
        list_of_lengths (list): List of numbers.

    Returns:
        tuple: N50 and N75 values.

    """
    sorted_lengths = sorted(list_of_lengths, reverse=True)
    total_length = sum(sorted_lengths)

    n50_threshold = total_length * 0.5
    n75_threshold = total_length * 0.75

    cumulative_length = 0
    n50 = 0
    n75 = 0

    for length in sorted_lengths:
        cumulative_length += length

        if cumulative_length >= n50_threshold and n50 == 0:
            n50 = length

        if cumulative_length >= n75_threshold and n75 == 0:
            n75 = length
            break

    return n50, n75

contig_lengths = [10, 20, 30, 60, 70]
n50_value, n75_value = calculate_N50_N75(contig_lengths)

print("N50:", n50_value)
print("N75:", n75_value)
