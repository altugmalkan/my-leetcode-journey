26. Remove Duplicates from Sorted Array

You can refer to the problem statement [here](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/).

## Solution using additional space (dictionary-hashMap) :

### Approach

In this solution, I use a dictionary to track unique elements in the list and rearrange the list in-place to remove duplicates.

- **Initialize Variables**: I start by defining a dictionary `unique` to store each unique element encountered, and a counter `k` to keep track of the position in the list where the next unique element should be placed.
- **Loop Through `nums`**: For each element `num` in the list `nums`, I check if it has already been encountered by looking it up in the `unique` dictionary.
- **Add Unique Elements**: If `num` is not in `unique`, it means it’s a unique element:
  - I add `num` to the `unique` dictionary to mark it as encountered.
  - Then, I place `num` at the `k`-th position in the `nums` list.
  - Finally, I increment `k` to point to the next position for a unique element.
- **Return `k`**: After processing all elements, `k` represents the number of unique elements in `nums`.

### Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of `nums`. We iterate over each element once, and dictionary operations (insertion and lookup) are O(1) on average.
- **Space Complexity**: O(n) for the `unique` dictionary, as it could potentially store all elements in the worst case if all elements are unique.

---

## Solution using 2 pointers:

### Approach

In this solution, I use a two-pointer technique to remove duplicates in-place, optimizing for O(1) space complexity.

- **Initial Checks**: If the input list `nums` is empty, I return `0` immediately, as there are no elements to process.
- **Initialize Pointers**:
  - `left` pointer starts at the first index (position `0`).
  - The `right` pointer iterates through the list starting from index `1`.
- **Traverse the List**:
  - As `right` moves from the start to the end of the list, I compare the elements at `left` and `right`.
  - If `nums[left]` is different from `nums[right]`, it means we found a new unique element:
    - Increment `left` by `1` to move to the next position for placing the unique element.
    - Assign `nums[right]` to `nums[left]` to overwrite the next position with the new unique value.
- **Return Result**:
  - After the loop completes, `left` points to the last unique element, so the total count of unique elements is `left + 1`.

### Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of `nums`. We iterate over the list once.
- **Space Complexity**: O(1), as we only use two pointers and modify the list in-place.
