#1
test_list = ['one','two','three']
for a in test_list:
    print(a)

#2
arr = [(1,2),(3,4),(5,6)]
for (front, end) in arr:
    print(front+end)

#3
marks=[90,25,67,45,80]
number = 0
for a in marks:
    number += 1
    if a >=70:
        print("%d통과" % number)
    else:
        continue

#4
sum = 0
for i in range(1,11):
    sum += i
print(sum)

#5_개인연습
for i in range(1,11):
    print("*",end="") #줄바꿈방지하는방법
print()

#6
a = [1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)

#7
result=[x*y for x in range(1,11)
        for y in range(2,11)]
print(result)