"""
Created on 11/27/2020

@author: nadia
"""


def sequenceInput(seq):
    bases = {"A": "U", "C": "G", "G": "C", "T": "A", "U": "A"}
    dna = " ".join([(seq[i:i + 3]) for i in range(0, len(seq), 3)])
    print("DNA sequence: " + dna)
    # convert DNA to mRNA
    r = ""
    for x in seq:
        for k in bases.keys():
            if k == x:
                r += bases[k]
    mrna = " ".join([(r[i:i + 3]) for i in range(0, len(r), 3)])
    print("mRNA codons: " + mrna)
    # convert mRNA to tRNA
    t = ""
    for x in r:
        for k in bases.keys():
            if k == x:
                t += bases[k]
    trna = " ".join([(t[i:i + 3]) for i in range(0, len(t), 3)])
    print("tRNA anticodons: " + trna)
    getAA = input("Get amino acid sequence? (y/n) ")
    if getAA == "y":
        return trna, True
    else:
        return trna, False


def aminoacid(anti):
    aa = ""
    amino = {"Phe": ["UUU", "UUC"], "Leu": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"], "Ile": ["AUU", "AUC", "AUA"],
             "Met": "AUG", "Val": ["GUU", "GUC", "GUA", "GUG"], "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
             "Pro": ["CCU", "CCA", "CCC", "CCG"], "Thr": ["ACU", "ACG", "ACC", "ACA"],
             'Ala': ['GCU', 'GCC', 'GCG', 'GCA'], 'Tyr': ['UAU', 'UAC'], 'Stop': ['UAA','UAG','UGA','UGG'],
             'His': ["CAU", "CAC"], "Gln": ["CAA", "CAG"], "Asn": ["AAU", "AAC"], "Lys": ["AAG", "AAA"],
             "Asp": ["GAU", "GAC"], "Glu": ["GAA", "GAG"], "Cys": ["UGU", "UGC"], "Arg": ["CGU", "CGG", "CGA",
                                                                                          "CGC", "AGA", "AGG"],
             "Gly": ["GGU", "GGA", "GGC", "GGG"]}
    lst = anti[0].split()
    if anti[1]:
        for x in lst:
            for k in amino.keys():
                if x in amino[k]:
                    if aa == "":
                        if k != "Met":
                            pass
                        else:
                            aa += k
                    elif aa != "":
                        aa += "-" + k
                        if k == "Stop":
                            print(aa)
                            return shorten(aa)
    else:
        return "goodbye"


def shorten(aa):
    short = ""
    abbrev = {"Ala": "A", "Cys": "C", "Arg": "R", "Asn": "N", "Asp": "D", "Gln": "Q", "Glu": "E", "Gly": "G",
              "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F", "Pro": "P", "Ser": "S",
              "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V"}
    for x in aa.split("-"):
        for k in abbrev.keys():
            if x == "Stop":
                return short
            elif x == k:
                short += abbrev[k]


if __name__ == '__main__':
    s = input("Input DNA Sequence: ")
    gene = sequenceInput(s)
    print(aminoacid(gene))
