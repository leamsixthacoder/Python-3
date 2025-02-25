from dataclasses import dataclass
@dataclass(slots=True)
# use mypy to check datatype errors
class Project:
    name: str
    payment:int
    client: str
    
    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}")

@dataclass(slots=True)       
class Employee:
     name: str
     age: int
     salary: int
     project: Project
    

p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-soo", 38, 1000, p)
print(e.project)