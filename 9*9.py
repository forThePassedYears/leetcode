

# print('\n'.join(' '.join([f'{x}*{y}={x*y:2}' for x in range(1, y + 1)]) for y in range(1, 10))
print(
    '\n'.join(
        [' '.join([f'{x}*{y}={x*y}' for x in range(1, y + 1)]) for y in range(1, 10)])
)

# print(''.join(['{}*{} = {}'.format(i, j, i * j)
#                for i in range(1, 10) for j in range(1, 10)]))
