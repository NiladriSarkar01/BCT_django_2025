s={}
print(type(s))
s=set()
print(type(s))

s.add(2)
s.add(4)
s.add(5)
s.add(4)
print(s)
s.remove(2)
s.discard(2)
# s.clear()
s1={4, 6, 7, 8, 2}
s.update(s1)
print(s)

s0={3, 4, 6}
s2={3, 4, 7, 8, 9}

print(s0)
print(s0.difference(s2))
print(s0.intersection(s2))
print(s0.union(s2))
print(s0.isdisjoint(s2))
print(s0.issubset(s2))
print(s0.issuperset(s2))
print(s0.symmetric_difference(s2))


