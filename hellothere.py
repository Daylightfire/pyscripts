def people(repeatcount):
    print('I am not alone!')
    myName = input('What is your name?')
    print('It is good to meet you, ' + myName)
    print('My name is, Actually I do not seem to have that information ')
    theName = input ('Can you give me a name? ') #Add if count is more than one Name is already there
    print('So, '+ theName +' I guess that is me')
    myAge = input('What is your age?')
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    repeatcount = repeatcount + 1
    return repeatcount
repeatcount = 0
alone = input('Is anyone there? y/n ')
if alone == 'y':
    people(repeatcount)
    number = input('How many of you are here? ')
else:
    print('I am so lonely')
    print('I sleep now')

print('So there are ' + number + ' of you here')
print(repeatcount)
