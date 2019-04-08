from compute_levenshtein_distance import compute_levenshtein_distance as compute_dist

def align_strings(seq1, seq2):
    '''
    Calculates minimum edit distance between str1 and str2
    and saves backpointers to retrieve the allignments

    :param srt seq1: from this string
    :param srt seq2: into this string

    :returns: edit distance, a tuple of (seq1, changes)
    :rtype: a tuple of (seq1, changes)

    changes is a string where:
    "-": deletion from either seq1 or seq2
    a lowercase letter: no editing needed
    an uppercase letter: substitution or adding of this letter to seq2

    '''
    distance = 0
    alignment = ""

    if len(seq1) == 0 and len(seq2) == 0:
        return distance, (alignment, alignment)

    elif len(seq1) == 0:
        distance = len(seq2)
        alignment = seq2.upper()

    elif len(seq2) == 0:
        distance = len(seq1)
        for letter in seq1:
            alignment += '-'

    elif seq1 == seq2:
        distance = 0
        alignment = seq1

    else:

        shortest_dist, table, row, column = compute_dist(seq1, seq2)

        while True:

            if (row == 0 and column == 0):
                break

            # Make sure that i or j haven't reached 0'th row or 0'th column
            if row != 0 and column != 0 and seq2[row - 1] == seq1[column - 1]:
                alignment += seq2[row - 1]
                row = row - 1
                column = column - 1


            elif table[row][column] == (table[row - 1][column - 1] + 1):
                alignment += seq2[row - 1].upper()
                row = row - 1
                column = column - 1

            elif table[row][column] == (table[row - 1][column] + 1):
                alignment += seq2[row - 1].upper()
                row = row - 1

            elif table[row][column] == (table[row][column - 1] + 1):
                alignment += '-'
                column = column - 1

        distance = table[row][column]
        alignment = alignment[::-1]

    print("\nFrom string: ", seq1, "\nto string:", seq2,
          "\nMinimum edit distance:", distance,
          "\nChanges:", alignment)

    return distance, (seq1, alignment)

if __name__ == "__main__":
    align_strings('abcdef', 'azced')