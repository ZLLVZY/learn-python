def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)
    
with open('james.txt') as jam,open('julie.txt') as jul,open('mikey.txt') as mik,open('sarah.txt') as sar:
    data=jam.readline()
    james=data.strip().split(',')
    data=jul.readline()
    julie=data.strip().split(',')
    data=mik.readline()
    mikey=data.strip().split(',')
    data=sar.readline()
    sarah=data.strip().split(',')
clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
for each_item in james:
    clean_james.append(sanitize(each_item))
for each_item in julie:
    clean_julie.append(sanitize(each_item))
for each_item in mikey:
    clean_mikey.append(sanitize(each_item))
for each_item in sarah:
    clean_sarah.append(sanitize(each_item))
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))