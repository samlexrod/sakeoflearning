"""
My version of finding m values from the end of a singly linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.link_size = 1

    def append(self, new_element):
        current = self.head
        if self.head:                   # <- do only if there is a head
            while current.next:         # <- do until the next node is None
                current = current.next      # <- shifts the linked list
            current.next = new_element  # <- adding the next element
            self.link_size += 1
        else:                           # <- if there is no head
            self.head = new_element     # <- set head of list

    def find_from_end(self, m):

        counter = 1
        current = self.head
        while counter < self.link_size - m:
            current = current.next
            counter += 1
        print "There are {} elements in the list.".format(self.link_size)
        print "The element {} elements from the end is {}.".format(m, current.data)
        return current.data

def speed_append(values):
    linked_list = LinkedList()
    for value in values:
        element = Node(value)
        linked_list.append(element)
    return linked_list

def question5(ll, m):

    return ll.find_from_end(m)

# Test 1: Looking inside the range
#ll = speed_append(range(1, 6))
#print question5(ll, 3)

# Test 2: Looking outside the range
ll = speed_append(range(1, 7))
print question5(ll, 7)

# Test 3: Looking at the end of the list


# Test 4: Looking before the end of the list


'''
# create object of the list

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

# insert new_element

ll = LinkedList(e1) # <- starting object and adding the head to ll
ll.append(e2)       # <- appending the element to ll
ll.append(e3)       # <- appending the next element to ll
ll.append(e4)
ll.append(e5)

ll.find_from_end(3)

'''
