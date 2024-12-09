## 69. Sqrt(x):

You can refer to the problem statement [here](https://leetcode.com/problems/sqrtx/description/).

### Solution: Binary Search Approach

### Approach

- **Initialize Left and Right Pointers**:
  - Start with `left` set to `0` and `right` set to `x` (the input value). These pointers define the range within which we search for the square root.
- **Binary Search**:
  - Calculate the `mid` value as the average of `left` and `right`.
  - Check the square of `mid`:
    - **If `mid * mid` equals `x`**, return `mid` as the square root.
    - **If `mid * mid` is greater than `x`**, move the `right` pointer to `mid` to search in the lower half.
    - **If `mid * mid` is less than `x`**, move the `left` pointer to `mid + 1` to search in the upper half.
- **Return Result**:
  - Once the loop ends, `left - 1` represents the largest integer less than or equal to the square root of `x`. Alternatively, `right` will hold the same value.

### Complexity Analysis:

- **Time Complexity**: O(log x), as we are performing a binary search, halving the search range at each step.
- **Space Complexity**: O(1), since the operation is performed in place with no additional space required.
