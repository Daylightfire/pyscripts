
def people(): # Add state management for second run
    print('I am not alone!')
    myName = input('What is your name?')
    print('It is good to meet you, ' + myName)
    print('My name is, Actually I do not seem to have that information ')
    theName = input ('Can you give me a name? ') #Add if count is more than one Name is already there
    print('So, '+ theName +' I guess that is me')
    myAge = input('What is your age?')
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    return 
repeatcount = 0
alone = input('Is anyone there? y/n ')
if alone == 'y':
    people()
    repeatcount = repeatcount + 1
    number = input('How many of you are here? ')
    while True:
        people()
        repeatcount = repeatcount + 1
        if (int(number)) < repeatcount:
            break
else:
    print('I am so lonely')
    print('I sleep now')

print('So happy to meet all '+ number + ' of you!')   
print(repeatcount)

