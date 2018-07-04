def levenshtein_distance(w1, w2):
    mat = [[0 for _ in range(len(w2) + 1)] for _ in range(len(w1) + 1)]
    for i in range(len(w1) + 1):
        for j in range(len(w2) + 1):
            if i == 0 and j == 0:
                mat[i][j] = 0
            elif i == 0 and j != 0:
                mat[i][j] = j
            elif j == 0 and i != 0:
                mat[i][j] = i
            else:
                if w1[i - 1] == w2[j - 1]:
                    mat[i][j] = min(mat[i - 1][j - 1],
                                    mat[i - 1][j - 1] + 1,
                                    mat[i - 1][j] + 1,
                                    mat[i][j - 1] + 1)
                else:
                    mat[i][j] = min(mat[i - 1][j - 1] + 1,
                                    mat[i - 1][j] + 1,
                                    mat[i][j - 1] + 1)
    return mat[len(w1)][len(w2)]
