# Rosalind exercise 9: given collection of at most 10 symbols defining an ordered alphabet, and a positive integer n
# (n≤10), return ll strings of length n that can be formed from the alphabet, ordered lexicographically
# (use the standard order of symbols in the English alphabet).


import sys


def permutation(n, alphabet):
    permutations = []
    if n == 1:
        for letter in alphabet:
            permutations.append([letter])
        return permutations
    for letter in alphabet:
        for p in permutation(n - 1, alphabet):
            permutations.append([letter] + p)
    return permutations


def main():
    file = sys.argv[1]
    with open(file) as f:
        alphabet = list(f.readline().strip().split())
        n = int(f.readline())
    permutations = permutation(n, sorted(alphabet))
    for perm in permutations:
        print("".join(perm))


if __name__ == "__main__":
    main()