
def boomlulu_sort(alist):
    '''冒泡排序
    最优时间复杂度 O(n)  即遍历一次没有发现任何可以交换的元素
    最坏时间复杂度 O(n**2)
    稳定性： 稳定
    '''
    n = len(alist)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


if __name__ == '__main__':
    alist = [49, 38, 65, 97, 76, 13, 27, 49, 1, 66, 77, 8, 88, 99, 11]
    print(alist)
    boomlulu_sort(alist)
    print(alist)
