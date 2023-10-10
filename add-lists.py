class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# approach
# approach this as if it is gradeschool addition
# add the numbers for each node together, along with any remainder from previous operations
# create a new node with the appropriate value, insert the new node until we have completed the operation.


def add_lists(head_1, head_2):
    dummy = Node(None)
    tail = dummy
    carry = 0

    while head_1 or head_2 or carry:
        # extract the values
        val1 = 0 if not head_1 else head_1.val
        val2 = 0 if not head_2 else head_2.val

        # calculate the new nodes value, the carry value, and create the new node
        sum_of_nodes_and_carry = val1 + val2 + carry
        carry = 1 if sum_of_nodes_and_carry > 9 else 0
        node_value = sum_of_nodes_and_carry % 10

        # update the pointers
        tail.next = Node(node_value)
        tail = tail.next
        head_1 = None if not head_1 else head_1.next
        head_2 = None if not head_2 else head_2.next

    # return the dummy.next, as that will point to the head of the new list
    return dummy.next
