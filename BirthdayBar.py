def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def birthday_with_bubble_sort(s, d, m):
    
    s = bubble_sort(s)
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1

    return count

s = [1, 2, 1, 3, 2]
d = 3
m = 2


print("Lili solo le quiere dar a ron", birthday_with_bubble_sort(s, d, m))

