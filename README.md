# Gene Relationships Analyzer
This project implements a robust Python-based solution for analyzing the **Longest Common Subsequences (LCS)** between arbitrary strings. It includes features for computing all LCSs, visualizing relationships through an LCS matrix, and proposing strategies to reconstruct genealogical relationships between strings.

---

## Features:

- **LCS Finder**: Efficiently computes **all** Longest Common Subsequences and their lengths for any two given strings.
- **Validation**: Includes multiple **test cases** to ensure correctness of the LCS algorithm.
- **LCS Length Matrix**: Generates a **7x7 matrix** (`len_lcs_matrix`) using NumPy, where each cell represents the LCS length between a pair of strings in a given set.
- **Relationship Analysis**: Uses the LCS length matrix to explore **string similarity**, identify **related string groups**, and infer **genealogical relationships**.
- **Local & Global Strategies**: 
  - Implements a **local strategy** for inferring ancestry using greedy comparisons between neighbors.
  - Proposes a **global strategy** leveraging overall structure and metrics for optimal tree reconstruction.

---

## Test Cases:

Several built-in test cases demonstrate the correctness of the LCS function across diverse string pairs, covering:
- Identical strings
- Partially overlapping strings
- Completely disjoint strings

---

## Strategy Overview:

### Local Strategy (Greedy Heuristic)
- Compares each string to its immediate neighbors (e.g., parent-child).
- Builds branches of the genealogy tree based on **maximum local similarity**.
- Greedy property: selects the most similar neighbor without considering downstream impact.

### Global Strategy (Global Optimization)
- Constructs the entire tree by minimizing global dissimilarity or maximizing global similarity.
- Inspired by metrics like **least total distance**, or similarity score aggregation.
- Utilizes the full `len_lcs_matrix` to generate an optimized binary tree that captures ancestral relationships.

---

## Matrix Properties:

- `len_lcs_matrix` is a **NumPy 2D array** of shape `(7, 7)`.
- Symmetric with zeros on the diagonal (comparing each string with itself).
- Used to infer which strings are more strongly related and to construct genealogical trees based on similarity metrics.

---

## Example Usage:

```python
from lcs_utils import find_all_lcs, generate_lcs_matrix, analyze_relationships

# Example: Compute LCS between two strings
lcs_list, lcs_length = find_all_lcs("abcde", "acebd")
print(lcs_list, lcs_length)

# Generate matrix for a set of 7 strings
len_lcs_matrix = generate_lcs_matrix(set_strings)

# Analyze relationships
local_tree = build_local_genealogy(set_strings, len_lcs_matrix)
global_tree = build_global_genealogy(set_strings, len_lcs_matrix)
