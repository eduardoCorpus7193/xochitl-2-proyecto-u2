class Node:
    def __init__(self, data):
        # Constructor to initialize a node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Constructor to initialize the linked list
        self.head = None

    def insert_at_beginning(self, data):
        # Insert a node at the beginning of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        # Insert a node at the end of the linked list
        new_node = Node(data)

        if self.head is None:
            # If the linked list is empty, set the new node as the head
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_after_node(self, target_data, data):
        # Insert a node after a given node in the linked list
        new_node = Node(data)

        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_node(self, target_data):
        # Delete a node from the linked list
        if self.head is not None and self.head.data == target_data:
            # If the node to be deleted is the head, update the head to the next node
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == target_data:
                # If the next node's data matches the target data, skip the next node
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        # Display the linked list elements
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

"""
# Create a linked list
my_list = LinkedList()

# Insert nodes
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)

# Display the linked list
my_list.display()  # Output: 1 2 3

# Insert node at the beginning
my_list.insert_at_beginning(0)
my_list.display()  # Output: 0 1 2 3

# Insert node after a given node
my_list.insert_after_node(2, 1.5)
my_list.display()  # Output: 0 1 1.5 2 3

# Delete a node
my_list.delete_node(2)
my_list.display()  # Output: 0 1 1.5 3
"""