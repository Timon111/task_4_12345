import os
print(os.getcwd())
users = []
hobby = []
rezult = []
with open("FIO.txt", 'r+', encoding="utf-8") as myfile1:
    with open("HOBBY.txt", 'r+', encoding="utf-8") as myfile2:
        with open("rezult.txt", 'r+', encoding="utf-8") as myfile3:
            for line in myfile1:
                i = 0
                str1 = ''
                for i in range(len(line)):
                    if i == 0:
                        str1 += line[i]
                    elif line[i] == ',':
                        str1 += line[i+1]
                users.append(str1)
            for line in myfile2:
                hobby.append(line)
            rezult = dict(zip(users, hobby))
            print(rezult)
            myfile3.write(str(rezult))