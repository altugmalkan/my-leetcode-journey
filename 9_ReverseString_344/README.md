## 344. Reverse String:

You can refer to the problem statement [here](https://leetcode.com/problems/reverse-string/description/).

### Solution: Two Pointer Approach

### Approach

- **Initialize Two Pointers**:

  - `l` (left pointer) starts at the beginning of the array (`0`).
  - `r` (right pointer) starts at the end of the array (`s.Length - 1`).

- **Swap Elements**:

  - Use a `while` loop to iterate as long as `l` is less than `r`.
  - During each iteration:
    - Store the character at `s[l]` in a temporary variable `temp`.
    - Assign the value of `s[r]` to `s[l]`.
    - Assign the value of `temp` (original `s[l]`) to `s[r]`.
    - Increment `l` and decrement `r` to move the pointers closer to the center of the array.

- **End of the Loop**:
  - The loop ends when `l` is no longer less than `r`, meaning all the characters have been swapped, and the string is fully reversed in place.

### Complexity Analysis:

- **Time Complexity**: O(n), where `n` is the length of the string. We perform a single pass through half the array, swapping characters.
- **Space Complexity**: O(1), as the reversal is done in place without using additional space.

This approach efficiently reverses the string in place using the two-pointer technique.

---

### Solution 2: Using a Stack

### Approach

- **Use a Stack for Reversal**:

  - Initialize a `Stack<char>` to store characters from the input array `s`.
  - Use a `foreach` loop to push each character of `s` onto the stack.

- **Rebuild the Array**:
  - Use a `for` loop to iterate through the input array `s` by index.
  - For each index `i`, replace the character at `s[i]` with the character popped from the stack. This effectively reverses the order of the characters.

### Complexity Analysis:

- **Time Complexity**: O(n), where `n` is the length of the string. We iterate through the string twice: once to push all characters onto the stack and once to pop them back.
- **Space Complexity**: O(n), as the stack requires additional space to store all characters in the array.

This approach leverages a stack to reverse the string, which is simple and intuitive but uses additional space.
