while True:
    try: 
        numXs = int(input('How many Xs? : '))
        toPrint = ''
        while len(toPrint) < numXs:
            toPrint += 'X'
    except ValueError: print('enter a valid number : ')
    else: break
print(toPrint)