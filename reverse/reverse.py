class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        current = self.head
        prev = None
        upcoming = None
        while current is not None:
            # set the next value
            upcoming = current.get_next()

            #  change current's pointer
            current.set_next(prev)

            # increment and move head
            prev = current
            self.head = current
            current = upcoming

    # Recursion version
    # def reverse_list(self, node, prev):
    #     if self.head is None:
    #         return
        
    #     current = self.head
    #     backwards = False
        
    #     if current.next_node is None:
    #         backwards = True
    #     # Drill down to the bottom
    #     if backwards is False or current.next_node is not None:
    #         backwards = True
    #         current = node
    #         prev = current
    #         current = current.get_next()
    #         self.head = current
    #         self.reverse_list(current, prev)
    #     # cascade backwards
    #     if backwards is True:
    #         current = current.set_next(prev)   
    #         prev = node
    #         prev.next_node = None

        
            


            


