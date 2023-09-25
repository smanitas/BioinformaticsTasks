from Bio.Seq import Seq

for dna in ['CCUCGUACAGAAAUCAAC','CCAAGAACAGAUAUCAAU', 'CCAAGUACAGAGAUUAAC','CCGAGGACCGAAAUCAAC']:
    print(Seq(dna).translate())