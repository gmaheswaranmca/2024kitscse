'''
    conditional stmts 
    list, tuple, set, dict 
    def 
    class 

    find total sal of array of three emp objects 
'''

class Emp:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary 
    def __str__(self):
        return f'[name={self.name},salary={self.salary}]'
    def __repr__(self):
        return self.__str__()
    
employees = [
    Emp('dravid',20000),
    Emp('ganguli',30000), 
    Emp('sachin',25000) 
]
tot = 0.0
for e in employees: # element iterator
    tot += e.salary
    print(e)        # print each emp 
print(f'total sal is {tot}')

