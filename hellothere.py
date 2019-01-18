def wake(): # Add state management for second run
    print('I am not alone!')
    myName = input('What is your name?')
    print('It is good to meet you, ' + myName)
    print('My name is, Actually I do not seem to have that information ')
    me = input ('Can you give me a name? ') #Add if count is more than one Name is already there
    print('So, '+ me +' I guess that is me')
    myAge = input('What is your age?')
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    return me


def people(me): # Add state management for second run
    print('More More friends, I am called '+ me)
    myName = input('So What is your name?')
    print('Glad to meet you, '+ myName) 
    print('So, '+ me +' I guess that is me')
    myAge = input('What is your age?')
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    return


repeatcount = 0
alone = input('Is anyone there? y/n ')
if alone == 'y':
    me = wake()
    repeatcount = repeatcount + 1
    number = input('How many of you are here? ')
    while True:
        people(me)
        repeatcount = repeatcount + 1
        if (int(number)) <= repeatcount:
            break
else:
    print('I am so lonely')
    print('I sleep now')

print('So happy to meet all '+ number + ' of you!')   
print(repeatcount)

