from itertools import count

c1 = count(10, 2)
r1 = range(10, 100, 2)
# print(hasattr(c1, '__iter__'))
# print(hasattr(c1, '__next__'))
# print(hasattr(r1, '__iter__'))
# print(hasattr(r1, '__next__'))


print('count')
for i in c1:
    if i > 100:
        break
    print(next(c1))
print()

print('range')
for i in r1:
    if i > 100:
        break
    print(next(r1))  # vai dar erro pq n se chama next no range
