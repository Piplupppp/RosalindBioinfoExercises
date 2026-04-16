# Rosalind exercise 8: given a positive integer n≤7, return the total number of permutations of length n,
# followed by a list of all such permutations (in any order).


import sys


def permutation(numbers):
    permutations = []
    if len(numbers) == 1:
        permutations.append([numbers[0]])
        return permutations
    for number in numbers:
        resto = [x for x in numbers if x != number]
        for p in permutation(resto):
            permutations.append([number] + p)
    return permutations


def main():
    n = int(sys.argv[1])
    numbers = list(range(1, n+1))
    permutations = permutation(numbers)
    print(len(permutations))
    for perm in permutations:
        print(*perm)


if __name__ == "__main__":
    main()