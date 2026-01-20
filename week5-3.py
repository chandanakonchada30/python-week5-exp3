#24331A05E2
#factorial calculation (with recursion)
num=int(input("enter a number: "))
def fact(num):
    if num==1 :
        return 1
    else:
        return num*fact(num-1)
print("factorial of",num,"is",fact(num))
#factorial calculation(without using recursion)
num=int(input("enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial of",num,"is",fact)