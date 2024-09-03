while True:
    s=input('Enter String ')
    if len(s)==10:
        print(s[:2])
        print(s[1::-1])
        print(s[8:10])
        print(s[9:7:-1])
        print(s[3:7])
        print(s[6:2:-1])
        print(s[:9:2])
        print(s[9::-2])
        break
    else:
        print("Enter String of lrngth 10")