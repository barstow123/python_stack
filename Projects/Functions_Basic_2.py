#Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number
#  (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countdown(num):
    return [x for x in range(num, -1,-1)]

print(countdown(5))


#Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def printAndReturn(arr):
    print("First Value -", arr[0])
    return(arr[1])

print(printAndReturn([5,6]))

def firstPlusLength(arr):
    return arr[0] + len(arr)
print(firstPlusLength([1,2,3,4]))

#Values Greater than Second - Write a function that accepts any array,
#  and returns a new array with the array values that are greater than its 2nd value.
#  Print how many values this is.  If the array is only one element long, have the function return False

def greaterThanSecond(arr):
    if (len(arr) == 1):
        return False
    array = []
    for val in arr:
        if(val > arr[1]):
            array.append(val)
    print(len(array))
    return array
print(greaterThanSecond([1,4,6,7,8,1,2]))

# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value.
#  This function should take two numbers and return a list of length size containing only the number in value.
# For example, lengthAndValue(4,7) should return [7,7,7,7].

def LengthAndValue(size, value):
    # new_arr = []
    #   for count in range(size):
    #   new_arr.append(value)
    #   return new_arr
    return [value for i in range(size)]

print(LengthAndValue(7,5))
