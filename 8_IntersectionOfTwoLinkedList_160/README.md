## 160. Intersection of Two Linked Lists:

You can refer to the problem statement [here](https://leetcode.com/problems/intersection-of-two-linked-lists/description/).

### Solution: Two Pointer Approach

### Approach

- **Handle Edge Cases**:
  - If either `headA` or `headB` is `None`, return `None` as there can be no intersection.
- **Initialize Two Pointers**:

  - Set `xPtr` to start at `headA` and `yPtr` to start at `headB`.

- **Traverse the Lists**:

  - Move both `xPtr` and `yPtr` one step at a time through their respective lists.
  - If a pointer reaches the end of its list:
    - Redirect it to the head of the other list.
  - This ensures that both pointers traverse the same total number of nodes, even if the lists have different lengths.

- **Find the Intersection**:
  - The loop continues until `xPtr` and `yPtr` meet at the intersection node or both become `None` (indicating no intersection).
  - Return either `xPtr` or `yPtr` as they will be the same when an intersection is found.

### Complexity Analysis:

- **Time Complexity**: O(m + n), where `m` is the length of `headA` and `n` is the length of `headB`. Each pointer traverses both lists fully.
- **Space Complexity**: O(1), as no additional space is used beyond the two pointers.

This approach efficiently finds the intersection node, if it exists, without requiring additional data structures or modifying the input lists.
