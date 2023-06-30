D = int(input())
N = int(input())

diff = [0] * (D + 1)

for _ in range(N):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    diff[L] += 1
    diff[R+1] -= 1

accum = 0
for i in range(D):
    accum += diff[i]
    print(accum)
