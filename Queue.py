from Node import Node

class Queue:
    def __init__(self, max_size=None, size=0):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = size
    
    def is_empty(self):
        return self.size == 0
        
    def has_space(self):
        return self.max_size > self.size
        
    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        
    def enqueue(self, value):
        if self.has_space():
            new_node = Node(value)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.set_next_node(new_node)
                self.tail = new_node
            self.size += 1
            return new_node.get_value()
        
    def dequeue(self):
        if not self.is_empty():
            head_node = self.head
            if head_node.get_next_node() != None:
                self.head = head_node.get_next_node()
            else:
                self.head = None
                self.tail = None
            self.size -= 1
            return head_node.get_value()

    def stringify(self):
        head_node = self.head
        string = ""
        while head_node != None:
            string += str(head_node.get_value()) + ","
            head_node = head_node.get_next_node()
        return string.rstrip(',')