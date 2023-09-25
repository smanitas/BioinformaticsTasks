def translate_rna_to_protein(rna_string, genetic_code):
    codon_table = dict()
    with open(genetic_code) as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) == 2:
                    codon, protein = parts
                    codon_table[codon] = protein if protein != "" else None

    peptide = ""
    for i in range(0, len(rna_string), 3):
        codon = rna_string[i:i + 3]
        if codon_table.get(codon) is None:
            break
        peptide += codon_table[codon]

    return peptide


# Example usage
rna_file = "dataset_96_4.txt"
genetic_code = "RNA_codon_table_1.txt"

with open(rna_file) as file:
    rna_string = file.read().strip()

peptide = translate_rna_to_protein(rna_string, genetic_code)
print(peptide)