class Math_Dojo:

    def __init__(self, val):
        self.val = val

    def add(self, *args):
        for arg in args:
            self.val += arg
        return self

    def subtract(self, *args):
        for arg in args:
            self.val -= arg
        return self

    def result(self):
        return self.val

md = Math_Dojo(0)
x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x)