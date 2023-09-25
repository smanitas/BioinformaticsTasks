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
