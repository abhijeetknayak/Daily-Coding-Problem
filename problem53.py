class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if len(self.stack1) == 0:
            return None

        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop()) # Appending popped elements

        ret = self.stack2.pop() # Our return element

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop()) # Storing them back into the Input stack

        return ret

if __name__ == '__main__':
    queue = queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.stack1)

    print(queue.dequeue())
    print(queue.dequeue())

    print(queue.stack1)


