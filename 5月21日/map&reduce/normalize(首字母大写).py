def normalize(name):
    return '%s' % (name[:1].upper()+name[1:].lower())
L=['zl','lV','ZY']
print(list(map(normalize,L)))