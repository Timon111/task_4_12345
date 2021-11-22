from os import mkdir, makedirs, getcwd, remove
from os.path import join, exists
from shutil import copy, copy2, copytree

dir1 = ["my_project"]
dir2 = ["settings", "mainapp", "authapp"]
setting_file = ["__init__.py", "dev.py", "prod.py"]

mainap_file = ["__init__.py", "models.py", "views.py"]
mainap_dir =["templates"]
template_dir = ["mainapp"]
mainap2_file = ["base.html", "index.html"]

authapp_file = ["__init__.py", "models.py", "views.py"]
authapp_dir =["templates"]
template2_dir = ["mainapp"]
authapp2_file = ["base.html", "index.html"]
if not exists(dir1[0]):
    for dir in dir1:
        mkdir(join(".",dir))

    for dir in dir2:
        mkdir(join("my_project",dir))
    for file in setting_file:
        with open(join(dir1[0],dir2[0],file), encoding="utf-8", mode="w") as write_file:
            pass
    #2
    for dir in mainap_dir:
        mkdir(join(dir1[0],dir2[1],dir))
    for file in mainap_file:
        with open(join(dir1[0],dir2[1],file), encoding="utf-8", mode="w") as write_file:
            pass
    for dir in template_dir:
        mkdir(join(dir1[0],dir2[1],mainap_dir[0],dir))
    for file in mainap2_file:
        with open(join(dir1[0],dir2[1],mainap_dir[0],template_dir[0],file), encoding="utf-8", mode="w") as write_file:
            pass
    #3
    for dir in authapp_dir:
        mkdir(join(dir1[0],dir2[2],dir))
    for file in authapp_file:
        with open(join(dir1[0],dir2[2],file), encoding="utf-8", mode="w") as write_file:
            pass
    for dir in template2_dir:
        mkdir(join(dir1[0],dir2[2],authapp_dir[0],dir))
    for file in authapp2_file:
        with open(join(dir1[0],dir2[2],authapp_dir[0],template2_dir[0],file), encoding="utf-8", mode="w") as write_file:
            pass