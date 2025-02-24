import os

def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

def stars_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)
            

# ends_with('../files', '.txt')
# stars_with('../files', '01_test')