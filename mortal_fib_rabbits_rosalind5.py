# Rosalind exercise 4: given positive integers n≤100 and m≤20, return the total number of pairs of rabbits that will
# remain after the n-th month if all rabbits live for m months.


import sys


def f_n(n, m):
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1

    for i in range(3, n + 1):
        if i <= m:
            # nessuna morte ancora
            f[i] = f[i - 1] + f[i - 2]
        elif i == m + 1:
            # primo mese con morte (muore la prima generazione)
            f[i] = f[i - 1] + f[i - 2] - 1
        else:
            # regime completo
            f[i] = f[i - 1] + f[i - 2] - f[i - m - 1]

    return f[n]


def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    print(f_n(n, m))


if __name__ == '__main__':
    main()