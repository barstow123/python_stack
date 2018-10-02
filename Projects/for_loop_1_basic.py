print('Basic')
for i in range(151):
    print(i)


print('\n\n\nMultiples of Five')
for x in range(5, 1000005, 5):
    print(x)


print('\n\n\nCounting the Dojo Way')
for x in range(101):
    if (x%5 == 0):
        print('coding')
        if (x%10 == 0):
           print('dojo')
    else :
        print(x)


print('\n\n\nWoah, That Sucker\'s Huge')
sum = 0
for x in range(0, 500000, 2):
    sum += x
    print('val: %d' % x)
print('sum is: %d' % sum)


print('\n\n\nCountdown By Fours')
for x in range(2018, 0, -4):
    print(x)


print('\n\n\nFlexible Count Down')
def FlexCountDown(lowNum, highNum, mult):

    while lowNum%mult != 0:
        lowNum += 1

    for x in range(lowNum, highNum+1, mult):
        print(x)

FlexCountDown(2,9,3)