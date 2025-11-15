from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    end = len(nums)
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
    return nums
