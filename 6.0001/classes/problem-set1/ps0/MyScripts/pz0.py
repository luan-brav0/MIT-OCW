from math import log2

num1 = input('Enter the value X: ')
num2 = input('Enter the value Y: ')
x = int(num1)
y = int(num2)
print ('%d**%d = %d' % (x, y,x**y))
print('log(%d) = %d' % (x, log2(x)))

print(log2(2))