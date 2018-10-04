class Underscore:
    def map(self, arr, fun):
        returnArray = []
        for val in arr:
            returnArray.append(fun(val))
        return returnArray
    def find(self, arr, fun):
        for val in arr:
            if (fun(val)):
                return val
        return self
    def filter(self, arr, fun):
        returnArray = []
        for val in arr:
            isTrue = fun(val)
            if (isTrue):
                returnArray.append(val)
        return returnArray
    def reject(self, arr, fun):
        returnArray = []
        for val in arr:
            isTrue = fun(val)
            if (isTrue != True):
                returnArray.append(val)
        return returnArray


_ = Underscore()

print(_.map([1, 2, 3], lambda x: x * 2))  # should return [2,4,6]
print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))  # should return the first value that is greater than 4
print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))  # should return [2,4,6]
print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))  # should return [1,3,5]