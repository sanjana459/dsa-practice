# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true
# Hint: Use sets

def duplicates(nums):
    actual_len= len(nums)
    no_duplicates= len(set(nums))
    if actual_len != no_duplicates:
        print("true")

nums= [1,2,3,1]
duplicates(nums)




def missing_number(arr, n):
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual

# TC: O(n)
# SC: O(1)

# Benefits:
# Best-case time: O(1) if a duplicate is early
# Worst-case time: O(n)
# Space: O(n), same as before
# No need to build full set unless needed
