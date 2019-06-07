# destructor is called when you use "del" command, or the instance run out of the scope.
# use '__del__' to declare and define the deconstructor

class MyClass : 
    def __init__(self) : 
        print('constructor is called!')
    def __del__(self) : 
        print('destructor is called!')

# here we see the del effect
myclass1 = MyClass()
del myclass1

# here we make some scenarios to see the scope effect
print()
# first, "if" is not an effective scope for destructor
mvar = 1
myclass2 = None
if mvar == 1 : 
    myclass2 = MyClass()
else :
    print('Check to see this impossible option.')
print('Out of "if" scope!\n')

# second, "for" or "while" loops are semi-effective scopes for destructor
# that is because the myclass_tmp is redefined in the loop, and you notice that desctructor is called at last
for i in range(4) : 
    myclass_tmp = MyClass()
print('Out of "for" scope!\n')

# third, functions are fully-effective scopes for destructor
def des_test() : 
    myclass_test = MyClass()

des_test()
print('Out of "function" scope!\n')
