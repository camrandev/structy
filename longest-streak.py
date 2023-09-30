# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# track the max streak -> init to 0
# track current streak -> init to 0
# check if values are same -> use previous value -> init to None
# use a current pointer to iterate through -> init to head

# while a head node exists
# check if the current nodes value is equal to the previous saved value
# if it is, increment the current streak
# update max streak to greater of itself and current streak
# if the current nodes value is not equal to the saved value
# set prev val to current nodes value
# set current streak to 1

# outside of the if block, move current pointer to its next property

# return the max streak


def longest_streak(head):
    max_streak = 0
    current_streak = 0
    prev_val = None
    curr = head

    while curr:
        if curr.val == prev_val:
            current_streak += 1
        else:
            prev_val = curr.val
            current_streak = 1
        max_streak = max(max_streak, current_streak)
        curr = curr.next

    return max_streak
