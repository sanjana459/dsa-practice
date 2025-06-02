# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87

def first_second(myList):
    max1 = max2 = 0
    for i in myList:
        if i>max1:
            max2=max1
            max1=i
        elif i>max2:
            max2=i
    return max1, max2

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList))

# Time Complexity= O(n)
# Space Complexity= O(1)

def first_second(myList):
    myList.sort()
    return myList[-1], myList[-2]

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList))

# myList.sort()
# 1. Modifies the list in-place → The original list is changed.
# 2. No new list is created.
# 3. Returns None — that’s why you cannot assign it to a variable.

# sorted(myList)
# 1. Creates a new sorted list → The original list stays unchanged
# 2. Returns the new sorted list

def first_second(myList):
    myList.sort(reverse=True)
    return myList[0:2]

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList))

# Time Complexity:	O(n log n)
# Space Complexity:	O(1)

# O(nlogn) > O(n)