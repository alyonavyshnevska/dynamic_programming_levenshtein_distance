# Levenshtein Edit Distance

In information theory, linguistics and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

Mathematically, the Levenshtein distance between two strings _a_, _b_ (of length | a | and | b | respectively) is given by _lev_ <sub> _a,b_ </sub> (|_a_|,|_b_|) where




![levenshtein formula](docs/levenshtein-formula.svg)

![levenshtein formula_explain](docs/levenshtein-formula-explain.jpeg)

Note that the first element in the minimum corresponds to deletion (from _a_ to _b_), the second to insertion and the third to match or mismatch, depending on whether the respective symbols are the same.


There are two ways to calculate this distance:

- naive recursive implementation of the math formula
- dynamic programming algorithm that uses a table to avoid extra computations

Here, I implement the second way because it is more efficient.

## Design

1. Construct an empty table: list of lists of ints.
    -  Num of rows = target string seq2. len(seq2) + 1 (plus one in case the input is 0)
    - Num of cols = original string seq1. len(seq1) + 1 (plus one in case the input is 0)

2. For each char in target string (row):

        For each char in original string (column):
            if row is 0:
                set cell to the value of column (insertion needed, no char in row to edit)
            if column is 0:
                set cell to the value of row (insertion needed, no char in column to edit)
            if the chars align:
                copy the min edit distance from char at previous row and char at previous column
            if chars don's allign:
                choose either to edit, to delete or to insert (whichever option yiels
                the smallest edit distance)


 3. Return last value at last row, last column



### Data Structures

1. Table: list of lists of ints.   
Rows: chars of "To" string (seq2).
Columns: chars of "From" string (seq1).

2. Sequence: string.
