s=input("Enter String ")
s=s.upper()
countA=s.count('A')
countE=s.count('E')
countI=s.count('I')
countO=s.count('O')
countU=s.count('U')
tcount=countA+countE+countI+countO+countU

if countA>0:
    print("Count of A ",countA)
if countE>0:
    print("Count of E ",countE)
if countI>0:
    print("Count of I ",countI)
if countO>0:
    print("Count of O ",countO)
if countU>0:
    print("Count of U ",countU)

if tcount>0:
    print("Total vowels in string is ",tcount)
else:
    print("No Vowels in string")