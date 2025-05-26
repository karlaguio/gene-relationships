def longest_common_subsequences(x, y):
    """
    Computes the longest common subsequences (LCS) between two strings.

    This function finds all the possible longest common subsequences between two input strings
    using dynamic programming, and returns the sequences along with their length.

    Parameters
    ----------
    x : str
        The first string to compute the LCS.
    y : str
        The second string to compute the LCS.

    Returns
    ----------
    all_lcs : tuple
        A tuple containing:
        - A list of all the possible LCSs, sorted lexicographically.
        - The length of the longest common subsequences.

    Notes
    -----
    If no common subsequence exists, the function returns (None, 0).
    """
    # Step 1: Initialize the DP table
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Backtrack to find all LCSs
    def backtrack(i, j):
        """
        Recursively backtracks through the DP table to find all the longest common subsequences.

        Parameters
        ----------
        i : int
            The current index in string x.
        j : int
            The current index in string y.

        Returns
        -------
        set
            A set of all possible subsequences found from the current indices.
        """
        # Base case
        if i == 0 or j == 0:
            return {""}

        if x[i - 1] == y[j - 1]:
            # If characters match, include it in the LCS
            return {s + x[i - 1] for s in backtrack(i - 1, j - 1)}
        else:
            # Otherwise, explore both options and merge the results
            lcs_set = set()
            if dp[i - 1][j] >= dp[i][j - 1]:
                lcs_set.update(backtrack(i - 1, j))
            if dp[i][j - 1] >= dp[i - 1][j]:
                lcs_set.update(backtrack(i, j - 1))
            return lcs_set

    # Step 4: Collect all LCSs and return the result
    all_lcs_set = backtrack(m, n)
    all_lcs = sorted(list(all_lcs_set))  # Sort lexicographically for consistency
    lcs_length = dp[m][n]

    # Step 5: Return the results
    if lcs_length == 0:
        return (None, 0)
    return (all_lcs, lcs_length)

# Test cases
x1, y1 = 'ABCBDAB', 'BDCABA'
x2, y2 = 'abc', ''
x3, y3 = 'abc', 'a'
x4, y4 = 'abc', 'ac'

# Verify outputs
result1 = longest_common_subsequences(x1, y1)
result2 = longest_common_subsequences(x2, y2)
result3 = longest_common_subsequences(x3, y3)
result4 = longest_common_subsequences(x4, y4)

# Ensure order and content match
assert result1 == (['BCAB', 'BCBA', 'BDAB'], 4), f"Test Case 1 Failed: {result1}"
assert result2 == (None, 0), f"Test Case 2 Failed: {result2}"
assert result3 == (['a'], 1), f"Test Case 3 Failed: {result3}"
assert result4 == (['ac'], 2), f"Test Case 4 Failed: {result4}"

print("All test cases passed successfully!")

import numpy as np

