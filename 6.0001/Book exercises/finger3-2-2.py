# list = []
# print(len(list))
# l=0

# #
# # print(type(list[l]))

# try: 
#     list[l] += 'd'
# except ValueError:
#     list.insert(l, 'd')

# print(list[l])

s = '1.23,2.4,3.123'

# s = s.split(',')
# ans = 0
# for n in range(len(s)):
#     ans +=  float(s[n])
#     print (ans)
ans = 0
num = ''
for d in range(len(s)):
    if s[d] != ',': 
        num += s[d]
    else: 
        ans += float(num)
        num = ''
print(ans)

        

        