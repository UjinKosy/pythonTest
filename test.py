n, k = map(int, input().split())


def cCount(n , k):
    if k > n:
        return 0
    if k == 0:
        return 1
    return cCount(n-1,k) + cCount(n-1,k-1)

print (cCount(n,k))