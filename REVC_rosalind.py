# Rosalind REVC: reverse complement (s^c) of DNA sequence


def reverse_complement(s):
    s_reverse = s[::-1]
    complement_map = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }
    return "".join(complement_map.get(base) for base in s_reverse)
    # complement = ""
    # for base in reverse_sequence:
    #   complement += complement_map.get(base, "N")
    # return complement


def main():
    s = input("Insert a DNA sequence: ")
    print(reverse_complement(s))


if __name__ == "__main__":
    main()
