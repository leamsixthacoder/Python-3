import os, fnmatch

def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)
            
            
# match('../files', '*_file*.*')
# match('../files', '*2_*_*.*')
# match('../files', '*_file_*.*')