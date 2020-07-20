class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.storage = [None] * capacity
        self.pointer = 0

    def append(self, item):
        # if there is no capacity
        if self.capacity == 0:
            return

        # add initial items
        self.storage[self.pointer] = item

        # check th e length of list
        if len(self.storage) is self.capacity:
            self.storage[self.pointer] = item

        # increment the pointer 
        self.pointer = (self.pointer + 1) % self.capacity
            

    def get(self):
        true_values = [i for i in self.storage if i != None ]
        return true_values