#!/usr/bin/env Rscript
# Author: 'Laiyin Zhou (l.zhou24@imperial.ac.uk), Sebatian Dohne (sebastian.dohne24@imperial.ac.uk), Yanfeng Wang (yanfeng.wang24@imperial.ac.uk), Yaxin Liu (yaxin.liu24@imperial.ac.uk)'
# Script: TAutoCorr.R.
# Description: This script evaluates the correlation between consecutive years' annual mean temperatures in Key West using a permutation test.  
# Arguments: None
# Date: Nov 2024
#dependencies: core R functions like cor and sample; graphics (for plotting)

# Usage:
# 
# 
# To run the script:
# Rscript TAutoCorr.R
#
# No arguments are required for running this script.

# Load and explore data

rm(list=ls())

load("../data/KeyWestAnnualMeanTemperature.RData")
ls()

class(ats)
head(ats)

plot(ats)


# Calculate the observed correlation coefficient
observed_cor <- cor(ats$Temp[-1], ats$Temp[-length(ats$Temp)])
observed_cor

# Perform permutation testing
set.seed(12345)
n_permutations <- 10000  # Define the number of permutations
permuted_cors <- numeric(n_permutations)  # To store correlation coefficients from permutations

for (i in 1:n_permutations) {
  # Randomly shuffle the temperature values
  permuted_temps <- sample(ats$Temp) 
  # Calculate correlation for the permuted time series
  permuted_cors[i] <- cor(permuted_temps[-1], permuted_temps[-length(permuted_temps)])
}

# Calculate the approximate p-value
p_value <- sum(permuted_cors >= observed_cor) / n_permutations

# Display results
cat("Observed correlation coefficient:", observed_cor, "\n")
cat("Approximate p-value:", p_value, "\n")


# Plot histogram of permuted correlations
output_dir <- "../results" # Define the results directory
pdf(file = file.path(output_dir, "Coefficients.pdf"), width = 8, height = 6) # Save the plot as PDF

# Generate the plot
hist(permuted_cors, breaks = 30, col = "lightblue", main = "",
     xlab = "Correlation Coefficient")
abline(v = observed_cor, col = "red", lwd = 2, lty = 2)
legend("topleft", legend = c("Observed Correlation"), col = "red", lty = 2, lwd = 2)
text(x = max(permuted_cors) - 0.2, 
     y = max(hist(permuted_cors, breaks = 30, plot = FALSE)$counts) * 0.8, 
     labels = expression(italic(p) == "6 × 10"^-4), 
     pos = 4, cex = 1.2)

dev.off()
