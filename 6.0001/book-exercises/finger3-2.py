
# Devide a series of floats in a string separated by commas present the total sum.

#given string
s = '1.23,2.4,3.123'

ans = 0
num = ''

for d in s:
    if d != ',': 
        num += d
    else: 
        ans += float(num)
        num = ''
# alternatively: 
# ans = sum(map(s.split(',')))
print(ans)