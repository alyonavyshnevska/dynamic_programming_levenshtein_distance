# Levenshtein Edit Distance 

In information theory, linguistics and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. 

Mathematically, the Levenshtein distance between two strings $a$ , $b$ (of length $| a |$ and $| b |$ respectively) is given by $ {\displaystyle \operatorname {lev} _{a,b}(|a|,|b|)}$ where 




![levenshtein formula](docs/levenshtein-formula.svg)

 ${\displaystyle 1_{(a_{i}\neq b_{j})}}$ is a function that equals 0 when $a_{i}=b_{j}$ and 1 otherwise.
 $\operatorname{lev}_{a,b}(i,j)$ is the distance between the first $i$ characters of $a$ and the first $j$ characters of $b$.

Note that the first element in the minimum corresponds to deletion (from $a$ to $b$), the second to insertion and the third to match or mismatch, depending on whether the respective symbols are the same.


There are two ways to calculate this distance:

- naive recursive implementation of the math formula
- dynamic programming algorithm that uses a table to avoid extra computations

Here, I implement the second way because it is more efficient.