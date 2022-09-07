# asking to input desired number to find if a perfect relation can be made such that root**pwr=num is the output and 0 < pwr < 
num = int(input('enter number: '))
root = 0
pwr = 1
# var step determinates if loop should go +1 or -1 according to num 
step = 1 if num >= 0 else -1

found = False
while root**pwr > num:
    for pwr in range (1,6):
        for root in range(0, num + 1,step):
            if root**pwr == num:
                print('ANS:', root, '**', pwr, '=', num)
                found = True
                
if found == False: 
    print('no number that would result in root**pwr when 0<pwr<6 where found. Restart and try another number.')