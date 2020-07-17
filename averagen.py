sum = 0
count = 0
print("Please enter 10 numbers: ")
while count < 10:
    number = float(input())
    sum = sum + number
    count += 1
average = sum / 10
print("N=10,sum={}".format(sum))
print("average = {:2f}".format(average))
