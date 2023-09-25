def generate_theoretical_spectrum(peptide):
    masses = {
        'A': 71,
        'C': 103,
        'D': 115,
        'E': 129,
        'F': 147,
        'G': 57,
        'H': 137,
        'I': 113,
        'K': 128,
        'L': 113,
        'M': 131,
        'N': 114,
        'P': 97,
        'Q': 128,
        'R': 156,
        'S': 87,
        'T': 101,
        'V': 99,
        'W': 186,
        'Y': 163
    }

    spectrum = [0]
    peptide_mass = sum(masses[aa] for aa in peptide)
    spectrum.append(peptide_mass)

    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            subpeptide_mass = sum(masses[aa] for aa in peptide[i:j])
            spectrum.append(subpeptide_mass)

    spectrum.sort()
    return spectrum


def check_linear_peptides(peptides, spectrum):
    matching_peptides = []
    for peptide in peptides:
        peptide_spectrum = generate_theoretical_spectrum(peptide)
        if set(peptide_spectrum).issubset(set(spectrum)):
            matching_peptides.append(peptide)
    return matching_peptides


spectrum = [0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333]
peptides = ['VAQ', 'TCQ', 'QCV', 'TCE', 'AQV', 'CTV']

matching_peptides = check_linear_peptides(peptides, spectrum)
print("The linear peptides consistent with the given spectrum are:")
for peptide in matching_peptides:
    print(peptide)
