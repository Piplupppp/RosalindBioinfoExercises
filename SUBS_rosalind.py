# Rosalind SUBS: given two DNA strings s and t (each of length at most 1 kbp), return all locations of t
# as a substring of s.


import sys


def substring(s, t):
    positions = []
    for i in range(len(s) - len(t) + 1):
        if t == s[i:i+len(t)]:
            positions.append(i+1)
    return positions


def main():
    # lines = sys.stdin.read().splitlines()
    # s = lines[0]
    # t = lines[1]

    file = sys.argv[1]
    with open(file) as f:
        lines = f.read().splitlines()
    s = lines[0]
    t = lines[1]

    print(*substring(s, t))


if __name__ == '__main__':
    main()