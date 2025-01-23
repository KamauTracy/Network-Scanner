class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

import pandas as pd 

mydataset = {
    'cars':["BMW", "Volvo", "Ford"],
    'passings':[3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)