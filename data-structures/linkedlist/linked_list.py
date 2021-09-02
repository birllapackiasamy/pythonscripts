class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_nodes(self):
        temp = self.head
        while True:
            print(temp.data)
            if temp.next is not None:
                temp = temp.next
            else:
                break




# linkedlist = LinkedList()
# linkedlist.add_node(5)
# linkedlist.add_node(4)
# linkedlist.add_node(3)
# linkedlist.add_node(2)
# linkedlist.add_node(1)
# linkedlist.print_nodes()