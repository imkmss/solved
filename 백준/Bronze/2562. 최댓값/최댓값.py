numbers=[int(input().strip()) for _ in range(9)]

print(max(numbers))
print(numbers.index(max(numbers))+1)