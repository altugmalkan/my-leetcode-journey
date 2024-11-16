## 287. Find the Duplicate Number:

You can refer to the problem statement [here](https://leetcode.com/problems/find-the-duplicate-number/description/).

### Solution 1: Using Sorting

### Approach

- **Sort the Array**:
  - The input list `nums` is sorted, which allows us to easily find duplicates by comparing adjacent elements.
- **Iterate Through the Sorted List**:
  - Traverse through the array and check if any two consecutive elements are the same.
  - **If they match**, return the duplicate element.

### Complexity Analysis:

- **Time Complexity**: O(n log n) due to the sorting step.
- **Space Complexity**: O(1) (ignoring the space used by the sort function).

---

### Solution 2: Using a List for Tracking Seen Elements

### Approach

- **Initialize an Empty List**:
  - Create an empty list `list` to keep track of seen numbers.
- **Iterate Through `nums`**:
  - For each number `num` in `nums`:
    - **If `num` is already in `list`**, return `num` as it is the duplicate.
    - Otherwise, append `num` to `list`.
- **Return Result**:
  - The function returns as soon as a duplicate is found.

### Complexity Analysis:

- **Time Complexity**: O(n) for iterating through the list and checking membership.
- **Space Complexity**: O(n) for storing the list of seen numbers.

---

### Solution 3: Floyd's Cycle Detection Algorithm (Tortoise and Hare Method)

### Approach

- **Two Pointers (Slow and Fast)**:
  - Initialize `slow` and `fast` pointers at the start of the list.
- **Phase 1: Detect the Cycle**:
  - Move `slow` by one step and `fast` by two steps until they meet, indicating the presence of a cycle.
- **Phase 2: Find the Entry Point of the Cycle**:
  - Reset `slow` to the start and move both `slow` and `fast` by one step until they meet again. The meeting point is the duplicate number.
- **Return Result**:
  - Return `slow` as it represents the duplicate number.

### Complexity Analysis:

- **Time Complexity**: O(n) as we traverse the list a constant number of times.
- **Space Complexity**: O(1) as no additional space is used.
