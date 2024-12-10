def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        result.append(min(left[i], right[j]))

        {True: i, False: j}[left[i] < right[j]] += 1

    return result + left[i:] + right[j:]
