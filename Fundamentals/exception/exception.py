# if you do not know where the bug is, or you want to handle errors with effective methods

try :
    mvar = 10
    svar = 20
    rvar = mvar + svar
    fp_read = open('Hey! I do not exist!', mode='r')
    buffer = fp_read.read()
except IOError as err :
    print('IO throws an exception, file might not exists')
finally :
    print('you fxxk it up, dude!')
    print(rvar)