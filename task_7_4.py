import os
import codecs
from os import listdir
from os.path import join, exists, getsize
from shutil import copy, copy2, copytree

files = []
keys = [10,100,1000,10000,100000,1000000]
files = [0, 0, 0, 0, 0, 0]
folder = join(".", "some_data_adv")
for file in listdir(folder):
    if 10 < getsize(join(".", "some_data_adv",file)) < 100:
        files[1] = files[1] + 1
    elif getsize(join(".", "some_data_adv",file)) < 1000:
        files[2] = files[2] + 1
    elif getsize(join(".", "some_data_adv",file)) < 10000:
        files[3] = files[3] + 1
    elif getsize(join(".", "some_data_adv",file)) < 100000:
        files[4] = files[4] + 1
    elif getsize(join(".", "some_data_adv",file)) < 1000000:
        files[5] = files[5] + 1
a = dict(zip(keys, files))
print(a)
