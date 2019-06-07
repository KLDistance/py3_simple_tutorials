import os

# now to recursively visit and store all the information of the total sub-directories
print('All the directories and file information tuples')
scan_dir_path = './directory_tourist_dir'
for iter in os.walk(scan_dir_path) : 
    print(iter)

print()
print('All the files')
# if we only care about all the files instead of directories
for iter in os.walk(scan_dir_path) : 
    for jter in iter[2] : 
        print(jter)