# Given set of strings
set_strings = [
    ('a', 'ATGGTGCGAAAGCATCTCTTTTCGTGGCGTGATAAGTTTTATGGTATCCCCGGACGTTGGCTACTACAATTCTCCGAAGTATAAGTGAGTAGGATATGTCAATAACAAGAGGGGATGCGTGACGCATTAGCACCAACTGAATCAAACGATAACTAACGTGGTTTCAGTGAGCGTATGTGGCAAAGGATTGGATACATTTTTCGAGCACGTCTACATAATGACCGTGACAATACTGGAGACTCCGTACCGTCATCTTGACACTCCT'),
    ('b', 'TGGTGCGAAAGCATCTCTTTTCCGTGGCGTATAGTTTTATGGTATCCCCGGAACGCTGGCTACTACAATCTCCGAAGTATAGAGTGAGTAGATTTAATTAACAGAGGGCGTCGTTGACGCATTAGCACCAACTGAATCAACCGATAACTTAACGTGGGTTTCAGTGACTATAGGGCAAAGGATGAACATTTTCGAGCAGCTCTAATAATGAGCGTGACAATATGAATCCACACCGTCATCTTGAACTCCT'),
    ('c', 'TCTGTGCGATATACATCTCTATCGTTGCGGTATGTTTTATGTGCATCACCCCACGCGCTGGCTACAGTACAATCTGCTGGAAGTACTAGGTGGTAGTTAATAACTAGGGTGCGTCGTTGCGCATTACACAACTGGACAACCACTTAACTGGGGTAATCAGTGTTTAGGGCAGACAAGATGAAAACAAGTTTTCGAGCAGGCTCCTATAATGAGGACGGAACGTTAATAAATCCAACACCGCACTGCTTCGTAACCCT'),
    ('d', 'ATGAGGCGCAAAATTCTCTTTCTCGTGGCGCTGATTAAGTTTTATGTATCCCCGGACGTTGGCTACTGACAATTGCTCCGAAGTATAAAGTAGTAGGATATGTCAATAACAAAGACGGGGATAGCGTGACAGCATTAGAACGCAACTGGAATCAAACGTAACCTAAAGGGTTGTCAGGAGCGTATGTGGTCAAAAAGGATTGGATGACATTTTTCGACACGTCTACATAATGACCTGTGACAAACTAGGAGACCTCCTACTCGGTCAATCTTGACGACTCCT'),
    ('e', 'TGGTGCGATATACATCTCTTTTCGTGCGTATGTTTTATGGTGATCACCCGGAACCGCTGGCTACATACAATCTCTGGAAGTACTAGGTGGTAGTTTAATAACTAGAGGTGCGTCGTTGACGCATTACACAACTGGATCAACCGAACTTAACTGGGTATCAGTGATATAGGGCGACAAGATGAACAATTTTCGAGCAGCTCCTGAATAATGAGACGGAACGTATAATCCAACACCGTCACTGCTTCGAACCCT'),
    ('f', 'GGGGGAAAGCGATCCCTTATCGTGGCTGTGATAAGTTTTTATCGGGTATCCGCCGGACGTTGGCGTACTACAATTCTCCGAAGTTAAGTGAGTTAGGGATATAGTCAATAACAAGAGGGGATTGTCGTGACGCATAGCACACAACTGAATCAAATCGATAACTAAACGGGTTTCAGTAGAGCGTTGTGGCAAAGATTGGATACATTTTTCGCAGGACGTCTTACCTAATGACGTGGACAATAACTGGCAGACGTCCGTACCGTCATCTTGACCACTCCCT'),
    ('g', 'TGGTGCGATATACATCCTCTTTTCGTGCGTATGTTTTAGGTACACCGGATACGCCTGGCTTACAAGTACCAATCTCTGAGAAGTCACTGAGGTGGTAGTTTAATAACTAGAAGGGTGCGTCGGACGCATTCACACATACTGGATCAACCGAGACTTAACTGGGGTATCAGTGATTGATAGGGCGACAAGATATACAATTTTCGAGCAGCTCCCTGAATAAGTGAAGAACGGAGACGTATAATCCAACACGATTCACTGCTTCGAACCCT')
]

# Extract only the sequences
sequences = [seq for _, seq in set_strings]

def lcs_length(x, y):
    """
    Calculates the length of the longest common subsequence (LCS) between two strings.

    This function uses dynamic programming to compute the length of the LCS between
    two input strings by filling up a 2D matrix with the LCS lengths at each step.

    Parameters
    ----------
    x : str
        The first string to compute the LCS.
    y : str
        The second string to compute the LCS.

    Returns
    -------
    int
        The length of the longest common subsequence between x and y.
    """
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table to find LCS length
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Generate the LCS length matrix
def generate_lcs_matrix(sequences):
    """
    Generates a matrix of LCS lengths between all pairs of sequences.

    This function computes the LCS lengths for all pairs of sequences in the input
    list of sequences and stores the results in a 2D matrix.

    Parameters
    ----------
    sequences : list of str
        List of strings for which the pairwise LCS lengths are calculated.

    Returns
    -------
    np.ndarray
        A 2D numpy array where each element [i, j] represents the LCS length
        between sequences[i] and sequences[j].
    """
    num_strings = len(sequences)
    len_lcs_matrix = np.zeros((num_strings, num_strings), dtype=int)

    for i in range(num_strings):
        for j in range(num_strings):
            len_lcs_matrix[i, j] = lcs_length(sequences[i], sequences[j])

    return len_lcs_matrix

# Calculate LCS length matrix
len_lcs_matrix = generate_lcs_matrix(sequences)

# Print the LCS length matrix
print("LCS Length Matrix:")
print(len_lcs_matrix)
