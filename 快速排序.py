def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


myList = [49, 100, 38, 65, 97, 76, 13, 27, 49, 1, 66, 77, 8, 88, 99, 11]
quick_sort(myList, 0, len(myList) - 1)
print(myList)
# def QuickSort(myList, start, end):
#     # 判断low是否小于high,如果为false,直接返回
#     if start < end:
#         i, j = start, end
#         # 设置基准数
#         base = myList[i]

#         while i < j:
#             # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
#             while (i < j) and (myList[j] >= base):
#                 j = j - 1

#             # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
#             myList[i] = myList[j]

#             # 同样的方式比较前半区
#             while (i < j) and (myList[i] <= base):
#                 i = i + 1
#             myList[j] = myList[i]
#         # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
#         myList[i] = base

#         # 递归前后半区
#         QuickSort(myList, start, i - 1)
#         QuickSort(myList, j + 1, end)
#     return myList


# myList = [49, 38, 65, 97, 76, 13, 27, 49, 1, 66, 77, 8, 88, 99, 11]
# print("Quick Sort: ")
# QuickSort(myList, 0, len(myList) - 1)
# print(myList)
