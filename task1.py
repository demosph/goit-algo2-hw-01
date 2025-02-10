def find_min_max(arr):
    if not arr:
        raise ValueError("Array cannot be empty")

    def recursive_search(left, right):
        if left == right:
            return arr[left], arr[left]
        elif left + 1 == right:
            return min(arr[left], arr[right]), max(arr[left], arr[right])

        mid = (left + right) // 2
        min1, max1 = recursive_search(left, mid)
        min2, max2 = recursive_search(mid + 1, right)

        return min(min1, min2), max(max1, max2)

    return recursive_search(0, len(arr) - 1)


# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_val, max_val = find_min_max(arr)
print(f"Min: {min_val}, Max: {max_val}") # Output: Min: 1, Max: 9