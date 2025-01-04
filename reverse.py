a=int(input("Enter the 5 digit number :- "))

num=a//10000
print(num)
num2=(a//1000)%10
print(num2)
num3=(a//100)%10
print(num3)
num4=(a//10)%10
print(num4)
num5=a%10
print(num5)

reverse=num5 * 10000+num4* 1000+num3 * 100+num2* 10+num
print(reverse)