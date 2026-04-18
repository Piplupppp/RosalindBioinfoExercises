# Rosalind SIGN: given a positive integer n≤6, return the total number of signed permutations of length n
# followed by a list of all such permutations (you may list the signed permutations in any order).


import sys
import itertools


def permutations(n):
    perm = itertools.permutations(range(1, n+1))
    results = []
    for perm in perm:
        signs = itertools.product([-1, 1], repeat=n)
        for sign in signs:
            results.append([s * x for s, x in zip(sign, perm)])
    return results


def main():
    n = int(sys.argv[1])
    results = permutations(n)
    print(len(results))
    for result in results:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()