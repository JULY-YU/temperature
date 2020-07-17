F=0
print("Please enter: ")
while F <= 250:
    F=int(input())
    C=(F - 32) / 1.8
    print("F = {:5d},C = {:7.2f}".format(F,C))
