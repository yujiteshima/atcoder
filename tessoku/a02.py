# Linear Search
N, X = map(int, input().split())

A = list(map(int, input().split()))

found = False

for a in A:
    if X == a:
        found = True

if found:
    print("Yes")
else:
    print("No")
