n = int(input())
s = str('')
while n > 0:
    s = s + str(n % 2)
    n = n // 2
print(s[::-1])