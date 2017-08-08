def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
            return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return(None)
        
james=get_coach_data('james.txt')
julie=get_coach_data('julie.txt')
mikey=get_coach_data('mikey.txt')
sarah=get_coach_data('sarah.txt')
'''with open('james.txt') as jam,open('julie.txt') as jul,open('mikey.txt') as mik,open('sarah.txt') as sar:
    data=jam.readline()
    james=data.strip().split(',')
    data=jul.readline()
    julie=data.strip().split(',')
    data=mik.readline()
    mikey=data.strip().split(',')
    data=sar.readline()
    sarah=data.strip().split(',')'''
    
'''for each_item in james:
    clean_james.append(sanitize(each_item))
for each_item in julie:
    clean_julie.append(sanitize(each_item))
for each_item in mikey:
    clean_mikey.append(sanitize(each_item))
for each_item in sarah:
    clean_sarah.append(sanitize(each_item))'''
    
'''james=sorted([sanitize(each_item) for each_item in james])
unique_james=[]
for each_item in james:
    if each_item not in unique_james:
        unique_james.append(each_item)
print(unique_james[:3])

julie=sorted([sanitize(each_item) for each_item in julie])
unique_julie=[]
for each_item in julie:
    if each_item not in unique_julie:
        unique_julie.append(each_item)
print(unique_julie[:3])

mikey=sorted([sanitize(each_item) for each_item in mikey])
unique_mikey=[]
for each_item in mikey:
    if each_item not in unique_mikey:
        unique_mikey.append(each_item)
print(unique_mikey[:3])

sarah=sorted([sanitize(each_item) for each_item in sarah])
unique_sarah=[]
for each_item in sarah:
    if each_item not in unique_sarah:
        unique_sarah.append(each_item)
print(unique_sarah[:3])'''
print(sorted(set(sanitize(each_item) for each_item in james))[:3])
print(sorted(set(sanitize(each_item) for each_item in julie))[:3])
print(sorted(set(sanitize(each_item) for each_item in mikey))[:3])
print(sorted(set(sanitize(each_item) for each_item in sarah))[:3])