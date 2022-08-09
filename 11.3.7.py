mylist = []
count = 1
for i in range(97, 123):
    #for j in range(1, 27):
    mylist.append(chr(i) * count)
    count += 1
print(mylist)
