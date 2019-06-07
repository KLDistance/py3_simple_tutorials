class BaseClass : 
    base_var = 100
    def __init__(self, input_var) : 
        self.base_var += input_var
        print("base class constructor is called!")
    def BaseFunc(self) :
        print("base member function is called!")

class SubClass(BaseClass) : 
    sub_var = 400
    def __init__(self) :
        BaseClass.__init__(self, 200)
        print("sub class constructor is called!")
    def SubFunc(self) : 
        print("sub member function is called!")

subclass = SubClass()
subclass.BaseFunc()
subclass.SubFunc()
print(subclass.base_var)
print(subclass.sub_var)
