#Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big".
# Example: makeItBig([-1, 3, 5, -5])
def biggieSize(arr):
    for idx in range(len(arr)):
        if(arr[idx] > 0):
            arr[idx]="Big"
    return arr

print(biggieSize([-1, 3, 5, -5]))


# Count Positives - Given an array of numbers, create a function to replace the last value with number of positive values.
#  Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def count_positives(arr):
    sum = 0
    for val in arr:
        if (val > 0):
            sum += 1
    arr[len(arr)-1] = sum
    return arr
print(count_positives([-1,1,1,1]))

def sumTotal(arr):
    sum = 0
    for val in arr:
        sum = sum + val
    return sum
print(sumTotal([1,2,3,4,5]))

#Average - Create a function that takes an array as an argument and returns the average of all the values in the array.
# For example multiples([1,2,3,4]) should return 2.5

def multiples(arr):
    sum = 0
    for val in arr:
        sum = sum + val
        avg = sum/len(arr)
    return avg

print(multiples([1,2,3,4,5]))



def find_len(arr):
    return len(arr)


def minimum(arr):
    if len(arr) == 0:
        return false
    min = arr[0]
    for val in arr:
        if min > val:
            min = val
    return min
print(minimum([1,2,-4,5]))

#Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.
#  If the passed array is empty, have the function return false.
#  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
    if len(arr) == 0:
        return false
    max = arr[0]
    for val in arr:
        if val > max:
            max = val
    return max
print(maximum([-1,-2,-3]))

def ultimate_analyze(arr):
    things = {}
    things['sumTotal'] = sumTotal(arr)
    things['average'] = multiples(arr)
    things['minimum'] = minimum(arr)
    things['maximum'] = maximum(arr)
    things['len'] = find_len(arr)
    return things
print(ultimate_analyze([1,2,3,4,5]))

def reverseList(arr):
    for count in range(int(len(arr)/2)):
        print("count is ", count)
        temp = arr[count]
        arr[count] = arr[len(arr)-count-1]
        arr[len(arr)-count-1] = temp
    return arr
print(reverseList([1,2,3,4,5]))