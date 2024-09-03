s=input("Enter String ")
n=-1
c=s.count('T')
for i in range(1,c+1):
    n=s.find('T',n+1)
    print(n)
s=s.replace('T','t')
print(s)