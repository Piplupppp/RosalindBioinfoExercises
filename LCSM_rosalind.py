# Given a collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format, return a longest common
# substring of the collection. (If multiple solutions exist, you may return any single solution.)


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


def longest_common_substring(sequences):
    s = min(sequences, key=len)
    for k in range(len(s), 0, -1):
        for i in range(len(s)-k+1):
            t = s[i:i+k]
            if all(t in seq for seq in sequences):
                return t


def main():
    file = sys.argv[1]
    with open(file) as f:
        lines = f.read().splitlines()
    sequences = parse_fasta(lines)

    print(longest_common_substring(sequences))


if __name__ == "__main__":
    main()