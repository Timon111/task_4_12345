str = input("Введите строку чисел:")
seen = set()
result = [x for x in str.split(' ') if x not in seen and not seen.add(x)]
print(result)