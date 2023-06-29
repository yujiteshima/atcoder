N, Q = map(int, input().split())
A = list(map(int, input(split())))
# Caluculate the cumlative sum in advance
accum = [0] * N
accum[0] = A[0]
for i in range(1, N):
    accum[i] = accum[i-1] + A[i]
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    ans = accum[R+1] - accum[L]
    print(ans)
