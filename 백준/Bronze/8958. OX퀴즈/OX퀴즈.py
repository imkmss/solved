import sys
input = sys.stdin.readline

T=int(input().strip())

for i in range(T):
    quiz=input().strip()
    stack=0
    score=0
    for ch in quiz:
        if ch=="O":
            stack+=1
            score+=stack
        else:
            stack=0
    print(score)