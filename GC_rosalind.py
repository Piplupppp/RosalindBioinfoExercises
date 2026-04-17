# Rosalind GC: given at most 10 DNA strings in FASTA format (of length at most 1 kbp each), return the ID
# of the string having the highest GC-content, followed by the GC-content of that string.


import sys


def gc_content(sequence):
    count = 0
    for base in sequence:
        if base == "G" or base == "C":
            count += 1
    return count / len(sequence) * 100


def main():
    sequence_list = {}

    with open(sys.argv[1]) as file:
        first_line = True
        sequence = ""
        for line in file:
            if line.startswith(">") and first_line:
                s_id = line.strip()[1:]
                first_line = False
                continue
            elif line.startswith(">") and not first_line:
                sequence_list[s_id] = gc_content(sequence)
                s_id = line.strip()[1:]
                sequence = ""
                continue
            else:
                sequence += line.strip()
        sequence_list[s_id] = gc_content(sequence)

    s_max = max(sequence_list, key=lambda k: sequence_list[k])
    print(f"{s_max}\n{sequence_list[s_max]:.6f}")


if __name__ == "__main__":
    main()