T=int(input().strip())

for i in range(T):
    a,b=(input().split())
    a = int(a)
    result=""

    for j in b:
        result+=j*a
    print(result)
