class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# zipper merge problem

# set dummy node
# set a tail to track where to insert

# perform the main merge
# while both lists still exist
# if value at head_1 is greater than value at head_2
# insert value at head 2 -> add it to the tracked tail node
# move head2 to head2.next
# else
# insert value at head1
# insert value at head 2 -> add it to the tracked tail node
# move head1 to head 1.next


# merge whatever is left
# return the dummy node.next, as it will point to the new list
def merge_lists(head_1, head_2):
    dummy = Node(1)
    tail = dummy

    while head_1 and head_2:
        if head_1.val > head_2.val:
            tail.next = head_2
            head_2 = head_2.next
        else:
            tail.next = head_1
            head_1 = head_1.next
        tail = tail.next

    if head_1:
        tail.next = head_1

    if head_2:
        tail.next = head_2

    return dummy.next
