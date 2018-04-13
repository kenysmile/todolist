a = ('2',)
items = ['o', '2', 'd', 'o']

l = list(a)

for x in items:
   # l.append(x)

    if x == a:
        print(a)
    else:
        print(tuple(l))

