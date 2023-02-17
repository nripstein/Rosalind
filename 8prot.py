# done and submitted



codon_dict = {"UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
"UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
"UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
"UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
"UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
"UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
"UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
"UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
"UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
"UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
"UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
"UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
"UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
"UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"}


def prot(dna: str) -> str:
    codons = []
    output = ""
    for letter_index in range(0, len(dna), 3):
        codons.append(dna[letter_index] + dna[letter_index + 1] + dna[letter_index + 2])
    for codon in codons:
        to_add = codon_dict[codon]
        if to_add != "Stop":
            output += codon_dict[codon]
        else:
            return output
    return output

# print(codon_dict["AGG"])


# print(prot("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA") == "MAMAPRTEINSTRING")
# a was too long to save
