Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    if a ^ b == 0:
        print("YES")
    else:
        print("NO")