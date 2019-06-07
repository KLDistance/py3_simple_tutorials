mvar1 = 1
def func1(input_var) : 
    # if you want to change global variable inside a function, use "global" keyword to redeclare the global variable
    # this is because Python reinterpreter consider it is usually unsafe to change global value inside a function
    global mvar1
    mvar1 += 1
    print(mvar1 + input_var)

func1(10)
print(mvar1)
print()

# if you just want to use a global value but do not make any alternation, "global" is not necessary
mvar2 = 1
def func2(input_var) : 
    print(mvar2 + input_var)

func2(10)
print(mvar2)