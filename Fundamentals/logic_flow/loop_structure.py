n = 100

sum = 0
counter = 1
while counter <= n : 
    sum = sum + counter
    counter += 1

print(sum)
print('')

list = [1, 3, 5, 7, 9]
for iter in list : 
    print('%d ' % iter)
print('')
for iter in range(1, 3, 1) : 
    print('%d ' % list[iter])