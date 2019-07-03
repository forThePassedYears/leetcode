
def digui(num, a, b, c):
    if num == 1:
        print(a, '--->', c)
        return
    else:
        digui(num - 1, a, c, b)
        print(a, '--->', c)
        digui(num - 1, b, a, c)


num = input('Number:')
digui(int(num), 'A', 'B', 'C')
