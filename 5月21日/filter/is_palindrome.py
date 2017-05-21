def is_palindrome(n):
    s1=str(n)
    l=len(s1)
    l1=l//2
    i=0
    a=1
    while i<l1:
        k=-1*(i+1)
        a=0
        if s1[i]==s1[k]:
            a=1
        else:
            break
        i=i+1
    return a
print(list(filter(is_palindrome,range(1,1000))))	