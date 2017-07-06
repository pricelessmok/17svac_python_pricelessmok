def sum(a,b):
    return a+b

print(sum(1,2))

def hello():
    return 'hello'
print(hello())

a = sum(3,4)
print(a)

#3 *입력변수 이렇게 찍으면 튜플로 한 뭉탱이로 잡힌다.
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum_many(1,2,3)
print(result)

#4
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = sum_mul('sum',1,2,3,4,5)
print(result)
result = sum_mul('mul',1,2,3,4,5)
print(result)

#5
def sum_and_mul(a,b):
    return a+b, a*b
result = sum_and_mul(3,4)
print(result)

#6 return에 대한 학습내용
def say_nick(nick):
    if nick == '바보':
        return
print(say_nick('바보'))

#7
def say_myself(name, old, man=True):
    print("제 이름은 %s 입니다" %name)
    print("저는 %d살 입니다" %old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
say_myself("lee",25,False)

say_nick("바보")

#8 변수의 유효범위
a = 1
def vartest(a):
    a += 1
    return a
print(vartest(a))
print(a)