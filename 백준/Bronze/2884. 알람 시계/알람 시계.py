H,M=map(int,input().split())

if 45-M>0:
    if H==0:
        print(23, 60-(45-M))
    else:
        print(H-1, 60-(45-M))
else:
    print(H, abs(45-M))