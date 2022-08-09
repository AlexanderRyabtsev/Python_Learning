n = int(input())
mylist = []
mylist2 = []
for i in range(n):
    x = int(input())
    mylist.append(x)
    f = x ** 2 + 2 * x + 1
    mylist2.append(f)
print(*mylist, sep='\n')
print()
print(*mylist2, sep='\n')
