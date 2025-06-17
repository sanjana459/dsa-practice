# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Here we are doing no repetition of the same pairs and and also not allowed to use the same element twice

def pair_sum(array,target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if i!=j and array[i] + array[j] == target:
                print(f"The pairs are: {array[i]} and {array[j]}")

array= [2,7,11,15]
pair_sum(array, 9)

# Time Complexity= O(n^2)
# Space Complexity= O(1)

# If they say "no extra space", use brute force (O(n²)).
# If they say "optimize for time" or "large data", use hash map (O(n)).

# Can you dictionaries for optimization. Cant use sets because we need to store index and value