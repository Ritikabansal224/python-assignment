number= int(input("enter number"))
num = number
reverse = 0
while (number > 0):
        reminder = number % 10
        reverse = (reverse * 10) + reminder
        number = number // 10
if (num == reverse):
        print(True)
else:
        print(False)