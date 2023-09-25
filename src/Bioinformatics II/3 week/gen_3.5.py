"""
Exercise Break: How many subpeptides does a linear peptide of given length n have?
(Include the empty peptide and the entire peptide.)

    Input: An integer n.
    Output: The number of subpeptides of a linear peptide of length n.

Sample Input:
4

Sample Output:
11
"""

def count_subpeptides(n):
    return n * (n + 1) // 2 + 1

if __name__ == "__main__":
    n = int(input())
    subpeptide_count = count_subpeptides(n)
    print(subpeptide_count)
