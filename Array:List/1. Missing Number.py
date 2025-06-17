# Write a function to find the missing number in a given integer array of 1 to 100. 
# The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.

# Example

# missing_number([1, 2, 3, 4, 6], 6) # 5


def missing_number(array, total):
    array_total=0
    for i in array:
        array_total= array_total + i
    real_total= total*(total+1)/2
    missing= real_total-array_total
    return missing


array= [1,2,3,4,5,7]
print(missing_number(array,7))

# Time Complexity = O(n)
# Space Complexity = O(1)

def missing_number(arr, n):
    full_set = set(range(1, n + 1))
    arr_set = set(arr)
    missing = full_set - arr_set  
    return missing.pop()

# Time Complexity = O(n)
# Space Complexity = O(n)