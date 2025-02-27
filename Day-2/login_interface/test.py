import ast
with open('./data.txt', 'r') as mf:
    l=mf.read().split(';')
    print(l)
    l.pop()
    for u in l:
        print(u)
        u=u.strip('{')
        u=u.strip('}')
        u=u.replace("'", "")
        print(u)
        res = []
        for sub in u.split(', '):
            if ':' in sub: 
                res.append(map(str.strip, sub.split(':', 1))) 
        res = dict(res)
print(res)
print(type(res))

print(res['password'])
        