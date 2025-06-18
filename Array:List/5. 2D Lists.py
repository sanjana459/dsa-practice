# Given 2D list calculate the sum of diagonal elements.

# Example

# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
# diagonal_sum(myList2D) # 15

def diagonal_sum(myList2D):
    total=0
    for i in range(len(myList2D)):
        for j in range(len(myList2D[1])):
            if i==j:
                total += myList2D[i][j]
    return total

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
print(diagonal_sum(myList2D))


def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# Time complexity: O(n) 
# Space complexity: O(1)