def reconstruct_string(k, d, paired_reads):
    in_kmer = {i: [p.split('|')[0], p.split('|')[1]] for i, p in enumerate(paired_reads)}
    bkmer = [False] * len(in_kmer)
    pos = len(in_kmer[0][0]) - 1

    while bkmer.count(False) > 1:
        i = 0
        while i < len(in_kmer):
            if not bkmer[i]:
                ikmer = in_kmer[i][0]
                ikmer1 = in_kmer[i][1]
                ek = ikmer[len(ikmer) - pos:]
                ek1 = ikmer1[len(ikmer1) - pos:]
                for j in range(len(in_kmer)):
                    if not bkmer[j]:
                        jkmer = in_kmer[j][0]
                        jkmer1 = in_kmer[j][1]
                        sk = jkmer[:pos]
                        sk1 = jkmer1[:pos]
                        if ek == sk and ek1 == sk1:
                            npref = ikmer + jkmer[pos:]
                            nsuff = ikmer1 + jkmer1[pos:]
                            in_kmer[i][0] = npref
                            in_kmer[i][1] = nsuff
                            bkmer[j] = True
                            i = -1
                            break
            i += 1

    bpos = bkmer.index(False)
    pre = in_kmer[bpos][0]
    suf = in_kmer[bpos][1]
    res = pre + suf[len(suf) - (pos + 1 + d):]
    return res

# Read input from file
with open('dataset_204_16.txt', 'r') as file:
    k, d = map(int, file.readline().strip().split())
    paired_reads = file.readline().strip().split()

# Reconstruct the string
result = reconstruct_string(k, d, paired_reads)

# Write output to file
with open('output.txt', 'w') as file:
    file.write(result)
