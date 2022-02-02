def bubble_sort(list1):
    def swap(i, j):
        list1[i], list1[j] = list1[j], list1[i]

    n = len(list1)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x)
            if list1[i - 1] > list1[i]
                swap(i - 1, i)
                swapped = True


                
