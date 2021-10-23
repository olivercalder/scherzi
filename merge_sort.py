def merge(left, right):
    if len(left) <= 0:
        return right
    if len(right) <= 0:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

def merge_sort(array):
    if len(array) < 2:
        return array
    return merge(merge_sort(array[:len(array) // 2]), merge_sort(array[len(array) // 2:]))

unsorted = [5, 3, 4, 9, 8, 1, 7, 2, 0, 6]
print(unsorted)
print(merge_sort(unsorted))
