nums = []
 
for i in range(10):
    # asks for input and ads to nums list
    # nums.append(i + 1) 
    while True:
        try:
            currentNum = int(input(str(i + 1) + '- enter any number:'))
            nums.append(currentNum)
        except ValueError:
            print('Please enter a valid whole number')    
            continue
        else:
            break
    

# checks all numbers
print('Numbers entered: ' + str(nums))
largestOdd = 0

# interates over nums checking for the largest odd number
for num in range(len(nums)):
    # check for odd numbers and atribute to var if True
    if nums[num] % 2 != 0 and largestOdd <= nums[num]:
        largestOdd = nums[num]   
    #  
    if nums[num] == nums[-1] and largestOdd == 0: 
        print ('No odd numbers found. Please restart operation')
        
print('Largest Odd Number: ' + str(largestOdd))
