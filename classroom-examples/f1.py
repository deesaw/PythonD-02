def indexes(s="", char=''):
    st=0
    for i in range(s.count(char)):
            st= s.index(char, st+1)
            print(st)

indexes("hello",'l')