def read_txt(fn):
    with open(fn) as f:
        print(f.read())
        

def read_txt_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()
            
def write_new_txt(fn, str):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(str)
        

def append_line_txt(fn, str):
    with open(fn, 'a', encoding= 'utf-8') as f:
        f.write('\n')
        f.write(str)
        
        
# read_txt('../../Classes_and_Object-oriented_Programming/Abstraction_and_Encapsulation/properties_decoradors.py')
# read_txt_by_line('../../Classes_and_Object-oriented_Programming/Abstraction_and_Encapsulation/properties_decoradors.py')
# write_new_txt('example.txt', 'This was a good thing')
# append_line_txt('example.txt', 'This another line a good thing')