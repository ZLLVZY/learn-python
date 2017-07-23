try:
    data=open('sketch.txt')
    '''for each_line in data:
    (role,line_spoken)=each_line.split(':',1)
    print(role,end='')
    print(' said:',end='')
    print(line_spoken,end='')
    无处理
    for each_line in data:
    if not each_line.find(':')==-1:
        (role,line_spoken)=each_line.split(':',1)
        print(role,end='')
        print(' said:',end='')
        print(line_spoken,end='')
        针对所有数据的格式写出逻辑'''
        #print(data.readline(),end='')
        #data.seek(0)
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print(' said:',end='')
            print(line_spoken,end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
