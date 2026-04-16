# Rosalind exercise 7: given two strings s and t of equal length, return the hamming distance between s and t,
# denoted dH(s, t) and equal to the number of corresponding symbols that differ in s and t


import sys


def d_h(s, t):
    hamming_dist = 0
    for base_s, base_t in zip(s, t):
        if base_s != base_t:
            hamming_dist += 1
    return hamming_dist


def main():
    file = sys.argv[1]
    with open(file) as f:
        s, t = f.read().splitlines()
        print(d_h(s, t))


if __name__ == "__main__":
    main()