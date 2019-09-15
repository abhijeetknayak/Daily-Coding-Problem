class node:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_val(self):
        return self.val

class linkedlist:
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def insert(self, val):
        newNode = node(val)
        newNode.set_prev(self.tail)
        newNode.set_next(None)
        self.tail.set_next(newNode)
        self.tail = newNode

    def size(self):
        count = 0
        current = self.head
        while current:
            count = count + 1
            current = current.get_next()
        return count

    def print_all_next(self):
        current = self.head
        while current:
            print(current.get_val(), end= ' -> ')
            current = current.get_next()
        print("Null")

    def print_all_prev(self):
        current = self.tail
        while current:
            print(current.get_val(), end=' -> ')
            current = current.get_prev()
        print("Null")

    def delete_element(self, val):
        current = self.head
        while current:
            current_val = current.get_val()
            if current_val == val:
                current.get_prev().set_next(current.get_next())
                current.get_next().set_prev(current.get_prev())
                break
            else:
                current = current.get_next()

    def reverse_in_place(self):
        current = self.head
        next = current.get_next()
        while current:
            if current == self.head:
                current.set_next(None)
                current = next
            elif next is None:
                current.set_next(self.head)
                self.head = current
            else:
                next = current.get_next()
                current.set_next(self.head)
                self.head = current
                current = next

    def sort(self, list2):
        i = 0
        j = 0
        min1 = self.head
        min2 = list2.head
        if min1.val < min2.val:
            list = linkedlist(node(min1.val))
            min1 = min1.get_next()
            i += 1
        else:
            list = linkedlist(node(min2.val))
            min2 = min2.get_next()
            j += 1
        while i <= self.size() and j <= list2.size():
            if i < self.size() and j < list2.size():
                if min1.val < min2.val:
                    list.insert(min1.val)
                    min1 = min1.get_next()
                    i += 1
                else:
                    list.insert(min2.val)
                    min2 = min2.get_next()
                    j += 1
            elif i == self.size() and j < list2.size():
                list.insert(min2.val)
                min2 = min2.get_next()
                j += 1
            elif i < self.size() and j == list2.size():
                list.insert(min1.val)
                min1 = min1.get_next()
                i += 1
            else:
                break
        return list

if __name__ == '__main__':

    # First Linked List
    list1 = linkedlist(node(13))
    list1.insert(34)
    list1.insert(51)
    list1.insert(79)

    # Second Linked List
    list2 = linkedlist(node(22))
    list2.insert(43)
    list2.insert(55)
    list2.insert(85)

    # Third Linked List
    list3 = linkedlist(node(2))
    list3.insert(56)
    list3.insert(123)
    list3.insert(234)
    list3.insert(345)

    print("List1 : ", end='')
    list1.print_all_next()
    print("List2 : ", end='')
    list2.print_all_next()
    print("List3 : ", end='')
    list3.print_all_next()

    # List of Linked Lists
    sorted_list = [list1, list2, list3]

    # Linked list to store the sorted list. Daily Coding Problem 78
    l = linkedlist()

    for idx in range(0, len(sorted_list)):
        if idx == 0:
            l = sorted_list[idx]
        else:
            l = l.sort(sorted_list[idx])

    print("Final Sorted List(Next) : ", end='')
    l.print_all_next()
    print("Final Sorted List(Prev) : ", end='')
    l.print_all_prev()

    # Daily Coding Problem 73
    l.reverse_in_place()

    print("Reversed List : ", end='')
    l.print_all_next()