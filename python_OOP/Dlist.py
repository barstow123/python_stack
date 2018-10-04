class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = None

class DList:

    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.foot = node

    def addNode(self, value):
        node = Node(value)
        runner = self.foot
        runner.next = node
        node.last = runner
        self.foot = node
        return self

    def insertNode(self, val, pos):
        if (pos < 0):
            print("Error: position too low. out of range")
            return self
        node = Node(val)
        runner = self.head
        if (pos == 0):
            node.next = runner
            runner.last = node
            self.head = node
            return self
        i = 1
        while(runner.next):
            if (i == pos):
                node.next = runner.next
                runner.next = node
                node.last = runner
                return self
            runner = runner.next
            i += 1
        if (i == pos):
            runner.next = node
            node.last = runner
            self.foot = node
            return self
        print("Error, position too high. out of range")
        return self


    def displayAll(self):
        runner = self.head
        print('\n\n')
        print(id(runner), runner.value, id(runner.next))
        while(runner.next != None):
            runner = runner.next
            print(id(runner.last), id(runner), runner.value, id(runner.next))
        return self

    def deleteNode(self, value):
        runner = self.head
        if (runner.value == value):
            self.head = runner.next
            del runner
            return self
        while (runner.next.next):
            if (runner.next.value == value):
                __delNextNode(runner)
                return self
            runner = runner.next
        else:
            if (runner.value == value):
                __delNextNode(runner)
                self.foot = runner
                return self
            if (runner.next.value == value):
                del runner.next
                #runner.next = None
                self.foot = runner

    def __delNextNode(runner):
        temp = runner.next
        runner.next = runner.next.next
        runner.next.last = runner
        del temp
        return self
            
        


my_list = DList(0)
my_list.addNode(1).addNode(2).addNode(3).addNode(4)
my_list.deleteNode(4)
my_list.displayAll()
my_list.insertNode(10,4).displayAll()
