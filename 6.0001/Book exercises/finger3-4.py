x = 27
guesses = 0
eps = 0.01
low = 0.0
high = max(1.0, x) if x > 0 else min(-1.0, x)
ans = (high + low)/2.0
while abs(abs(ans)**3 - abs(x)) >= eps:
    print(low, high, ans)
    guesses += 1
    if abs(ans**3) < abs(x): 
        low = ans 
    else: 
        high = ans
    ans = (high + low)/2.0
print ('guesses: ', guesses)
print(ans, ' is close to sqrt of ', x)
