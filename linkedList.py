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


list1 = LinkedList()
list1.headval = Node('Mon')

l2 = Node('Tue')
l3 = Node('Wed')

# Link the first node to the 2nd node
list1.headval.nextval = l2

# Link 2nd node to 3rd node
l2.nextval = l3

current_val = list1.headval

while current_val:
    # print(current_val.dataval)
    current_val = current_val.nextval

list1.print_list()