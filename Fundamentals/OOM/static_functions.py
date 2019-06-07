# static functions can be called when there is no instance from class in scope

class MyClass : 
    def PubMemFunc(self) :
        print("I can be called from an instance")
    # use decorational word to declare a static method
    @staticmethod
    def StaticMemFunc() : 
        print("I can be called directly from class type!")

# directly use class name to call static function
MyClass.StaticMemFunc()

# use instance to call ordinary member function
myclass = MyClass()
myclass.PubMemFunc()
# you can also use instance to call static method, but this is not recommeded!
myclass.StaticMemFunc()