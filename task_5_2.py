

def nums_generator(n):
    sum = 0
    for num in range(1, n + 1, 2):
        if num**2 < 200:
            sum += num
            yield (num, sum)
