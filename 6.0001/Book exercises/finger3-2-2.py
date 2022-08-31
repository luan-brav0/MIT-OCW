import timeit
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
def f1(s):
    ans = sum(map(float, s.split(",")))
    print (ans)
    return
def f2(s):
    for d in range(len(s)):
        if s[d] != ',': 
            num += s[d]
        else: 
            ans += float(num)
            num = ''
    print(ans)
    return

    
timeit.timeit("f1(s)", setup="from __main__ import f1, f2;s='1.23,2.4,3.123'")



        

        