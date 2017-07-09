movies=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print(movies[4][1][3])
print(movies)
'''for each_item in movies:
#    print(each_item)
    if isinstance(each_item,list):
        for sub_list in each_item:
            print(sub_list)
    else:
        print(each_item)'''
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)