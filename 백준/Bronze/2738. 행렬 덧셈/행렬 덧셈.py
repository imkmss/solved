N, M = map(int, input().split())

arr1 = [[0]*M for _ in range(N)]
arr2 = [[0]*M for _ in range(N)]
arr3 = [[0]*M for _ in range(N)]

#배열1만들기
for i in range(N):
    row=list(map(int, input().split()))
    arr1[i]=row

#배열2만들기
for j in range(N):
    row=list(map(int, input().split()))
    arr2[j]=row

#배열3=배열1+배열2 행렬덧셈
for i in range(N):
    for j in range(M):
        arr3[i][j]=arr1[i][j]+arr2[i][j]
        print(arr3[i][j], end=" ")
    print()