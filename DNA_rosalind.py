# Rosalind DNA: count nucleotides.


def count_nucleotides(s):
   nucleotides = {base: 0 for base in "ACGT"}
   for letter in s:
      nucleotides[letter] += 1
   return nucleotides


def main():
   s = input("Insert a DNA sequence: ")
   nucleotides = count_nucleotides(s)
   for nucleotide in nucleotides:
      print(nucleotides[nucleotide], end=" ")
      # print(f"{nucleotide}: {nucleotides[nucleotide]} nt")


if __name__ == "__main__":
   main()


# Solution
# import sys

# file = open(sys.argv[1])
# dna_str = file.read() #You can also put the text from the file into the code as a variable

# A = dna_str.count("A")
# C = dna_str.count("C")
# G = dna_str.count("G")
# T = dna_str.count("T")

# print(A, C, G, T)