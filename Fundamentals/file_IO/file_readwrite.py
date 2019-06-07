mvar = "A file IO example.\nThis example contains two lines."

filePath = './file_readwrite_text.txt'
hFile = open(filePath, mode='w', encoding='utf8')
hFile.write(mvar)
# you can use close only
hFile.flush()
hFile.close()

hFile2 = open(filePath, mode='r', encoding='utf8')
# read all the contents in the file
fileStr = hFile2.read()

print(fileStr)
hFile2.close()

# it is very essential to close the file in the right place.
# to let the file be accessed by other operations such as delete or rewrite!

# other detailed parameters see https://www.runoob.com/python3/python3-file-methods.html