# Contains Duplicate Solutions

This repository contains multiple solutions for the "Contains Duplicate" problem on LeetCode. Each solution has a unique ID for easy reference.
You can find the solution [here](Solution.py).

## Solution 1: Brute Force Approach (ID: 1)

**Explanation**:
This approach uses two nested loops to compare each element with every other element.

**Time Complexity**: O(n^2)  
**Space Complexity**: O(1)

---

## Solution 2: Sorting Approach (ID: 2)

**Explanation**:
The array is sorted first, and then we check for duplicates by comparing consecutive elements.

**Time Complexity**: O(n log n)  
**Space Complexity**: O(1)

---

## Solution 3: Using List to Store (ID: 3)

**Explanation**:
A list is used to store seen elements, and we check if an element is already in the list.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

---

## Solution 4: Using Set (ID: 4)

**Explanation**:
A set is used to store unique elements, and we compare its length with the original array.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)
