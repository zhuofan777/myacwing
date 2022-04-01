import sys

sys.setrecursionlimit(10000)
n = int(input())
list_str = input()
arr = list(map(int, list_str.split(' ')))


def quick_sort(nums, l, r):
    if l >= r:
        return
    i, j = l - 1, r + 1
    pivot = nums[l + r >> 1]
    while i < j:
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    quick_sort(nums, l, j)
    quick_sort(nums, j + 1, r)


quick_sort(arr, 0, n - 1)
print(' '.join(map(str, arr)))
