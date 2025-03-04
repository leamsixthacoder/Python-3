import pickle

class Person:
    age = 45
    name = 'John Smith'
    kids = ['Pete', 'Lilly', 'Kate']
    employers = {'AWS': 2022, 'Microsoft': 2018, 'Yahoo': 2005}
    shoe_sizes = (11,12)
    
def serialize(obj):
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f'Serialized object: \n{pickled}\n')
    return pickled

def deserialize(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized: \n{unpickled}\n')
    
def deserialize_employees(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized Kids: \n{unpickled.kids}\n')

def obj_to_file(fn, obj):
    with open(fn, 'wb') as pf:
        pickle.dump(obj, pf, protocol=pickle.HIGHEST_PROTOCOL)
        
def file_to_obj(fn, obj):
    with open(fn, 'rb') as pf:
        obj = pickle.load(pf)
        print(obj)
        return obj
    

# pickled = serialize(Person())
# deserialize(pickled)
# deserialize_employees(pickled)

# obj = obj_to_file('person.xyz', Person())
# person = file_to_obj('person.xyz', obj)