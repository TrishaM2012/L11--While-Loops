num = int(input("Enter a number: "))
sum = 0
temp = num
while temp>0:
    digit = temp % 10
    sum += digit ** 3
    temp  //= 10
    
if num == sum:
    print("Its an Armstrong Number")
else:
    print("It's not an Armstrong Number")
    
 