# Newton-Raphson for square root 
# Find x such that x**2 - 24 is within epsilon of 0

eps = 0.01
# initial given value
initVal = 25.0



def newt(eps, initVal, root): 
    initVal = float(initVal)
    guess = initVal/2.0
    TotalGuesses = 0
    while abs(abs(guess)**root- abs(initVal)) >= eps:
        TotalGuesses += 1
        guess = guess - (((guess**root) - initVal)/(root*guess**(root-1)))

    print (f'Total guesses (Newton-Raphson): {TotalGuesses}')
    print (f'The square root of {initVal} is about {round(guess,len(str(eps)))}')
    return TotalGuesses

def bisec(eps, initVal, root):
    high = max(1.0, initVal) if initVal > 0 else min(-1.0, initVal)
    low = 0.0
    guess = (high + low)/2.0
    totalGuesses = 0

    # while the difference of initVal and cubed guess isn't eps or bigger 
    while abs(abs(guess)**root - abs(initVal)) >= eps:
        
        totalGuesses += 1
        # if cubed guess is bigger than initVal, low should be current value of guess, else high takes the value 
        if abs(guess**root) < abs(initVal): 
            low = guess 
        else: 
            high = guess
        # updates guess
        guess = (high + low)/2.0

    # prints total guesses and guesswer
    print (f'Total guesses (bisectional): {totalGuesses}')
    print (f'{round(guess,len(str(eps)))} is close to sqrt of {initVal}')
    return totalGuesses


newt(eps, initVal, 2)
bisec(eps, initVal, 2)

print(f"Newton's method is {(bisec(eps, initVal, 2) / newt(eps, initVal, 2) )} times faster")