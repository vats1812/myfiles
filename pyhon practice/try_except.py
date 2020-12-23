print("enter number one")
num1=input()
print("enter number two")
num2=input()

try:
    print("the sum of these number is", int(num1)+int(num2))
except Exception as b:
    print(b,"\nyou entered wrong")

print("this is very inportant part of this progrram")