class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:

    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
        return self

    def removeNode(self, val):
        runner = self.head
        if (runner.value == val):
            self.head = runner.next
            del runner
            return self
        while(runner.next):
            if (runner.next.value == val):
                temp = runner.next
                runner.next = runner.next.next
                del temp
                return self
            runner = runner.next
        else:
            temp = runner.next
            if (runner.next.next):
                runner = runner.next.next
            del temp
            return self

    def insertNode(self, val, pos):
        if (pos < 0):
            print("Error: position too low. out of range")
            return self
        count = 0
        node = Node(val)
        runner = self.head
        if count == pos:
            node.next = self.head
            self.head = node
            return self
        while(runner.next):
            count += 1
            if count == pos:
                node.next = runner.next
                runner.next = node
                return self
            runner = runner.next
        count += 1
        if count == pos:
            node.next = runner.next
            runner.next = node
            return self
        print("Error, position too high. out of range")
        return self





    def printAllValues(self):
        runner = self.head
        print(f'\n\nid points to {self.head}')
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))

list = Slist(3)
list.addNode(4)
list.addNode(5)
list.addNode(6)
list.addNode(7)
list.printAllValues()
list.removeNode(3)
list.removeNode(5)
list.removeNode(7)
list.printAllValues()
list.insertNode(1,0)
list.insertNode(8,2)
list.insertNode(9,3)
list.printAllValues()
