class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


# Get union of two linked lists by one pass on each linked list
def union(llist_1, llist_2):
    llist_union = LinkedList()

    if llist_1.size() == 0 and llist_2.size() == 0:
        return llist_union

    if llist_1.size() == 0:
        set_2 = set()
        head = llist_2.head
        while head:
            if head.value not in set_2:
                set_2.add(head.value)
                llist_union.append(head.value)
            head = head.next

    elif llist_2.size() == 0:
        set_1 = set()
        head = llist_1.head
        while head:
            if head.value not in set_1:
                set_1.add(head.value)
                llist_union.append(head.value)
            head = head.next

    else:
        set_all = set()
        head = llist_1.head
        while head:
            if head.value not in set_all:
                set_all.add(head.value)
                llist_union.append(head.value)
            head = head.next

        head = llist_2.head
        while head:
            if head.value not in set_all:
                set_all.add(head.value)
                llist_union.append(head.value)
            head = head.next
    return llist_union


# Get intersection of two linked lists by one pass on each linked list
def intersection(llist_1, llist_2):
    llist_intersect = LinkedList()
    if llist_1.size() == 0 or llist_2.size() == 0:
        return llist_intersect
    else:
        set_1 = set()
        head = llist_1.head
        while head:
            set_1.add(head.value)
            head = head.next

        set_2 = set()
        head = llist_2.head
        while head:
            if head.value in set_1 and head.value not in set_2:
                llist_intersect.append(head.value)
                set_2.add(head.value)
            head = head.next

    return llist_intersect


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))      # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print(intersection(linked_list_1, linked_list_2))   # 6 -> 4 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]   # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
element_2 = [1, 7, 8, 9, 11, 21, 1]     # Empty

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 7, 8, 9, 11, 21, 1]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))      # 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_5, linked_list_6))   # Empty


# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))  # Empty
print(intersection(linked_list_7, linked_list_8))   # Empty
