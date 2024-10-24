# Below are the python scripts for the CMEEcoursework Groupwork Practicals in Python week 2:
- Authors: Laiyin Zhou, Yaxin Liu, Sebastian Dohne and Yangfeng Wang
- Languages used: Python

## Groupwork Practicals: Groupwork Practical on Align DNA sequences, Groupwork Practical on Missing oaks problem

# align_seqs_better.py

## Description

A Python script that reads two DNA sequences from FASTA files, aligns them using a custom scoring function, and identifies the best-scoring alignments. The results are displayed in the console and saved in a binary file using `pickle`.

## Features

- Reads DNA sequences from FASTA files.
- Calculates alignment scores.
- Displays best alignments.
- Saves best alignments in a binary file.

## Modules Used

- **ipdb**: Debugging tool.
- **os**: Handles file path manipulation and directory creation.
- **sys**: Accesses command-line arguments and system parameters.
- **csv**: Reads from and writes to CSV files.

## Installation

To install and run the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd /path/to/your/project
    ```

3. Install dependencies if required (optional):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Specify FASTA files via command line, or use defaults from `../data/`.

### Command-line Usage

```bash
python3 align_seqs_better.py <fasta_file_1> <fasta_file_2>

  
