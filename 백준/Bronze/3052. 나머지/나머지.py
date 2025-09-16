A=[int(input().strip()) for _ in range(10)]
remain=set()

for a in A:
    remain.add(a%42)

print(len(remain))

