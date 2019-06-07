class MyClass : 
    i = 10
    def Func(self) : 
        print("Test function!")

# this is instance-level variable, not static
myclass = MyClass()
print(myclass.i)

# it is weird to assign a value directly to class static variables, since this is not pre-defined!
# but actually it can be done when you want to give a class, not an instance, a static property.
MyClass.j = 10
print(MyClass.i)
MyClass.j += 2
print(MyClass.j)
print(myclass.i)
print()
# when you try to give the static variable the same name as one in the class non-static variable, the value is altered!
MyClass.i += 100
print(MyClass.i)
print(myclass.i)
print()
# this makes later new instances hold the different inialized member value!
myclass2 = MyClass()
print(myclass2.i)
print(MyClass.i)