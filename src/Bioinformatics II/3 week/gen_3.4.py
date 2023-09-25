"""
Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.

    Input: An amino acid string Peptide.
    Output: Cyclospectrum(Peptide).

Code Challenge: Solve the Generating Theoretical Spectrum Problem.

Note: An obvious approach for solving the Generating Theoretical Spectrum Problem
would be to construct a list containing all subpeptides of Peptide,
and then find the mass of each subpeptide by adding the integer masses
of its constituent amino acids. This approach will work, but you may like to check out Charging Station:
Generating the Theoretical Spectrum of a Peptide to see a more elegant algorithm
that applies to both linear and cyclic peptides.

Sample Input:
LEQN

Sample Output:
0 113 114 128 129 227 242 242 257 355 356 370 371 484
"""

def mass_of_amino_acid(amino_acid):
    masses = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
    }
    return masses[amino_acid]

def linear_spectrum(peptide):
    prefix_mass = [0]
    n = len(peptide)
    for i in range(n):
        prefix_mass.append(prefix_mass[i] + mass_of_amino_acid(peptide[i]))
    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)

def circular_spectrum(peptide):
    prefix_mass = [0]
    n = len(peptide)
    for i in range(n):
        prefix_mass.append(prefix_mass[i] + mass_of_amino_acid(peptide[i]))
    peptide_mass = prefix_mass[n]
    spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(spectrum)

if __name__ == "__main__":
    peptide = "QWDQVRDATEKTKPHSKRGIATWECSESEKLEMHTW"
    spectrum = circular_spectrum(peptide)
    spectrum_str = ' '.join(str(mass) for mass in spectrum)
    print(spectrum_str)

with open('output.txt', 'w') as file:
    file.write(spectrum_str)