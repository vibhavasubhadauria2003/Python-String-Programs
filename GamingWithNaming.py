s=input("Enter String ")
s=s.lower()
s1=""
for i in range(0,len(s),1):
    n=97
    while n<=122:
        print(s1+chr(n))
        if chr(n)==s[i]:
            s1=s1+chr(n)
            break
        n=n+1