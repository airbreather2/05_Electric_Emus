
# Electric Emus Final Assessment and Feedback

## Feedback on Project Structure and Workflow

### Strengths:
1. **Directory Structure**: The project used a clear and logical directory structure (`code`, `data`, `results`, etc.). 
2. **.gitignore**: Properly excluded unnecessary files, such as temporary LaTeX files and intermediate outputs in the `results` directory.
3. **README.md**:
   - Contained author details and clear descriptions of scripts.
   - Provided basic usage instructions for most scripts.

### Areas for Improvement:
1. **README.md Enhancements**:
   - Include input/output examples for each script to assist users in understanding their functionality.
   - Expand the "Dependencies" section to include installation instructions for required R and Python libraries.
2. **Results Directory**:
   - Avoid committing generated files (e.g., `Coefficients.pdf`, `Best-alignment-Results.txt`) to Git. Only keep a `.gitkeep` file.

---

## Feedback on Code Structure, Syntax, and Errors

### General Observations:
1. Scripts included detailed docstrings, improving readability and reusability.
2. Modular design was inconsistent—some scripts (e.g., `align_seqs_better.py`) were well-structured, while others lacked reusable functions (reflecting the starting point/scripts you were given).

### Script-Specific Feedback:

#### **PP_Regress_loc.R**
- **Strengths**:
  - Implemented regression analysis effectively with robust data manipulation using `dplyr`.
  - Saveed results in a well-structured CSV file.
- **Improvements**:
  - Add inline comments explaining critical steps (e.g., `filter(sd(Prey.mass) > 0)`).
  - Use `tryCatch` to handle potential errors in `lm()` when fitting models.

#### **TAutoCorr.R**
- **Strengths**:
  - Calculateed permutation p-values efficiently.
  - Outputed visualizations and numerical results clearly.
- **Improvements**:
  - Add input validation for the loaded dataset (`ats`) to check for missing columns or incorrect formats.
  - Include comments explaining key steps in the permutation test.
  - Compare with provided solution script. 

#### **align_seqs_better.py**
- **Strengths**:
  - Implemented robust error handling for file input/output operations.
  - Included detailed docstrings for all functions.
- **Improvements**:
  - Replace hardcoded default file paths with a configuration file or command-line arguments.
  - Optimize redundant loops in `best_match`.

#### **Groupwork_oaks_debugme.py**
- **Strengths**:
  - Uses `doctest` for function validation.
  - Writes clean and concise output files.
- **Improvements**:
  - Use `logging` instead of `print` for debugging and status messages.
  - Add error handling for malformed CSV files.

#### **TAutoCorrLatexCode.tex**
- **Strengths**:
  - The report is well-written with clear sections for Introduction, Results, and Conclusion.
  - Includes a concise explanation of the permutation test methodology.
- **Improvements**:
  - Add references to relevant literature on temperature autocorrelation studies.
  - Verify that all figures referenced in the document exist before compilation.

---

## Florida Autocorrelation Practical

### Feedback on Code:
1. **Strengths**:
   - The `TAutoCorr.R` script correctly implements a permutation test and generates informative visualizations.
   - Efficient use of vectorized operations in R enhances performance.

2. **Areas for Improvement**:
   - Add a function to calculate p-values for different numbers of permutations (e.g., 1,000, 10,000, etc.).
   - Include descriptive labels in the histogram to make the plot more informative.

### Feedback on Write-Up:
- The LaTeX report provided a succinct explanation of the practical and its findings. 
- Suggested enhancements:
  - Include a discussion on potential limitations of the permutation approach.
  - Relate findings to broader climatic patterns or hypotheses.
  - Could have discussed the autocorrelation issue more in terms of underlying factors and analytical methods.   
---

## Git Practices

### Strengths:
1. Regular commits demonstrated consistent progress.
2. `.gitignore` effectively managed excluded files.

### Areas for Improvement:
1. Commit messages:
   - Many messages (e.g., "final version") are vague. Use detailed messages describing changes (e.g., "Add permutation test for autocorrelation analysis").
2. Contributions:
   - **Yaxin** contributed extensively to Python and R scripts but could improve commit quality.
   - **Sebastian** made key contributions to LaTeX documents.
   - **Laiyin** and **Yanfeng** focused on specific scripts (e.g., `align_seqs_better.py` and `Groupwork_oaks_debugme.py`) but had fewer commits.

### Recommendations:
1. Adopt a branching strategy (e.g., feature branches) to isolate changes and avoid conflicts.
2. Use tags for major milestones (e.g., `v1.0`).

---

## Conclusion
Your group demonstrated strong programming and analytical skills, with clear improvements in documentation and workflow over time. Great job collaborating, and hopefully this exercise gave you a useful experience in the process of collaborative code development.