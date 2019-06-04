def my_function(input_para1) : 
    print('this is an input parameter %s' % input_para1)
    return

my_function(100)

def ret_function(input_para1) : 
    res = input_para1 + 4343
    return res

mvar = ret_function(1000)
print(mvar)

# function with default parameters
def default_para_function(input_para1 = 1000) : 
    return input_para1 + 5000
print(default_para_function())
print(default_para_function(0))

# function with unknown number of parameters
def tuple_function(input_para1 = 4000, *the_rest_paras) : 
    print(input_para1)
    print(the_rest_paras)
tuple_function(0, 2, 4, 6, 8, 10)

def null_function(input_para1) : 
    # if you do nothing, there must be a declaration!
    pass

null_function(222)