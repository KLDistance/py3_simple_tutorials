# a class with member variables and member functions
class MyClass :
    member_var1 = 15142
    member_var2 = 'I am a member of MyClass'
    def member_func1(self) :
        return "MyClass!"
    def member_func2(self, input_var) :
        return self.member_var1 + input_var

# declare an instance from "MyClass"
myclass = MyClass()
print(myclass.member_var1)
print(myclass.member_var2)
print(myclass.member_func1())
print(myclass.member_func2(10000))