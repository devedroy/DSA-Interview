n = int(input())
i = 1
while i <= n:
    j = 1
    k = 1
    while j <= n - i + 1:
        print(k,end="")
        j += 1
        k += 1
    print()
    i += 1

