number= int(input("enter number"))
while (number > 0):
        digit = number % 10
        number = number // 10

        print(digit,end=" ")