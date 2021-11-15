import os
from collections import Counter
print(os.getcwd())
with open("test.txt", 'r+', encoding="utf-8") as myfile:
    new_tuple = []
    for line in myfile:
        newl = str(line)

        for i in range(len(newl)):
            if newl[i] == '-':
                remote_addr = str(line[0:i-1])
                break

        new_tuple.append(str(remote_addr))

    s = new_tuple
    sublist, count = max(Counter(tuple(x) for x in s).items(), key=lambda x: x[1])
    print(list(sublist), count)
    #print('%s -> %d' % (list(sublist), count))
