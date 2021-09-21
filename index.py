#.find()

#Write a function called findElement. It receives 2 arguments: an array, a value
#You must return the index in which the value is located in the array
#If the value is not found in the array return -1

def findElement(arr, b):
    for i in range (0, len(arr), 1):
        if arr[i] == b:
            return i
        else:
            return -1

result2 = findElement([2, 3, 4], 4)
print( result2 )

def findElement2( arr, value):
    i = 0
    while i < len(arr):
        if arr[i] == value:
            return i
        i += 1
    return -1

nums = [10 , 20 , 30 , 40 , 50]
result = findElement2(nums , 40)
print( result )

# .filter()
# Write a function called filterElements. It receives 3 arguments: an array, a string, a value
# The string can have the following values:
#     - greater
#     - lesser
#     - equal
#     - notEqual
# You must filter all the elements that match with the criteria against the value and 
# return them in a new array
# For example:


# filterElements( arr, "lesser", 20)  arr = [10, 40, 20, 30, 40, 50]
# Should return all values lesser than 20 inside the array  => [10]
# If no match is found return an empty array
def filterElements2(arr, criteria, val):
    result4 = []
    for element in arr:
        if criteria == "greater" and element > val:
            result4.append( element ) 
        elif criteria == "lesser" and element < val:
            result4.append( element ) 
        elif criteria == "equal" and element == val:
            result4.append( element )
        elif criteria == "notEqual" and element != val:
            result4.append( element )
    return result4

nums = [10 , 20 , 30 , 40 , 50, 60, 70, 80, 90, 100]
val = 50

newarray = filterElements2(nums, "notEqual", val)
print( newarray )


def filterElements(arr, word, value):
    i = 0
    while i < len(arr):
        if arr[i] == value:
            if word == "greater":
                return arr[i] > value
            elif word == "lesser":
                return arr[i] < value
            else:
                if word == "equal":
                    return arr[i] == value
                else:
                    return arr[i] !=  value
        i += 1
    return [] 

nums = [10 , 20 , 30 , 40 , 50, 60, 70, 80, 90, 100]
val = 50
result3 = filterElements(nums, "lesser", 20)
