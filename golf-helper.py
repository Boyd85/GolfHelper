print ('Welcome to the Golf Club Helper')
print ('Tell me your situation, and Ill recommend a club')

onGreen = 20
green = input('Did you hit it on the green (y/n)?')
distance = int(input('How far is the ball from the hole?'))

while green != 'y' or 'n':
    print('An invalid input was entered. Please use y(yes) or n(no).')
    green = input('Did you hit it on the green (y/n)?')
    distance = int(input('How far is the ball from the hole?'))
    break

if (green is 'y'):
    if (distance > onGreen):
        print('Your distance is beyond the green')
    else:
        print('I recommend using your Putter.')
        
if(green is 'n'):
    if(distance < onGreen):
        print('You specified you are not on green but your yardage is on the green. Please Re-Evaluate.')
    elif(distance > 200):
        print('I recommend using your Driver.')
    elif(140 < distance < 200):
        print('I recommend using your 5 - Iron')
    elif(100 < distance < 140):
        print('I recommend using your 9 - Iron')
    else:
        print('I recommend using a Pitching wedge.')


    
