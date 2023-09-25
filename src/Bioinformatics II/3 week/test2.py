from Bio.Seq import Seq

def count_dna_strings(amino_acid_seq):
    count = 0
    codons = {
        'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'E': ['GAA', 'GAG'],
        'A': ['GCA', 'GCC', 'GCG', 'GCT'],
        'D': ['GAT', 'GAC'],
        'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    }

    def generate_dna_strings(amino_acid_seq, current_seq):
        if len(current_seq) == len(amino_acid_seq) * 3:
            if str(Seq(current_seq).translate()) == amino_acid_seq:
                nonlocal count
                count += 1
            return
        for codon in codons[amino_acid_seq[len(current_seq) // 3]]:
            generate_dna_strings(amino_acid_seq, current_seq + codon)

    generate_dna_strings(amino_acid_seq, '')
    return count

target_amino_acid_seq = "LEADER"
num_strings = count_dna_strings(target_amino_acid_seq)
print(f"The number of DNA strings transcribing and translating to '{target_amino_acid_seq}' is: {num_strings}")
