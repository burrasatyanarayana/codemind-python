n=input().split()
n.sort()
n.sort(key=len)
print(*n)