def OuterFunc() : 
    print('This is an outer function')
    def InnerFunc() : 
        print('This is an inner function')
    InnerFunc()

OuterFunc()