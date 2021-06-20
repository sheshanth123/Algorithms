## Using recursion O(log(n)) time  // O(log(n)) space because of stacks

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    
    while(left <= right):

        middle = (left + right) // 2
        matchFound = array[middle]

        if matchFound == target:
            return middle
        elif target > matchFound:
            left = middle+1
            return binarySearchHelper(array, target, middle+1, right)
        else:
            right
            return binarySearchHelper(array, target, left, middle-1)

## Using iteration O(log(n)) time // O(1) space

def binarySearch(array, target):
    left = 0
    right = len(array) -1

    while(left <= right):
        middle = (left + right) // 2
        matchFound = array[middle]

        if target == matchFound:
            return middle
        elif target > matchFound:
            left = middle + 1
        else:
            right = middle - 1
    return -1   
