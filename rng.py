def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

cho = input("선택 하세요(1/2):")

num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

if cho == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif cho == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

else:
    print("1~2 사이의 수만 입력해주세요")