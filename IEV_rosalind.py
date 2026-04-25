# Rosalind IEV: you are given six nonnegative integers, each of which does not exceed 20,000. The integers correspond
# to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six
# given integers represent the number of couples having the following genotypes:
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return the expected number of offspring displaying the dominant phenotype in the next generation, under the
# assumption that every couple has exactly two offspring.

# According to the formula of expected value E of a random variable X (E(X) = sum(k * p(X=k), for 1<=k<=n),
# the expected value for a random offspring is:
# 1 × P(dominant) + 0 × P(recessive) = P(dominant)
# (where 1 = dominant resulting offspring, 0 = recessive resulting offspring), which is also the same as saying
# "what is the probability of having a dominant phenotype of a random offspring of a specific pair type?"

# Expected number of dominant offspring from each pair type, under the assumption that each pair always has 2 offspring:
# n_pairs (input) × 2 offspring × P(dominant_offspring)

# INPUT: number of pairs for each pair type.
# OUTPUT: number of expected dominant offspring in the next generation.


import sys


def main():
    w = int(sys.argv[1])     # AA_AA
    x = int(sys.argv[2])     # AA_Aa
    y = int(sys.argv[3])     # AA_aa
    z = int(sys.argv[4])     # Aa_Aa
    j = int(sys.argv[5])     # Aa_aa
    k = int(sys.argv[6])     # aa_aa

    # Probability of dominant offspring from each pair
    p_d_AA_AA = 1
    p_d_AA_Aa = 1
    p_d_AA_aa = 1
    p_d_Aa_Aa = 3 / 4
    p_d_Aa_aa = 1 / 2
    p_d_aa_aa = 0

    p_dominant_offspring = [p_d_AA_AA, p_d_AA_Aa, p_d_AA_aa, p_d_Aa_Aa, p_d_Aa_aa, p_d_aa_aa]
    n_pairs = [w, x, y, z, j, k]
    p_tot = sum(n_p * 2 * pdo for n_p, pdo in zip(n_pairs, p_dominant_offspring))

    print(p_tot)


if __name__ == "__main__":
    main()