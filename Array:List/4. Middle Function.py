# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

def middle(myList):
    return myList[1:-1]

myList = [1, 2, 3, 4]
print(middle(myList))


# Time Complexity:	O(n)
# Space Complexity:	O(n)