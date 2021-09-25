n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n > m:
    n, m = m, n
print(min(x, n - x, y, m - y))