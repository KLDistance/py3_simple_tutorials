# constructor is initially called when you create an instance from a class

class MyClass : 
    __mem1 = 0
    __mem2 = 'I have not been initialized!'
    def __init__(self) : 
        self.__mem1 = 1000
        self.__mem2 = 'I am initailized.'
        print('Constructor is called!')
    
    def Func(self) : 
        print(self.__mem1)
        print(self.__mem2)

# this step calls the __init__
myclass = MyClass()

myclass.Func()