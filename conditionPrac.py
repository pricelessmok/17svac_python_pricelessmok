money = 1
if money:
    print("go")
else:
    print("stop")

x = 1
y = 2
print(x>y)

list = [1,2,3]
print(1 in list)

if 4 in list:
    pass
else:
    print("none")

treeHit = 0
while treeHit<10:
    treeHit += 1
    print("%d 번" % treeHit)
print("success")

arr = ['porsche','ferrarri','benz']
print("""1.porsche
2.ferrarri
3.benz
choice : """)
choice = int(input())
print(arr[choice-1])