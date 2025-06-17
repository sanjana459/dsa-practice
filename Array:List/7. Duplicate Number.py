# Write a function to remove the duplicate numbers on given integer array/list.

# Example

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]


def remove_duplicates(myList):
    arr=[]
    for i in myList:
        if i in arr:
            continue
        else:
            arr.append(i)
    return arr

             
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))   

# for i in myList: O(n)
# if i in arr: O(k) in worst case (because in for a list takes O(k) where k is the current length of arr)
# Worst-case overall: O(n²) — because for every element you are searching in arr which is growing.

# Most optimal solution is this when we can use only Lists and Arrays


def no_duplicates(lst):
    new_set=set(lst)    #--------> O(n)
    return list(new_set) #--------> O(n)

print(no_duplicates([1, 1, 2, 2, 3, 4, 5])) 


# TC: O(n)
# SC: O(n)
# Using sets is better