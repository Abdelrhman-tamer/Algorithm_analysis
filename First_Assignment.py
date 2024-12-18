
def counting_sort(arr):
    max_val = max(arr)
    n = len(arr)

    count = [0] * (max_val + 1)
    output = [0] * n

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output