def longest_common_subsequence(X, Y):
    # ToDo 
    # Get lengths of both strings
    m, n = len(X), len(Y)

    # Create a DP table initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Length of LCS
    lcs_length = dp[m][n]

    # To find the actual LCS, backtrack
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the LCS since we built it backwards
    lcs.reverse()

    return lcs_length

#testing
""" X = "cloud"
Y = "loud"
lcs_length = longest_common_subsequence(X, Y)
print(lcs_length)  # Output: 4
lngth = longest_common_subsequence("dynamicprogramming", "machinelearning")
print(lngth) """
