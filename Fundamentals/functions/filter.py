# filter is able to filt the datatype which is regarded as null
result = filter(None, [1, 0, False, True])
print(list(result))

# restrict the filtering criteria to obtain odd numbers from 0 to 9
def odd(input_num) : 
    return input_num % 2

result2 = filter(odd, range(10))
print(list(result2))

# use lambda filtering is the same result
result3 = filter(lambda odd_num : odd_num % 2, range(10))
print(list(result3))