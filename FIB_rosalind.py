# Rosalind FIB: given positive integers n≤40 and k≤5, return the total number of rabbit pairs that will be
# present after n  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits
# produces a litter of k rabbit pairs (instead of only 1 pair)


import sys


def f_n(n, k):
    if n <= 2:
        return 1
    return f_n(n-1, k) + (k * f_n(n-2, k))

    # f1 = 1
    # f2 = 1
    # for i in range(3, n):
        # f_new = f2 + (k * f1)
        # f1 = f2
        # f2 = f_new
    # return f_new


def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])

    # n, k = input().split()
    # n, k = int(n), int(k)

    print(f_n(n, k))


if __name__ == '__main__':
    main()