class Node:
    """Class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node.

        Args:
            data (int): The data stored in the node.
            next_node (Node, optional): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None.
        """
        self.data = data  # Calls the data setter
        self.next_node = next_node  # Calls the next_node setter

    @property
    def data(self):
        """Retrieve the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node with validation.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the linked list.

        The list is printed in sorted order, one number per line.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The data value for the new node.
        """
        new_node = Node(value)

        # If list is empty or new node should be the new head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Find the correct position for insertion
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert new node in sorted order
        new_node.next_node = current.next_node
        current.next_node = new_node
