import re
import os
print(os.getcwd())
with open("test.txt", 'r+', encoding="utf-8") as myfile:
    new_tuple = []
    for line in myfile:
        pattern = re.compile("(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) - - [[](\d{1,2}\/\w{1,9}\/\d{4}[:]\d{2}[:]\d{2}[:]\d{2}[ ][+]\d{4})[]] \"(\w{3,4}) (\/downloads\/product[_]\d{1,2}) HTTP\/1.1\" (\d{1,3}) (\d{1,3})")
        print(f"parset_raw = {tuple(pattern.findall(str(line)))}")