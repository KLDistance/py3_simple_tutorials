# To define a private member variable inside a class, use two underscores "__" in front of a variable name.

class MyClass1 : 
    pub_mem = 'I am public in MyClass1'
    __priv_mem = 'I am private in MyClass1'
    def func(self) : 
        print(self.pub_mem)
        print(self.__priv_mem)

mc1 = MyClass1()
# you can only directly use pub_mem!
print(mc1.pub_mem)
mc1.func()
print()

# To define a private member function inside a class, use two underscores "__" in front of a function name

class MyClass2 :
    def pub_func(self) : 
        print("This public member function is called.")
    def __priv_function(self) :
        print("You cannot reach here!")

mc2 = MyClass2()
# you can only directly call pub_func!
mc2.pub_func()