list = [1, 5, 6, 7, 8,[0,1,2]]
print(list[5][0])
print(list[5][0]+list[5][1])
print(list[:4])
print(list[5][:2])
list2 = [9,8,7]
print((list+list2)*2)
list[2] = 8
print(list)
list[:3] = [8,8,8]
print(list)
del list[5]
print(list)
list.sort()
print(list)
list.reverse()
print(list)
print(list.index(7))
print(list.count(8))
list.extend(list2)
print(list)