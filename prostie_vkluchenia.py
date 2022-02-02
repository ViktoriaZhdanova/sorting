# создание функции для вставки
def insertion_sort(list1): 
        for i in range(len(list1)): 
            value = list1[i] 
            pos = i 
            while pos > 0 and list1[pos - 1] > value
                list1[pos] = list1[pos - 1] 
                pos = pos - 1
            list1[pos] = value
        return list1
