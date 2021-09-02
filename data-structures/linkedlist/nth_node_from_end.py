from linked_list import LinkedList


class LinkedListExtended(LinkedList):
    def __init__(self):
        super().__init__()

    def find_nth_node_from_end(self, n):
        temp_pointer = self.head
        data_pointer = self.head

        for i in range(n):
            temp_pointer = temp_pointer.next

        while temp_pointer.next is not None:
            data_pointer = data_pointer.next
            temp_pointer = temp_pointer.next

        print(data_pointer.data)


if __name__ == "__main__":
    ll_obj = LinkedListExtended()
    ll_obj.add_node(5)
    ll_obj.add_node(4)
    ll_obj.add_node(3)
    ll_obj.add_node(2)
    ll_obj.add_node(1)
    ll_obj.find_nth_node_from_end(0)
