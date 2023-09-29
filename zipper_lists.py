class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# I believe this is a ziper merge problem, except value arragnement does not matter, we just want to list A ->b etc

# start off with a dummy node to hold our new linked list
# use a variable to track the tail of our list, so we know where to insert, start this at the dummy node

# perform our main merge
# while both lists have values in them

# starting at on list number 1
# set the outside tracked tails next property to the current L1 node
# update the l1 pointer to its own next property
# update the tail to its own next property
# set the outside tracked tails next property to the current l2 node
# update the head_2 to its own next propertt
# update the tracked tail to its own next property

# merge in any residuals
# if head_1 still exists, set tracked tails next to head_1
# if head_2 still exists, set tracked tails next to head_2

# return the next value of dummy node, as that will point to our new list head


def zipper_lists(head_1, head_2):
    # declare variables to track a dummy node and tail

    dummy_list = Node(1)
    tail = dummy_list

    # perform the main merge while both lists have nodes int hem
    while head_1 and head_2:
        tail.next = head_1
        head_1 = head_1.next
        tail = tail.next

        tail.next = head_2
        head_2 = head_2.next
        tail = tail.next

    # perform any cleanup merges required
    if head_1:
        tail.next = head_1

    if head_2:
        tail.next = head_2

    # return the dummy node next value, as that is where the list will starting
    return dummy_list.next

    # this solution is O(n) time, as each list is iterated over at most 1 time, and O(1) space as the only extra memory we use is the dummy list pointer
