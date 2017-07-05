print ("hello world!")
print("""안녕하세요
저는
이용목 입니다.""")

print("No new line", end="");print(" ok") #자동 줄바꿈 제한

try:
    4/0
except ZeroDivisionError as e:
    print(e)

a=2+3j
b=3
print(a*b)

i=0
while i<4:
    i+=1
    print(i)