class Node():
    def __init__(self, prev, data):
        self.prev = prev
        self.next = None
        self.data = data
        if prev is not None:
            prev.next = self



class LinkedList():
    def __init__(self):
        self.base_node = None


    def add(self, data):
        current_node = self.base_node
        if current_node is None:
            self.base_node = Node(None, data)
            return self.base_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            return Node(current_node, data)


    def remove(self, data):
        current_node = self.base_node
        while current_node is not None:
            if current_node.data == data:
                if current_node is self.base_node:
                    self.base_node = self.base_node.next
                    if self.base_node is not None:
                        self.base_node.prev = None
                else:
                    current_node.prev.next = current_node.next
                    if current_node.next is not None:
                        current_node.next.prev = current_node.prev
                break
            current_node = current_node.next

        if current_node is None:
            return -1
        else:
            return 0


    def find(self, data):
        current_node = self.base_node
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return -1


    def size(self):
        count = 0
        current_node = self.base_node
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count


    def is_empty(self):
        return self.size() == 0
