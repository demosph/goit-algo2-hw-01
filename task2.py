import random

def quick_select(arr, k):
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input")

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(mid))

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"The {k} smallest element: {quick_select(arr, k)}") # Output: The 3 smallest element: 7