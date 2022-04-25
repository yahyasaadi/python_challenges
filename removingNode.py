class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


    # Removing data
    def removeNode(self, remove_data):
        HeadVal = self.headval

        if HeadVal is not None:
            if HeadVal.dataval == remove_data:
                self.headval = HeadVal.nextval
                HeadVal = None

        while HeadVal is not None:
            if HeadVal.dataval == remove_data:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if HeadVal == None:
            return

        prev.nextval = HeadVal.nextval
        HeadVal = None
    
    
    # Printing the linked list
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    

list1 = LinkedList()
list1.headval = Node('Mon')

l2 = Node('Tue')
l3 = Node('Wed')

list1.headval.nextval = l2
l2.nextval = l3

list1.removeNode('Tue')
list1.print_list()