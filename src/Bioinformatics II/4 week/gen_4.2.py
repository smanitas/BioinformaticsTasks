def read_spectrum(file_name):
    with open(file_name, 'r') as file:
        spectrum = [float(mass) for mass in file.read().split()]
    return spectrum

experimental_spectrum = read_spectrum('experimental_spectrum.txt')


def read_mass_table(file_name):
    mass_table = {}
    with open(file_name, 'r') as file:
        for line in file:
            amino_acid, mass = line.strip().split()
            mass_table[int(mass)] = amino_acid
    return mass_table


def generate_peptide_sequence(spectrum, mass_table, n):
    leaderboard = [([], 0)]
    leader_peptide = []
    parent_mass = max(spectrum)

    while leaderboard:
        leaderboard = expand_leaderboard(leaderboard, mass_table)
        leaderboard = trim_leaderboard(leaderboard, spectrum, n)

        for peptide, score in leaderboard:
            if sum(peptide) == parent_mass and score > calculate_score(leader_peptide, spectrum):
                leader_peptide = peptide

        leaderboard = select_leaderboard(leaderboard, n)

    return leader_peptide


def expand_leaderboard(leaderboard, mass_table):
    new_leaderboard = []
    for peptide, score in leaderboard:
        for mass in mass_table:
            new_peptide = peptide + [mass]
            new_score = calculate_score(new_peptide, spectrum)
            new_leaderboard.append((new_peptide, new_score))
    return new_leaderboard


def trim_leaderboard(leaderboard, spectrum, n):
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    if len(sorted_leaderboard) <= n:
        return sorted_leaderboard
    threshold = sorted_leaderboard[n - 1][1]
    trimmed_leaderboard = []
    for peptide, score in sorted_leaderboard:
        if score >= threshold or (score == threshold and len(peptide) == len(sorted_leaderboard[n - 1][0])):
            trimmed_leaderboard.append((peptide, score))
    return trimmed_leaderboard


def calculate_score(peptide, spectrum):
    peptide_spectrum = generate_linear_spectrum(peptide)
    score = 0
    spectrum_counts = collections.Counter(spectrum)
    for mass in peptide_spectrum:
        if spectrum_counts[mass] > 0:
            score += 1
            spectrum_counts[mass] -= 1
    return score


def generate_linear_spectrum(peptide):
    prefix_mass = [0]
    for i in range(len(peptide)):
        prefix_mass.append(prefix_mass[i] + peptide[i])
    linear_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(linear_spectrum)


def select_leaderboard(leaderboard, n):
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    if len(sorted_leaderboard) <= n:
        return sorted_leaderboard
    threshold = sorted_leaderboard[n - 1][1]
    selected_leaderboard = []
    for peptide, score in sorted_leaderboard:
        if score >= threshold:
            selected_leaderboard.append((peptide, score))
    return selected_leaderboard


# Read spectrum and mass table
spectrum = read_spectrum('experimental_spectrum.txt')
mass_table = read_mass_table('integer_mass_table.txt')

# Generate peptide sequence
peptide_sequence = generate_peptide_sequence(spectrum, mass_table, n=1000)

# Convert peptide sequence to space-separated integer masses
peptide_masses = ' '.join(str(mass_table[mass]) for mass in peptide_sequence)

# Print the result
print(peptide_masses)
