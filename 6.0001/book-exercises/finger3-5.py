# Newton-Raphson for square root 
# Find x such that x**2 - 24 is within epsilon of 0
# although the book is about to teach functions in python in the subsequent part of the book. I opted to use functions for this exercise as my goal is to go as fast as possible
eps = 0.01
# initial given valueg
initVal = -9.0



def newt(eps, initVal, root): 
    '''
    Assumes eps, InitVal, and root ints or floats
        eps > 0 
    Returns int totalGuesses such that each guess tries to find guess**root equal to initVal within eps by Newton-Raphson method        
        if fails to find a valid guess, it retuns 0
    '''
    initVal = float(initVal)
    guess = initVal/2.0 if initVal >= 0 else complex(initVal/2.0, initVal/2.0)
    TotalGuesses = 0
    while abs(abs(guess)**root- abs(initVal)) >= eps:
        TotalGuesses += 1
        guess = guess - (((guess**root) - initVal)/(root*guess**(root-1)))

    print (f'Total guesses (Newton-Raphson): {TotalGuesses}')
    print (f'The square root of {initVal} is about {guess}')
    return TotalGuesses

def bisec(eps, initVal, root):
    '''
    Assumes eps, InitVal, and root are ints or floats
        eps > 0 
    Returns int totalGuesses
    '''
    high = max(1.0, initVal) if initVal > 0 else min(-1.0, initVal)
    low = 0.0
    guess = (high + low)/2.0
    totalGuesses = 0


    # while the difference of initVal and cubed guess isn't eps or bigger 
    while abs(abs(guess)**root - abs(initVal)) >= eps:
    # portion_saved*    
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
    print (f'{guess} is close to sqrt of {initVal}')
    return totalGuesses


newt(eps, initVal, 2)
bisec(eps, initVal, 2)

print(f"Newton's method is {(bisec(eps, initVal, 2) / newt(eps, initVal, 2) )} times faster")