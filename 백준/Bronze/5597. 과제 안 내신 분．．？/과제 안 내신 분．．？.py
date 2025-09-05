import sys

nums = set(map(int, sys.stdin.read().split()))
missing = sorted(set(range(1, 31)) - nums)
print(missing[0])
print(missing[1])