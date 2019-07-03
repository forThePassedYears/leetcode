alist = [49, 38, 65, 97, 76, 13, 27, 49, 1, 66, 77, 8, 88, 99, 11]


def select_sort(alist):
    '''选择排序
        最坏时间复杂度 O(n**2)
        最优时间复杂度 O(n**2)
    '''
    n = len(alist)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


print(alist)
select_sort(alist)
print(alist)
