flag = 0
for e in range(1, 151):
    for a in range(1, e // 2 + 1):
        for b in range(e // 2, e // 2 + e // 4 + 1):
            for c in range(e // 2 + e // 4, e // 2 + e // 4 + e // 8 + 1):
                for d in range(e // 2 + e // 4 + e // 8, e + 1):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
                        print(a + b + c + d + e)
                        flag = 1
                        break
            if flag:
                break
        if flag:
            break
    if flag:
        break