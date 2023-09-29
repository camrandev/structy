# set pointers to start, end
# while start is less than end
# if start is not equal to 5, increment it until it is
# if end is equal to 5, increment it until it is not

# if start is equal to 5 and end is not equal to 5, swap them

# return nums


def five_sort(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        while nums[l] != 5:
            l += 1
        while nums[r] == 5:
            r -= 1
        nums[r], nums[l] = nums[l], nums[r]
        r -= 1
        l += 1
    return nums
