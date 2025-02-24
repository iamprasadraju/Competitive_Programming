def team():
    count = 0
    n = int(input())
    for _ in range(n):
        seq = input().split()
        a, b, c = map(int, seq)
        if a + b + c >= 2:
            count += 1
    print(count)

team()