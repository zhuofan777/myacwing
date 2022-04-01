n = int(input())
arr = list(map(int, input().split()))
tmp = [0] * n


def merge_sort(arr, l, r):
    if l >= r:
        return 0
    mid = l + r >> 1
    res = merge_sort(arr, l, mid) + merge_sort(arr, mid + 1, r)
    k = 0
    i = l
    j = mid + 1
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            res += mid - i + 1
            tmp[k] = arr[j]
            k += 1
            j += 1
    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = arr[j]
        k += 1
        j += 1
    i, j = l, 0
    while i <= r:
        arr[i] = tmp[j]
        i += 1
        j += 1
    return res


print(merge_sort(arr, 0, n - 1))
