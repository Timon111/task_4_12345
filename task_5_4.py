str = input("Введите строку чисел:")
str1 = str.split(' ')
str2 = str1.copy()
str2.pop(0)
result = []
i = 0


def nums(n):
    i = 0
    for n[i] in n:
        yield n[i]


n = nums(str2)
p = nums(str1)
for i in range(len(str1)-1):
    nex = int(next(n))
    pre = int(next(p))
    #print((f'Предыдущий: {pre}', f'Следующий: {nex}'))
    if nex > pre:
        result.append(nex)
print(f'src: {str1} \n result: {result}')

#300 2 12 44 1 1 4 10 7 1 78 123 55