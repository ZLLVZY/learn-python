class NamedList(list):
    def __init__(self,a_name):
        list.__init__([])
        self.name=a_name
        
johnny=NamedList('John Paul Jones')
johnny.append('Bass Player')
johnny.extend(['Composer','Arranger','Musician'])
print(johnny)
print(johnny.name)
for attr in johnny:
    print(johnny.name+'is a '+attr+'.')