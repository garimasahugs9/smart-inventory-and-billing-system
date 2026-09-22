# 1.Check whether a number is an Armstrong number.
'''
n = int(input("Enter a number: "))
copied = n
sum = 0
digit = len(str(n))
while copied>0:
    digit=copied%10
    sum = sum +digit**digit
    copied = copied//10

if sum==n:
    print("it is a armstromg number")
else:
    print("it is not a armstromg number")
'''
# 2.Check whether a number is prime.
"""n = int(input("Enter a number: "))
while n>=2:
    for i in range(2,n-1):
        if n%i=0 :
            print("not a prime number")"""
            
# 3.Print all prime numbers between 1 and N.
# 4.Find the largest digit in a number.
# 5.Find the smallest digit in a number.


num=abs(int(input()))
sum=0
while (num>0):
    rem = num%10

    sum = sum + rem
    num = num//10
print (sum)

