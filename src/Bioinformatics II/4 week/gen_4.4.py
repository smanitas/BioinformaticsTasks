"""
Code Challenge: Implement ConvolutionCyclopeptideSequencing.

    Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties)
    of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard
    is restricted to the top N (and ties).

Sample Input:
20
60
57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493

Sample Output:
99-71-137-57-72-57
"""

from collections import Counter

def read_input(filename):
    with open(filename, 'r') as f:
        M = int(f.readline().strip())
        N = int(f.readline().strip())
        spectrum = list(map(int, f.readline().strip().split()))
    return M, N, spectrum


def write_output(filename, peptides):
    with open(filename, 'w') as f:
        f.write(' '.join(peptides))


def convolutional_cyclopeptide_sequencing(spectrum, N, M):
    counts = Counter(spectral_convolution(spectrum)).items()
    counts_with_mass_in_range = [m for m in counts if m[0] >= 57 and m[0] <= 200]
    masses = sorted(counts_with_mass_in_range, key=lambda x: x[1], reverse=True)
    cut = masses[M - 1][1]
    top_m_masses = [m[0] for m in masses if m[1] >= cut]

    return cyclopeptide_sequencing_noisy(spectrum, N, aa_masses=top_m_masses)


def cyclopeptide_sequencing_noisy(linear_spectrum, N, aa_masses):
    parent_mass = max(linear_spectrum)

    def cut(leaderboard):
        if len(leaderboard) > N:
            sl = sorted(leaderboard, key=lambda x: x[2], reverse=True)
            cut_score = sl[N - 1][2]
            leaderboard = [p for p in sl if p[2] >= cut_score]

        return leaderboard

    peptides = [([], 0, 0)]
    output = []
    while len(peptides) > 0:
        new_peptides = []
        remove = []
        for p in peptides:
            remove.append(p)
            for aa in aa_masses:
                new_p = (p[0] + [aa], compute_peptide_mass(p[0] + [aa]))
                new_p_score = peptide_spectrum_score(new_p[0], linear_spectrum)
                new_peptides.append((new_p[0], new_p[1], new_p_score))

        for p in remove:
            peptides.remove(p)

        peptides += new_peptides
        remove = []
        new_peptides = []
        for p in peptides:
            if p[1] == parent_mass:
                if len(output) > 0:
                    if p[2] == output[0][2]:
                        output.append(p)
                    elif p[2] > output[0][2]:
                        output = [p]
                else:
                    output = [p]
            elif p[1] > parent_mass:
                remove.append(p)

        for p in remove:
            peptides.remove(p)
        remove = []
        peptides = cut(peptides)

    return [peptide2mass_string(p[0]) for p in output]


def spectral_convolution(spectrum):
    convolution = []
    for i in range(len(spectrum)):
        for j in range(i + 1, len(spectrum)):
            convolution.append(abs(spectrum[i] - spectrum[j]))

    return [c for c in convolution if c > 0]


def compute_peptide_mass(pept):
    return sum(pept)


def peptide_spectrum_score(peptide, spectrum):
    cs = compute_spectrum(peptide, circular=True)
    intersection = Counter(spectrum) & Counter(cs)
    return len([e for e in intersection.elements()])


def compute_spectrum(peptide, circular=False):
    spectrum = []
    n = len(peptide)
    prefix_mass = [0]
    for i in range(n):
        prefix_mass.append(prefix_mass[i] + peptide[i])
    peptide_mass = prefix_mass[n]
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    spectrum.append(0)
    spectrum.sort()
    return spectrum


def peptide2mass_string(peptide):
    return '-'.join(map(str, peptide))


if __name__ == "__main__":
    M, N, spectrum = read_input("dataset_104_7.txt")
    peptides = convolutional_cyclopeptide_sequencing(spectrum, N, M)
    write_output("output.txt", peptides)