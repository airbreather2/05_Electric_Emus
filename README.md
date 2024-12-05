# CMEE Coursework Groupwork Practicals - Python Week 2

- **Authors**: Laiyin Zhou, Yaxin Liu, Sebastian Dohne, and Yangfeng Wang
- **Languages**: Python, R, Latex

## Groupwork Practicals
This repository contains these main groupwork practicals:
1. **Align DNA Sequences**
2. **Missing Oaks Problem**
3. **Visuaising regression groupwork**
4. **KeyWestAnnualMeanTemperature.R**
5. **TAutoCorrLatexCode.tex**
---

## align_seqs_better.py

- **Description**:  
  A Python script that reads two DNA sequences from FASTA files, aligns them using a custom scoring function, and identifies the best-scoring alignments. The results are displayed in the console and saved in a text file.

- **Features**:
  - Reads DNA sequences from FASTA files.
  - Calculates alignment scores.
  - Displays best alignments.
  - Saves best alignments in a binary file.

- **Modules Used**:
  - **ipdb**: Debugging tool.
  - **os**: Handles file path manipulation and directory creation.
  - **sys**: Accesses command-line arguments and system parameters.
  - **csv**: Reads from and writes to CSV files.

- **Installation**:
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

- **Usage**:
  - Specify FASTA files via command line, or use defaults from `../data/`.
  - **Command-line Usage**:
     ```bash
     python3 align_seqs_better.py <fasta_file_1> <fasta_file_2>
     ```

---

## Missing_oaks_problem.py

- **Description**:  
  This Python script identifies rows where the genus is 'Quercus' (oak) in a CSV dataset and saves these rows to a new output file. It reads from an input CSV, checks each row for the genus, and writes matching rows to an output CSV without the header.

- **Script Information**:
  - **Script Name**: `Missing_oaks_problem.py`
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
  - Run the script using:
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
  

### PP_Regress_loc.R

- **Description**:  
  This script generates multiple plots containing linear regressions of predator and prey masses grouped by predator lifestage and feeding type by location from the EcolArchives-E089-51-D1 dataset. It also calculates regression coefficients for each group and saves them to a CSV file.

  - **Functions**:
    - The script does not define reusable functions but performs the following tasks:
      - Creates a combined dataset with log-transformed predator and prey masses.
      - Identifies groups with insufficient data for regression.
      - Generates regression plots faceted by feeding interaction type.
      - Saves regression results to a CSV file.

  - **Arguments**:  
    This script does not require any arguments when running.

- **Dependencies**:  
  - `ggplot2`: For data visualization.
  - `dplyr`: For data manipulation.
  - `broom`: For organizing regression results.
  - `purrr`: For functional programming operations.

- **Usage**:  
  - To run the script, use the following command in a terminal:
     ```bash
     Rscript PP_Regress_loc.R
     ```
  - The script will:
    - Load the dataset and preprocess it.
    - Generate a PDF file with regression plots (`test_Visualising_regression_analysis.pdf`).
    - Save a CSV file containing regression coefficients (`PP_Regress_bylocation_Results.csv`).
      
### KeyWestAnnualMeanTemperature.R

- **Description**:  
This script evaluates the correlation between consecutive years' annual mean temperatures in Key West using a permutation test. It computes the observed correlation coefficient, generates a null distribution, and calculates an approximate p-value. The results are visualized in a histogram saved as a PDF.

- **Dependencies**:
  - base (core R functions like cor and sample)
  - graphics (for plotting)

- **Usage**:
  - Run the script with:
  ```bash
  Rscript KeyWestAnnualMeanTemperature.R
  ```

  - The script will:
    - Load the dataset KeyWestAnnualMeanTemperature.RData.
    - Compute the observed correlation coefficient.
    - Perform a permutation test with 10,000 iterations.
    - Save a histogram of correlation coefficients to ../results/Coefficients.pdf.

## TAutoCorrLatexCode.tex

- **Description**:
This LaTeX document generates a report analyzing the correlation between annual mean temperatures in Key West.

- **Dependencies**:
  - LaTeX distribution: Ensure you have a LaTeX compiler such as pdflatex, xelatex, or lualatex installed.
  - Packages:
    - 'geometry':for setting page margins
    - 'setspace':for controlling line spacing
    - 'graphicx':for inserting images
    - 'amsmath' :for mathematical expressions

- **Usage**:
To compile the LaTeX file and generate a PDF
  - Input:
    - The script references the histogram plot Coefficients.pdf located in the ../results directory. Ensure this file exists (run "KeyWestAnnualMeanTemperature.R" first) before compiling the LaTeX document.
  - Output:
    - If you want the output PDF to be saved in a specific directory (e.g., ../results), compile with the following command in terminal:
   ```bash
   pdflatex -output-directory=../results TAutoCorrLatexCode.tex
   ```
