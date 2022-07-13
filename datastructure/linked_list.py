class Node:
    """
    An object for storing a single node of linked list
    A node contains - Data and ref to next node
    """

    data = None

    def __init__(self, node_data, next_node=None):
        self.data = node_data
        self.next = next_node

    def __repr__(self) -> str:
        """
        String representation of Node object
        """
        return f"<Node data:{self.data}>"


class Linkedlist:
    """
    Singly linked list
    """

    def __init__(self) -> None:
        self.head = None
        self.__count = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Return number of nodes: o(n) time as it traverse each element
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __len__(self):
        return self.__count

    def add(self, data):
        """
        Add new node at head. It takes O(1) time
        """
        new_head = Node(data, self.head)
        self.head = new_head
        self.__count += 1

    def __repr__(self) -> str:
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next
        return "->".join(nodes)

    def search(self, searchval):
        """
        Search for the first node containing data that matches the key
        Return the node or "None"
        Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == searchval:
                return current
            current = current.next
        return None

    def insert(self, data, index):
        """
        Insert node. It take o(n) iteration when searching the list and insert
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)
            current = self.head
            position = index
            while position > 1:
                current = current.next
                position -= 1
            prev_node = current
            next_node = current.next

            prev_node.next = new_node
            new_node.next = next_node
        self.__count += 1

    def remove(self, index):
        """
        Remove node from passed index.
        It takes o(n) time to look for index and perform remove
        """
        current = self.head
        next_node = current.next

        if index == 0:
            current.next = None
            self.head = next_node
            return current
        elif index > 0:
            position = 1
            prev_node = None

            while position <= index:
                next_node = current.next

                if index == position:
                    prev_node.next = next_node
                else:
                    prev_node = current

                position += 1
                current = current.next
        self.__count -= 1
