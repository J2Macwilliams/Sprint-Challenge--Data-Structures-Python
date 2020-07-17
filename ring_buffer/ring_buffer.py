class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.tail = 0

    def append(self, item):
        # if there is no capacity
        if self.capacity == 0:
            return

        # otherwise add to storage
        self.storage.append(item)

        # increment self.tail somewhere
        if len(self.storage) == self.capacity:
            self.storage.pop(self.tail)
            self.storage.insert(self.tail, item)
            self.tail = (self.tail + 1) % self.capacity
        
        
        
    def get(self):
        true_values = [i for i in self.storage if i != None ]
        return true_values