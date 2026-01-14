import sys

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    queries = []
    max_k = 0
    max_n = 0

    for _ in range(T):
        k = int(input().strip())
        n = int(input().strip())
        queries.append((k, n))
        if k > max_k: max_k = k
        if n > max_n: max_n = n

    # dp[k][n] : k층 n호 (1-indexed for n)
    dp = [[0] * (max_n + 1) for _ in range(max_k + 1)]

    # 0층: n호 = n
    for n in range(1, max_n + 1):
        dp[0][n] = n

    # 점화식: dp[k][n] = dp[k][n-1] + dp[k-1][n]
    for k in range(1, max_k + 1):
        dp[k][1] = 1
        for n in range(2, max_n + 1):
            dp[k][n] = dp[k][n - 1] + dp[k - 1][n]

    out = []
    for k, n in queries:
        out.append(str(dp[k][n]))
    print("\n".join(out))

if __name__ == "__main__":
    main()