#from nester import print_lol
import pickle
man=[]
other=[]
try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()           
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
print(man)
print(other)
'''try:
    man_file=open('man_data.txt',"w")
    other_file=open('other_data.txt',"w")
    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print("File error.")
finally:
    if man_file in locals():
        man_file.close()
    if other_file in locals():   
        other_file.close()'''
try:
    with open('man_data.txt',"wb") as man_file,open('other_data.txt',"wb") as other_file:
        '''print_lol(man,fh=man_file)
        print_lol(other,fh=other_file)'''
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('File error:'+ str(err))
except pickle.PickleError as perr:
    print('Pickling error:'+ str(perr))