# Below are the python scripts for the CMEEcoursework Groupwork Practicals in Python week 2:
- Authors: Laiyin Zhou, Yaxin Liu, Sebastian Dohne and Yangfeng Wang
- Languages used: Python

## Groupwork Practicals: Groupwork Practical on Align DNA sequences, Groupwork Practical on Missing oaks problem

# align_seqs_better.py

## Description

A Python script that reads two DNA sequences from FASTA files, aligns them using a custom scoring function, and identifies the best-scoring alignments. The results are displayed in the console and saved in a text file (.txt).

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

### Missing oaks problem

- **Description**:  
  This Python script identifies rows where the genus is 'Quercus' (oak) in a CSV dataset and saves these rows to a new output file. It reads from an input CSV, checks each row for the genus, and writes matching rows to an output CSV without the header.

  - **Script Information**:
    - **Script Name**: Missing_oaks_problem.py
    - **Authors**: Yaxin Liu (yaxin.liu24@imperial.ac.uk), Laiyin Zhou (l.zhou24@imperial.ac.uk), Sebastian Dohne (sebastian.dohne24@imperial.ac.uk), Yanfeng Wang (yanfeng.wang24@imperial.ac.uk)
    - **Version**: 0.0.1

  - **Functions and Workflow**:
    - **Read Input**: Reads the input CSV file `TestOaksData.csv` from the `../data` directory.
    - **Filter for Oaks**: Processes each row, checking if the genus is 'Quercus'. Matching rows are added to a list called `oaks`.
    - **Write Output**: Writes each oak entry to an output file `oaks.csv` located in the `../results` directory.

  - **Arguments**:  
    No command-line arguments are required.

- **Dependencies**:  
  Requires Python 3 and uses standard libraries:
  - `csv`: To read and write CSV files.
  - `os`: To ensure output directories exist.

- **Usage**:  
  1. Run the script using:
     ```bash
     python3 missing_oaks.py
     ```
  - The script will:
    - Read and filter oak entries from `../data/TestOaksData.csv`.
    - Write the filtered entries to `../results/oaks.csv`.

- **Additional Notes**:  
  - The script will create the `../results` directory if it does not already exist.
  - Ensure that `TestOaksData.csv` is available in the specified input directory (`../data`) before running the script.
  - This script omits headers in the output file by design, only including oak entries.

  
