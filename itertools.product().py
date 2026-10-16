from itertools import product

input1 = list(map(int, input().split()))
input2 = list(map(int, input().split()))

answer = list(product(input1, input2))
print(*answer)