# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)

def max_product(arr):
    product=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_product= arr[i] * arr[j]
            if current_product>product:
                product= current_product

    return product


arr = [1, 7, 3, 4, 9, 5] 
print(max_product(arr))

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# If allowed to sort (and use extra space temporarily), you could sort and just multiply the last two numbers (biggest two):


# def max_product(arr):
#     arr.sort()
#     return arr[-1] * arr[-2]

# Time: O(n log n) because of sort
# Space: O(1) if in-place sort


def max_product(arr):
    max1 = max2 = 0
    for num in arr:
        if num> max1:
            max2=max1
            max1= num
        elif num> max2:
            max2= num
    return max1 * max2


arr = [1, 7, 3, 4, 9, 5] 
print(max_product(arr))

# Time Complexity: O(n) 
# Space Complexity: O(1) 