def compute_levenshtein_distance(seq1, seq2):
    '''
    Calculates minimum edit distance between str1 and str2.
    Uses dynamic programming. Stores interemediate results in a table.

    :param str seq1: from this string
    :param str seq2: into this string

    :returns: edit distance
    :rtype: int
    '''

    # Create a table to store intermediate results
    table = [[0 for x in range(len(seq1)+1)] for x in range(len(seq2)+1)]

    for row in range(len(seq2)+1):
        for column in range(len(seq1)+1):

            if row == 0:
                table[row][column] = column

            elif column == 0:
                table[row][column] = row

            elif seq2[row-1] == seq1[column-1]  :
                table[row][column] = table[row-1][column-1]

            else:
                table[row][column] = 1 + min(table[row-1][column-1],
                                            table[row][column-1],
                                            table[row-1][column])

    return table[row][column], table, row, column


if __name__ == "__main__":
    arg1 = 'a'
    arg2 = 'aaab'
    shortest_distance = compute_levenshtein_distance(arg1, arg2)
    print("Shortest distance betweet {} and {} is {}".format(arg1, arg2,shortest_distance[0]))