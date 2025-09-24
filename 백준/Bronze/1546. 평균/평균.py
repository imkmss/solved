N=int(input().strip())

scores=list(map(int,input().split()))
M=max(scores)

new_scores=[(x/M)*100 for x in scores]
print(sum(new_scores)/N)
