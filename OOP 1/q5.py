# Question 5
''' In this question, we have to separate user input like positives, zeros and then negative numbers in sequence.
Numbers will be taken from user input until blank (enter key) not provided by user. After blank, user will be
displayed by sequence of positive numbers, zeros entered, negative numbers. Three lists are used to keep track 
of numbers as recommended in task instructions. While loop is given condition with True to iterate till blank is not 
given by user, if blank given break keyword is used to get out of loop. If number is greater than or equal to
1 then add in posiitve list, else if it is 0 then in list_zeros and else in negative numbers list. After that
all lists are printed by checking if their size is greater than 0 otherwise move on to next list to be
printed, end ="" is used to separate numbers with no space as already space is given in string after number
and it will keep our output on one line as well for certain list being printed.'''

'''Make lists to separate lists of positive, negative and zeros'''
list_zeros = []
list_positives = []
list_negatives = []

'''Use while loop to take input untill enter key pressed without input'''
while True:
    number = input('Enter an Integer (blank to quit): ')
    '''Break the loop if input is empty'''
    if number == '' or number == " ":
        break
    '''Convert number to integer'''
    number = int(number)
    '''Positive Number, Zeros then Negative'''
    if number>=1:
        '''Add it in positive numbers list'''
        list_positives.append(number)
    elif number==0:
        '''Add it in zeros numbers list'''
        list_zeros.append(number)
    else:
        '''Add it in negative numbers list'''
        list_negatives.append(number)

print('The numbers were: ')
'''If List size of positive numbers is 1 or greater than 1 than print its elements'''
if len(list_positives)>=1:
    for positive in list_positives:
        print(f"{positive} ",end="")
        
'''If List size of zeros list is 1 or greater than 1 than print its elements'''
if len(list_zeros)>=1:
    for zero in list_zeros:
        print(f"{zero} ",end="")
        
'''If List size of negative numbers is 1 or greater than 1 than print its elements'''
if len(list_negatives)>=1:
    for negative in list_negatives:
        print(f"{negative} ",end="")