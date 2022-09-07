# based on the code sampled in the book, code a program that finds the square root of a given real number, 
# part 2 - now modiify to find the cube root

x = float(input('I want to find the cube root of...:'))
# guesses counter (displays at end numbers of tries)
guesses = 0

# epislon representing the level of accuracy of answer
eps = 0.01

# lowest avg point to meet ans
low = 0.0

# highest avg point to meet ans
# set to maximum value between 1 and x if x is positive, else the minimum value between -1 and x
high = max(1.0, x) if x > 0 else min(-1.0, x)

# answer takes half the average between high and low vars
ans = (high + low)/2.0

# while the difference of x and cubed ans isn't eps or bigger 
while abs(abs(ans)**3 - abs(x)) >= eps:
    print(low, high, ans)
    guesses += 1

    # if cubed ans is bigger than x, low should be current value of ans, else high takes the value 
    if abs(ans**3) < abs(x): 
        low = ans 
    else: 
        high = ans

    # updates ans
    ans = (high + low)/2.0

# prints total guesses and answer
print ('guesses: ', guesses)
print(ans, ' is close to sqrt of ', x)
