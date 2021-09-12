
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new_node

    def insert_values(self, list_of_values):
        for i in list_of_values:
            self.insert_at_end(i)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
            return
        if index == 0:
            self.head = self.head.next

        itr = self.head
        for i in range(index - 1):
            itr = itr.next
        itr.next = itr.next.next

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
            return
        if index == 0:
            self.insert_at_beginning(value)
            return
        itr = self.head
        for i in range(index - 1):
            itr = itr.next
        itr.next = Node(value, itr.next)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print('Linked list is empty')
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next


    def remove_by_value(self, data_to_remove):
        if self.head is None:
            return
        if self.head.data == data_to_remove:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data_to_remove:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            llist = ""
            while itr:
                llist += str(itr.data) + "-->"
                itr = itr.next
            print(llist)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([90, 45, 24, 14, 56, 46, 25, "mango"])
    ll.print_list()

    ll.remove_by_value("oijero")
    ll.print_list()