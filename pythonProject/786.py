import sys

sys.setrecursionlimit(10000)
n, m = map(int, input().split())
list_str = input()
arr = list(map(int, list_str.split(' ')))


def quick_sort(nums, l, r, k):
    if l >= r:
        return nums[l]
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
    if j - l + 1 >= k:
        return quick_sort(arr, l, j, k)
    else:
        return quick_sort(arr, j + 1, r, k - (j - l + 1))


quick_sort(arr, 0, n - 1, m)
print(' '.join(map(str, arr)))
