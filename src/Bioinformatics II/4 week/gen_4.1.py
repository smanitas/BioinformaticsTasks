"""
Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.

    Input: An amino acid string Peptide and a collection of integers Spectrum.
    Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).

Code Challenge: Solve the Cyclopeptide Scoring Problem.

Sample Input:
NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484

Sample Output:
11
"""

def CyclopeptideScoring(peptide, spectrum):
    theoretical_spectrum = GenerateCyclicSpectrum(peptide)
    score = 0
    spectrum_counts = dict()

    for mass in spectrum:
        spectrum_counts[mass] = spectrum_counts.get(mass, 0) + 1

    for mass in theoretical_spectrum:
        if mass in spectrum_counts and spectrum_counts[mass] > 0:
            score += 1
            spectrum_counts[mass] -= 1

    return score

def GenerateCyclicSpectrum(peptide):
    mass_table = {
        'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'Y': 163,
        'W': 186,
    }

    prefix_mass = [0]
    for i in range(len(peptide)):
        prefix_mass.append(prefix_mass[i] + mass_table[peptide[i]])
    peptide_mass = prefix_mass[-1]
    cyclic_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    cyclic_spectrum.sort()
    return cyclic_spectrum

# Read input from file
with open('dataset_102_3_test.txt', 'r') as file:
    lines = file.readlines()
    peptide = lines[0].strip()
    spectrum = [int(x) for x in lines[1].split()]

# Calculate score
score = CyclopeptideScoring(peptide, spectrum)

# Print the result
print(score)