from os import mkdir, makedirs, getcwd, remove
from os.path import join, exists
from shutil import copy, copy2, copytree

lst_dir = ["my_project"]
lst_dir2 = ["settings", "mainapp", "adminapp", "authapp"]

if not exists("my_project"):
    for dir in lst_dir:
        mkdir(join(".",dir))
        for dir in lst_dir2:
            mkdir(join(lst_dir,dir))