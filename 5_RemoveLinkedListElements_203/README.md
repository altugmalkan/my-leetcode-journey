## 203. Remove Linked List Elements:

You can refer to the problem statement [here](https://leetcode.com/problems/remove-linked-list-elements/description/).

### Approach

In this solution, we use a `prev` node and a `curr` pointer to traverse the linked list and remove elements with the specified value.

- **Initial Setup**:

  - A dummy `prev` node is created and linked to the `head`. This helps handle edge cases where the `head` itself needs to be removed.
  - The `curr` pointer is initialized to start at `prev`, effectively placing it before `head`, allowing us to check if `head` holds the target value.

- **Iterate Through the List**:

  - As we traverse the list using `curr`, we check if the next node contains the value we want to remove.
  - **If the next node's value matches the target (`val`)**:
    - We remove it by reassigning `curr.next` to `curr.next.next`, bypassing the node and severing the link to it.
  - **If the next node's value does not match the target**:
    - We simply move `curr` forward to the next node.

- **Return Result**:
  - Once the loop completes, we return `prev.next`, which points to the potentially modified `head` of the list.

### Complexity Analysis:

- **Time Complexity**: O(n), where `n` is the number of nodes in the list. We iterate through the list once.
- **Space Complexity**: O(1), as no additional space is used apart from pointers.
