def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    # Create a 2D array to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Length of LCS is dp[m][n]
    lcs_length = dp[m][n]

    # Optional: Retrieve the LCS itself
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    return lcs_length, ''.join(lcs)

# Example usage
if __name__ == "__main__":
    X = "cloud"
    Y = "loud"
    length, lcs = longest_common_subsequence(X, Y)
    print(f"Length of LCS: {length}")
    print(f"LCS: {lcs}")
