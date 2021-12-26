name = input('Enter your name: ')

print('Welcome', name,'to this adventure!')

answer = input('You are on a muddy road, it has come to an end , so which way you would like to go left, right or go back? ').lower()

if answer == 'left':
    
    answer = input('you come to a river, you can walk around the river or you swim across the river ,what you want to do? ').lower()
    
    if answer == 'swim':
        print('You swam across and you will be eaten by alligator as there were large number of alligator waiting for someone, and you lose.')

    
    elif answer == 'walk':
        print('I appreciate your effort to go around, but you ran out of energy and water as river is very long , and you lose.')


    else:
        print('not a valid direction to choose, so choose wisely.')

    

elif answer == 'right':
    
    answer = input('You come to a bridge, but it looks stagering, so do you want to cross it or head back? (cross/back)').lower()

    if answer == 'back':
        print('OOPS ! , sorry you are not adventures and you lose.')

    elif answer == 'cross':
        
        answer = input('you cross the bridge and meet with two strangers, Do you want to talk or not? (yes/no) ').lower()
        
        if answer =='no':
            print('you ignore the strangers , you does not have any idea about your destination , so you lose')
        
        elif answer =='yes':
            answer = input('there are two strangers one having long beard and others having only moustache, so which one you choose? (beard/moustache)').lower()

            if answer =='beard':
                print('sorry, you choose a wrong person, he is terrorist and he kill you and at last you lose ')


            elif answer =='moustache':
                print('congratulation ! , you choose a right person finally you won this game.')

            else:
                print('not a valid direction to choose, so choose wisely.')


        else:
            print('not a valid direction to choose, so choose wisely.')



    else:
        print('not a valid direction to choose, so choose wisely.')

         
elif answer == 'back':
    print('OOPS ! , sorry you are not adventures and you lose.')

else:
    print('not a valid direction to choose, so choose wisely.')

print('thank you for trying',name)