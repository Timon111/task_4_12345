from os import mkdir, makedirs, getcwd, remove
from os.path import join, exists
from shutil import copy, copy2, copytree

main_name = "l7"
sub1_name = "subdir1"
sub2_name = "subdir2"
main_path = join(".", main_name, sub1_name, sub2_name)
#if not exists(main_path):
#    makedirs(main_path)
#
#lst_dir = ["dir1","dir2"]
#for dir in lst_dir:
#    mkdir(join(".",dir))

#lst_file = ["file1.txt","file2.bin"]
#for file in lst_file:
#    with open(join(".",file), encoding="utf-8", mode="w") as write_file:
#        pass