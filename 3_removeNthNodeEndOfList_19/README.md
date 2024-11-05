# 19. Remove nth Node End of List

You can refer to the problem statement [here](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/).

## My Solution

### Approach

- I maintained two pointers, `p` and `q`, both starting from the head of the list.
- I used a counter to measure the length of the list as we traverse it.
- The pointer `q` moves through the list until it reaches the end (`None`). For example, if the last element is `5`, `q` stops when it points to `5 → None`.
- **Edge Case**: If the length of the list is equal to the position of the element to be removed, we return an empty list.
- The pointer `p` is moved forward such that it stays `n-1` nodes behind the target element (one node before the target element).
- This positioning allows us to link the node before the target element to the node after it, effectively removing the target node from the list.
- Finally, we perform the linking operation and return the `head` of the modified list.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---

### Some other solution so it would give you perspective

### Approach

In this solution, we use two pointers, `R` (right pointer) and `L` (left pointer).

- We start by moving the right pointer `R` forward `n` steps in the initial loop.
- While `R` is not `null` and the right of `R` is also not `null`, we move both `R` and `L` one step forward.
- When `R` reaches the last element (i.e., points to the end of the list), the second loop ends.
- At this point, `L` stays one node behind the target node.
- We link `L` to the node after the target node, effectively removing the target node from the list.
- This completes the removal of the selected element, and the modified list is returned.

### Explanation of Pointers:

- **`R` (Right Pointer)**: Used to traverse the list and identify when to stop moving both pointers.
- **`L` (Left Pointer)**: Stops one node before the target node to allow linking to the node after the target.

By following this approach, we can efficiently remove the target element from th

**Time Complexity**: O(n)  
**Space Complexity**: O(1)
