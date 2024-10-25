#!/usr/bin/env python3

"""
Description: This script compares two DNA sequences from a FASTA file, aligns them, and calculates 
the best alignment based on the number of matching bases. It uses a scoring function to determine
the best match and saves the alignment result along with the score to a text file.

"""

__appname__ = 'align_seqs_better'
__author__ = 'Laiyin Zhou (l.zhou24@imperial.ac.uk), Sebatian Dohne (sebastian.dohne24@imperial.ac.uk), Yanfeng Wang (yanfeng.wang24@imperial.ac.uk), Yaxin Liu (yaxin.liu24@imperial.ac.uk)'
__version__ = '0.0.1'


## imports ##
import sys # module to interface our program with the operating system
import os  #  to check and create directory if necessary

# Two example sequences to match
def read_seq(file_path):
    """
    Read a DNA sequence from a FASTA file, ignoring the header.

    Args:
        file_path (str): Path to a FASTA file.

    Returns:
        str: DNA sequence from the file.
        
    Raises:
        FileNotFoundError: If the file is not found.
        ValueError: If the file is empty or incorrectly formatted.
        Exception: For any other unexpected file reading errors.
    """
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

def read_fasta(file1, file2):
    """
    Read sequences from two FASTA files.

    Parameters:
        file1 (str): Path to the first FASTA file.
        file2 (str): Path to the second FASTA file.

    Returns:
        tuple: A tuple containing two DNA sequences (seq1, seq2).
    """
    # Check if both filenames end with '.fasta'
    if not (file1.lower().endswith('.fasta') and file2.lower().endswith('.fasta')):
        print("Error: Both files must be FASTA files. Please provide valid .fasta files.")
        return None, None
        
    seq1 = read_seq(file1)
    seq2 = read_seq(file2)
    return seq1, seq2

# Decide wether files are default (../data/*.fasta) or explicit input (sys.argv)
file1 = sys.argv[1] if len(sys.argv) >1 else '../data/407228326.fasta'
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
    l1, l2 = l2, l1 # swap the two lengths


## functions ##
# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """
    Computes the alignment score by counting the number of matching bases 
    between two DNA sequences starting from a specified point.

    Args:
        s1 (str): The first DNA sequence (the longer sequence).
        s2 (str): The second DNA sequence (the shorter sequence).
        l1 (int): The length of the first DNA sequence.
        l2 (int): The length of the second DNA sequence.
        startpoint (int): The starting index in the first sequence for the alignment.

    Returns:
        int: The total score representing the number of matching bases found during the alignment.
    
    This function prints a visual representation of the alignment, where 
    '*' indicates a match and '-' indicates a mismatch.
    """
    matched = []  # Use a list instead of concatenating strings to make it run faster
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

    # some formatted output
    print("." * startpoint + matched_str)  # Convert list to string before printing
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# Test the function with some example starting points:
#calculate_score(s1, s2, l1, l2, 0)
#calculate_score(s1, s2, l1, l2, 1)
#calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences

# Ensure the 'results' directory exists, creating it if necessary
results_dir = '../results'
try:
    os.makedirs(results_dir, exist_ok=True)
except OSError as e:
    print(f"Error creating directory '{results_dir}': {e}")
    exit(1)  # Exit with an error code if directory creation fails


def best_match(s1, s2, l1, l2):
    """
    Identifies the best alignments (highest scores) between two DNA sequences and saves them to a text file.

    The function compares two DNA sequences (`s1` and `s2`) to find the optimal alignment(s) based on the number 
    of matching bases. It iterates over possible start points for aligning `s2` with `s1` and calculates a score 
    for each alignment. The highest score(s) are stored, and all alignments with that highest score are saved 
    to a text file.

    Args:
        s1 (str): The first DNA sequence (usually the longer sequence).
        s2 (str): The second DNA sequence (usually the shorter sequence to be aligned).
        l1 (int): The length of the first DNA sequence.
        l2 (int): The length of the second DNA sequence.

    Example Output:
        Best Alignment(s):
        ...ATGC
        AGCTATGC
        4

        ....ATGC
        AGCTATGC
        4
    """
    my_best_align = []
    my_best_score = -1

    for i in range(l1):  # take all the best alignments with the highest score
        z = calculate_score(s1, s2, l1, l2, i)
        align = "." * i + s2

        if z > my_best_score:
            my_best_align = [(align, s1, z)]  # write better alignment into the list
            my_best_score = z
        elif z == my_best_score:
            my_best_align.append((align, s1, z))  # add same best score to list

    # Store the results in a plain text file
    with open('../results/Best-alignment-Results.txt', 'w') as outfile:
        outfile.write("Best Alignment(s):\n")  # write headline
        for align, s1, score in my_best_align:
            outfile.write(f"{align}\n{s1}\n{score}\n\n")  # write each alignment, sequence, and score
    print(f"Results saved to {'../results/Best-alignment-Results.txt'}")

    return 0


def main(argv):
    """
    Main entry point of the program.

    Runs the score calculation from a startpoint of 0 and then searches for the best matches.

    Parameters:
        argv (list): Command-line arguments.
    """
    best_match(s1, s2, l1, l2)
    return 0

if __name__ == "__main__":
    """Makes sure the "main" function is called from command line"""
    status = main(sys.argv)
    sys.exit(status)
