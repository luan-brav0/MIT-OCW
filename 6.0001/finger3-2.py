# Devide and sum a series of floats in a string separated by commas

#given string
s = '1.23,2.4,3.123'

#total to be printed
total = 0
num = []
for n in s:
    if n is not ',':
        if not num[j]:
            num[j] = ''
        else:
            num += n
    else:
        j += 1
#digit index counter
j = 1

#list of numbers in string converted to 
nums = []

# analyses every digit d in string s
for d in s:
    #if digit is not a comma, add to list nums at index j
    if d is not ',':
        try: 
            nums[j] += d
        except ValueError:
            nums [j] = d
    #else, turn nums[j] into a float num and increase j by 1
    else:
        float(nums[j])
        j += 1