import os
from pathlib import Path


def rename_file(src, dst):
    os.rename(src, dst)
    
    
def rename_file2(src, dst):
    f = Path(src)
    f.rename(dst)
    
    
# rename_file('../files/subfolder/text.txt', '../files/subfolder/test.txt')
rename_file('../files/subfolder/test.txt', '../files/subfolder/text.txt')