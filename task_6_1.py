import os
print(os.getcwd())
with open("test.txt", 'r+', encoding="utf-8") as myfile:
    new_tuple = []
    for line in myfile:
        newl = str(line)


        for i in range(len(newl)):
            if newl[i] == '-':
                remote_addr = str(line[0:i-1])
                break

        for i in range(len(newl)):
            if newl[i] == ']' and newl[i+6] == ' ':
                request_type = str(line[i+1:i+6])
                break
            elif newl[i] == ']' and newl[i+7] == ' ':
                request_type = str(line[i+1:i+7])
                break

        for i in range(len(newl)):
            if newl[i:i+2] == "do":
                requested_resource = str(line[i:i+19])
                break
        new_tuple.append((remote_addr, request_type, requested_resource))
    print(new_tuple)