def generate_theoretical_spectrum(peptide):
    masses = {
        'A': 71,
        'L': 113,
        'E': 129,
        'W': 186,
        'F': 165,
        'M': 131,
        'I': 113,
        'T': 101
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


def check_cyclic_peptides(peptides, theoretical_spectrum):
    matching_peptides = []
    for peptide in peptides:
        peptide_spectrum = generate_theoretical_spectrum(peptide)
        if set(peptide_spectrum).issubset(set(theoretical_spectrum)):
            matching_peptides.append(peptide)
    return matching_peptides


theoretical_spectrum = [0, 71, 101, 113, 131, 184, 202, 214, 232, 285, 303, 315, 345, 416]
peptides = ['MAIT', 'TAIM', 'TLAM', 'TMIA', 'MTAI', 'TMLA']

matching_peptides = check_cyclic_peptides(peptides, theoretical_spectrum)
print("The cyclic peptides that could have generated the theoretical spectrum are:")
for peptide in matching_peptides:
    print(peptide)
