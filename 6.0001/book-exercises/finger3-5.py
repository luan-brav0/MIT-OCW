# Newton-Raphson for square root 
# Find x such that x**2 - 24 is within epsilon of 0
from doctest import NORMALIZE_WHITESPACE
from mimetypes import init


eps = 0.01
# initial given value
initVal = 24.0
# current guess number



def newt(eps, initVal, root): 
    guess = initVal/2.0
    TotalGuesses = 0
    while abs(guess**root - initVal) >= eps:
        TotalGuesses += 1
        guess = guess - (((guess**2) - initVal)/(2*guess))

    print (f'Total guesses (Newton-Raphson): {TotalGuesses}')
    print (f'The square root of {initVal} is about {guess}')
    return guess

def bisec(eps, initVal, root):
    high = max(1.0, initVal) if initVal > 0 else min(-1.0, initVal)
    low = 0.0
    ans = (high + low)/2.0
    totalGuesses = 0

    # while the difference of initVal and cubed ans isn't eps or bigger 
    while abs(abs(ans)**root - abs(initVal)) >= eps:
        print(low, high, ans)
        guesses += 1
        # if cubed ans is bigger than initVal, low should be current value of ans, else high takes the value 
        if abs(ans**3) < abs(initVal): 
            low = ans 
        else: 
            high = ans
        # updates ans
        ans = (high + low)/2.0

    # prints total guesses and answer
    print ('Total guesses (bisectional): ', guesses)
    print (ans, ' is close to sqrt of ', initVal)
    return ans

def compare(bisec,newt):
    eval(bisec)
    eval(newt)
    return bisec/newt
