# Rosalind IPRB: given three positive integers k, m, and n, representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return the probability that two randomly selected mating organisms will produce an individual possessing a
# dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


# Probabilities of dominant phenotype considering all possible mating combinations:
# AA × AA → always dominant → probability 1
# AA × aa → always dominant (Aa) → probability 1
# AA × Aa → probability 1
# Aa × Aa → probability 3/4
# Aa × aa → probability 1/2
# aa × aa → never dominant → probability 0


# Start
# ├── AA  (k/t)
# │   ├── AA  (k-1)/(t-1)
# │   ├── Aa  m/(t-1)
# │   └── aa  n/(t-1)
# ├── Aa  (m/t)
# │   ├── AA  k/(t-1)
# │   ├── Aa  (m-1)/(t-1)
# │   └── aa  n/(t-1)
# └── aa  (n/t)
#     ├── AA  k/(t-1)
#     ├── Aa  m/(t-1)
#     └── aa  (n-1)/(t-1)
# For mixed pairs probability needs to be multiplied by 2 due to the 2 possible different orders.


import sys


def main():
    k = int(sys.argv[1])
    m = int(sys.argv[2])
    n = int(sys.argv[3])
    t = k + m + n

    # Probability of each pair
    p_AA_AA = (k/t) * ((k-1)/(t-1))
    p_AA_aa = (k/t) * (n/(t-1)) * 2
    p_AA_Aa = (k/t) * (m/(t-1)) * 2
    p_Aa_Aa = (m/t) * ((m-1)/(t-1))
    p_Aa_aa = (m/t) * (n/(t-1)) * 2
    p_aa_aa = (n/t) * ((n-1)/(t-1))

    # Probability of dominant offspring from each pair
    p_d_AA_AA = 1
    p_d_AA_aa = 1
    p_d_AA_Aa = 1
    p_d_Aa_Aa = 3/4
    p_d_Aa_aa = 1/2
    p_d_aa_aa = 0

    # Total probability of dominant offspring coming from each randomly selected pair
    p_coppie = [p_AA_AA, p_AA_Aa, p_AA_aa, p_Aa_Aa, p_Aa_aa, p_aa_aa]
    p_figli = [p_d_AA_AA, p_d_AA_Aa, p_d_AA_aa, p_d_Aa_Aa, p_d_Aa_aa, p_d_aa_aa]
    p_tot = sum(pc * pf for pc, pf in zip(p_coppie, p_figli))

    print(p_tot)


if __name__ == '__main__':
    main()