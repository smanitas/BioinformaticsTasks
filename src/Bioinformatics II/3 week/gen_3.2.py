"""
Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.

    Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    Output: All substrings of Text encoding Peptide (if any such substrings exist).

Code Challenge: Solve the Peptide Encoding Problem.
Click here for the RNA codon table corresponding to the array GeneticCode.

Note: The solution may contain repeated strings if the same string occurs more
than once as a substring of Text and encodes Peptide.

Sample Input:
ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA

Sample Output:
ATGGCC
GGCCAT
ATGGCC
"""

def peptide_encoding_problem(dna, peptide):
    patterns = []

    last_index = len(dna) - len(peptide) * 3
    for i in range(last_index + 1):
        pattern_dna = dna[i:i + len(peptide) * 3]
        pattern_rna = dna_to_rna(pattern_dna)

        reverse_complement_pattern_dna = reverse_complement(pattern_dna)
        reverse_complement_pattern_rna = dna_to_rna(reverse_complement_pattern_dna)

        if translate_rna_to_protein(pattern_rna) == peptide or translate_rna_to_protein(reverse_complement_pattern_rna) == peptide:
            patterns.append(pattern_dna)

    return patterns

def dna_to_rna(pattern_dna):
    return pattern_dna.replace('T', 'U')

def reverse_complement(pattern_dna):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[base] for base in pattern_dna[::-1])

def translate_rna_to_protein(rna):
    genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        amino_acid = genetic_code.get(codon, '')
        if amino_acid == '*':
            break
        protein += amino_acid

    return protein


def read_dataset(filename):
    with open(filename, 'r') as file:
        dna = file.readline().strip()
        peptide = file.readline().strip()

    return dna, peptide


def write_output(filename, patterns):
    with open(filename, 'w') as file:
        for pattern in patterns:
            file.write(pattern + '\n')


# Example usage:
dataset_file = 'dataset_96_7.txt'
output_file = 'output.txt'

# Read input from dataset file
dna, peptide = read_dataset(dataset_file)

# Solve the peptide encoding problem
patterns = peptide_encoding_problem(dna, peptide)

# Write output to file
write_output(output_file, patterns)