# Genetic-Algorithm
This python implemented GA attempts to solve an 8x8 square puzzle containing 64 square pieces. The input file is 64 pieces in a random arrangement, with eight 4-digit numbers per line (for a total of 8 lines).
Each tile has 4 edges and is represented with 4 numbers. Each number represent the motif and there are a total of 7 motifs. The first number represents the top edge, the second number represents the right edge, the third number represents the bottom edge, and the fourth number represents the left edge.

The following steps were implemented:
- Random initialization using the input file
- Fitness evaluation of the entire population
- Parent selection using tournament selection
- Variation operators to generate offspring
- Survivor selection replacing least fit candidate solution

The algorithm is iterated multiple times to optimize the input (reduce number of edge mismatches). Parameter tuning was applied to make use of good paramter values. Th GA is succesfully able to reduce the number of mismatches but does not find the optimal solution i.e., zero edge mismatch.
