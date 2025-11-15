from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums
    sorted_left_side = merge_sort(nums[: len(nums) // 2])
    sorted_right_side = merge_sort(nums[len(nums) // 2 :])

    return merge(sorted_left_side, sorted_right_side)


def merge(first: List[int], second: List[int]) -> List[int]:
    final = []
    i, j = 0,0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final

