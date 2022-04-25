class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


    # Add new data in between
    def between(self, middle_node, newdata):
        
        if middle_node is None:
            print('The Node is absent')
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    
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

list1.between(list1.headval, 'Yay')
list1.print_list()