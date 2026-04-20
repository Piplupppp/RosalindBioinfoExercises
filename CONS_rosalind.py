# Rosalind exercise CONS: given a collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format,
# return a consensus string and profile matrix for the collection. (If several possible consensus strings exist,
# then you may return any one of them.)


import sys


def parse_fasta(file):
    sequences = []
    sequence = ""
    for line in file:
        if line.startswith(">"):
            if sequence:
                sequences.append(sequence)
            sequence = ""
            continue
        else:
            sequence += line.strip()
    sequences.append(sequence)
    return sequences


def main():
    file = sys.argv[1]
    with open(file) as f:
        lines = f.read().splitlines()
    sequences = parse_fasta(lines)

    n = len(sequences[0])
    profile = {
        "A": [0] * n,
        "C": [0] * n,
        "G": [0] * n,
        "T": [0] * n
    }

    for sequence in sequences:
        for i, base in enumerate(sequence):
            profile[base][i] += 1

    consensus = []

    for i in range(n):
        consensus.append(max("ACGT", key=lambda b: profile[b][i]))

    print("".join(consensus))
    for base in profile:
        print(base + ": " + " ".join(map(str, profile[base])))


if __name__ == "__main__":
    main()