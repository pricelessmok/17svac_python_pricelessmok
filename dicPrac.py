info = {'name':'lee', 'age':25, 'major':'computer'}
print(info)
print(info['name'])
print(info['age'])
print(info.keys())
for k in info.keys():
    print(k)

print(info.values())

test = info.get('name')
print(test)

print('name' in info)


