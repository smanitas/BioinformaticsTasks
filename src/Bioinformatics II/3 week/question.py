def count_tyrocidine_b1_strings():
    amino_acids = ['Val', 'Lys', 'Leu', 'Phe', 'Pro', 'Trp', 'Phe', 'Asn', 'Gln', 'Tyr']
    codons = {
        'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
        'Lys': ['AAA', 'AAG'],
        'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'Phe': ['TTT', 'TTC'],
        'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
        'Trp': ['TGG'],
        'Asn': ['AAT', 'AAC'],
        'Gln': ['CAA', 'CAG'],
        'Tyr': ['TAT', 'TAC']
    }

    count = 1
    for amino_acid in amino_acids:
        count *= len(codons[amino_acid])

    return count

# Calculate the number of DNA strings
num_strings = count_tyrocidine_b1_strings()
print(num_strings)
