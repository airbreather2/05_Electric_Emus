#!/usr/bin/env python3

"""Align DNA sequences and find the best alignment."""

__appname__ = 'align_seqs_fasta'
__author__ = 'Laiyin Zhou, Sebastian Dohne, Yanfeng Wang, Yaxin Liu'
__version__ = '0.0.1'

## imports ##
import sys  # module to interface our program with the operating system

# Two example sequences to match
def read_fasta(file1, file2):
    """Take two FASTA file inputs and extract the sequences."""
    def read_seq(file_path):
        try:
            with open(file_path, 'r') as f:
                next(f)  # skip the heading
                sequence = f.read().replace('\n', '').strip()  # exclude new line characters
                if not sequence:  # handle errors if files don't exist or incorrectly formatted
                    raise ValueError(f"File '{file_path}' is empty or incorrectly formatted.")
            return sequence
        # handle specific types of file reading errors:
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred while reading '{file_path}': {e}")
            sys.exit(1)

    seq1 = read_seq(file1)
    seq2 = read_seq(file2)
    return seq1, seq2

# Decide whether files are default (../data/*.fasta) or explicit input (sys.argv)
file1 = sys.argv[1] if len(sys.argv) > 1 else '../data/407228326.fasta'
file2 = sys.argv[2] if len(sys.argv) > 2 else '../data/407228412.fasta'

seq1, seq2 = read_fasta(file1, file2)

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1  # swap the two lengths

## functions ##
# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """Calculate and return the matching score (the number of matches starting from the startpoint)."""
    matched = []  # Use a list instead of concatenating strings
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]:  # if the bases match
                matched.append("*")
                score += 1
            else:
                matched.append("-")

    # Join list to form the final matched string
    matched_str = ''.join(matched)

    # Some formatted output
    print("." * startpoint + matched_str)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# now try to find the best match (highest score) for the two sequences
def best_match():
    """Find the best match (highest score) for two sequences."""
    my_best_align = None
    my_best_score = -1

    for i in range(l1):  # Note that you just take the last alignment with the highest score
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2  # think about what this is doing!
            my_best_score = z 
    print(my_best_align)
    print(s1)
    print("Best score:", my_best_score)


def main(argv):
    """ Main entry point of the program """
    best_match()  # Removed redundant call to calculate_score()
    return 0

if __name__ == "__main__":
    """Makes sure the "main" function is called from command line"""
    status = main(sys.argv)
    sys.exit(status)
