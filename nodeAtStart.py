class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    # Printing the linked list
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Add new data at the begining
    def at_the_begining(self, newdata):
        NewNode = Node(newdata)

        NewNode.nextval = self.headval
        self.headval = NewNode


list1 = LinkedList()
list1.headval = Node('Mon')

l2 = Node('Tue')
l3 = Node('Wed')

list1.headval.nextval = l2
l2.nextval = l3

list1.at_the_begining('Sun')
list1.print_list()