def binary(data):
    for i in range(len(data)):
        key = data[i]
        l, h = 0, i - 1
        while l < h:
            mid = l + (h - l)//2
            if key < data[mid]:
                h = mid
            else:
                l = mid + 1
        for j in range(i, l + 1, -1)
            data[j] = data[j -1]
        data[l] = key
    return data







