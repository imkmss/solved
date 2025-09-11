import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    H, W, N = map(int, input().split())

    floor = N % H if N % H != 0 else H
    # 호수(열)
    room = (N // H) + 1 if N % H != 0 else (N // H)

    # 층+호수를 붙여서 출력 (호수는 항상 2자리 이상)
    print(f"{floor}{room:02d}")
    # 같음: print(str(floor) + str(room).zfill(2))