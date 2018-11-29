def abc():
    for a in range(0,500):
        for b in range(0, 500):
            for c in range(0, 500):
                if a<b<c:
                    if a+b+c == 1000:
                        if a**2+b**2 == c**2:
                            return a,b,c



a,b,c =abc()
print(a*b*c)
