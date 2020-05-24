num = int(input("Enter a position : "))
print("The Fibonacci series up to term " + str(num) + " is: ")
num1 = 0; num2 = 1; x = 0
mylist = [0, 1]
if num == 1 :
    print(mylist[:1])
elif num == 2 :
    print(mylist)
else :
    while x < num :
        sum = num1 + num2
        mylist.append(sum)
        num1 = num2
        num2 = sum
        x += 1
    print(mylist)
