import random

# avoid sorting the entire list
"""
What is partitioning?
means that you select one element as pivot, we find a partition such that every element to the left of it smaller than the element, and right is bigger than the element

example find the 4th smallest element

select the firs k smaller or bigger elements, the order doesn't matter.
[3, 2, 1, 4, 8, 9, 7, 5, 6]
first left = 1
right = 8
pivot = 0

k = 5

first leftmark = 3, rightmark = 2
swap(right, pivot)
[1, 2, 3, 4, 8, 9, 7, 5, 6]

return rightmark

next, as k is 5, we returned 2
"""

def quickselect(array, left, right, k):
    if left == right:
        return array
    split = partition(array, left , right)  # 2
    length = split - left + 1  # split is the partition index, greater than left, to get the numbers between the left and the split, add one to the difference
    # value of k is length + 1, because there length number of elements on partition, the partition is the kth element.
    # lenght is counted inclusive of partition index
    if k == length:
        return array[k]  # return with the partiton index, because it was inclusive
    elif k < length:  # if k is less than the length of the partition
        quickselect(array, left, split - 1, k)
    else:  # if k is greater than the length of the split, then we call with lesser value of k,
        quickselect(array, split + 1, right, k - length)

def partition(array, left, right):
    pivot = array[left]  # = 3
    leftmark = left + 1  # 0 + 1 == 1, point to index 1
    rightmark = right  # last element pointer
    while leftmark < rightmark:
        while leftmark < right and array[leftmark] < pivot:
            leftmark += 1
        while rightmark > left and array[rightmark] >= pivot:
            rightmark -= 1
        if leftmark < rightmark:
            array[leftmark], array[rightmark] = array[rightmark], array[leftmark]

    pivot, array[rightmark] = array[rightmark], pivot

