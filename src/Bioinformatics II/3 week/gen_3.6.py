"""
Code Challenge: Implement CyclopeptideSequencing (pseudocode reproduced below).

Note: After the failure of the first brute-force algorithm we considered,
you may be hesitant to implement CyclopeptideSequencing for fear that its runtime will be prohibitive.
The potential problem with CyclopeptideSequencing is that it may generate incorrect k-mers at intermediate stages
(i.e., k-mers that are not subpeptides of a correct solution).
In practice, however, this is not a concern. See Charging Station: How fast is CyclopeptideSequencing?

CyclopeptideSequencing(Spectrum)
    CandidatePeptides ← a set containing only the empty peptide FinalPeptides ← empty list of strings
    while CandidatePeptides is nonempty
        CandidatePeptides ← Expand(CandidatePeptides)
        for each peptide Peptide in CandidatePeptides
            if Mass(Peptide) = ParentMass(Spectrum)
                if Cyclospectrum(Peptide) = Spectrum and Peptide is not in FinalPeptides
                    append Peptide to FinalPeptides
                remove Peptide from CandidatePeptides
            else if Peptide is not consistent with Spectrum
                remove Peptide from CandidatePeptides
    return FinalPeptides

Sample Input:
0 113 128 186 241 299 314 427

Sample Output:
186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
"""

import itertools

def CYCLOPEPTIDESEQUENCING(in_spectrum, masss):
    in_spectrum_a = in_spectrum.strip().split()
    in_spectrum_s = ''

    for p in in_spectrum_a:
        if p in masss.values():
            in_spectrum_s += MassKey(p, masss)

    dic_spe = {}
    for i, p in enumerate(list(map(chr, range(97, 97 + len(in_spectrum_s))))):
        dic_spe[p] = in_spectrum_s[i]

    ou_spectrum_s = list(dic_spe.keys())
    in_spectrum_d = list(dic_spe.keys())

    for k in range(len(in_spectrum_s) - 1):
        tmp = []
        for p in ou_spectrum_s:
            for q in in_spectrum_d:
                if p.find(q) < 0:
                    dp = DictValue(p, dic_spe)
                    dq = DictValue(q, dic_spe)
                    if Split(dp + dq, masss, in_spectrum_a) and str(Sum(dp + dq, masss)) in in_spectrum_a:
                        tmp.append(p + q)
        ou_spectrum_s = list(tmp)

    uou_spectrum_s = []
    for p in sorted(ou_spectrum_s):
        pd = DictValue(p, dic_spe)
        if pd not in uou_spectrum_s:
            uou_spectrum_s.append(pd)

    result = []
    for pd in sorted(uou_spectrum_s):
        result.append(Total(pd, masss))

    return result

def Total(mc, masss):
    tot = ''
    for p in mc:
        tot += masss[p] + '-'
    return tot[:-1]

def MassKey(p, masss):
    for k, v in masss.items():
        if v == p:
            return k

def Sum(mc, masss):
    tot = 0
    for p in mc:
        tot += int(masss[p])
    return tot

def DictValue(pq, dic_spe):
    dpq = ''
    for p in pq:
        dpq += dic_spe[p]
    return dpq

def Split(p, masss, in_spectrum_a):
    pp = p
    for i in range(len(pp) - 1):
        mc = pp[i:i + len(p) - 1]
        if str(Sum(mc, masss)) not in in_spectrum_a:
            return False
    return True

in_file = open('dataset_100_6.txt', 'r')
in_mass = open('integer_mass_table.txt', 'r')
line = 1
in_spectrum = ""
in_result = ""

for in_data in in_file:
    if line == 1:
        in_spectrum = in_data.strip()
    line += 1

masss = {}
for in_data in in_mass:
    line = in_data.strip().split()
    if len(line) == 2:
        masss[line[0]] = line[1]

result = CYCLOPEPTIDESEQUENCING(in_spectrum, masss)

for peptide in result:
    print(peptide)