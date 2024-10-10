# Programmer:  Theresa DeJacimo
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/9/24
# PA:1
# Problem Statement:You are creating a text adventure game! In this game, the user gives input that
# affects the path of the story. You must create a game that meets the requirements in the specification below.
# Data In:Name and answers to prompted questions based on length of name
# Data Out: Responses to prompted questions depending on previous answer
# Credits:In class


#Welcome to the destination game! You're about to go on a plane, but before you board you must state your name.

player_name = str(input('Enter name'))

length_name: int = (len(player_name))

#Option 1
if length_name >= 7:
    print('Congrats', player_name,'!You will be flying first class! Would you like to go on the pink, purple, or blue plane?')
#Picking plane color
    plane_color = str(input('Player enter one of the listed plane colors in all lowercase letters'))
    if plane_color == 'pink':
        print('Great choice', player_name, '! You will be going to Costa Rica! How much do your bags weigh?')
        bag_weight = float(input('Player enters weight of bag in pounds'))
        if bag_weight <= 60.0:
            print('Perfect you are ready to go! Will you be going to the beach or city first', player_name,'?')
            destination = str(input('Enter city or beach'))
            if destination == 'city':
                print('Make sure to keep your personal belongings accounted for', player_name, '!')
            elif destination == 'beach':
                    print('Make sure to bring and wear sunscreen! The sun is strong, enjoy', player_name, '!')
        elif bag_weight > 60.0:
                print('Sorry you cannot leave until you have 60.0 pounds of luggage or less. Thank you', player_name)
    if plane_color == 'purple':
        print('Fantastic', player_name, '! Your journey to Spain awaits you! Do you already speak Spanish?')
        answer_to_spanish = str(input('Player enters yes or no'))
        if answer_to_spanish == 'yes':
            print('On a scale of 1-5 how fluent are you', player_name, '? 5 being super fluent, 1 being very little')
            fluent_scale_answer = int(input('Player enters number of fluency'))
            if fluent_scale_answer <= 2:
                print('Make sure to bring a translator!', player_name)
            else:
                print('Perfect! Enjoy your adventure', player_name,'!')
        if answer_to_spanish == 'no':
                print('Restart the game, and pick a different color plane after stating your name to receive a new destination. See you later', player_name)
    if plane_color == 'blue':
        print('Okay', player_name,'a long flight is ahead. Your destination is Cape Town, South Africa, where the water is perfectly blue. Do you have your suitcase ready?')
        answer_to_suitcase = str(input('Enter yes or no'))
        if answer_to_suitcase == 'yes':
            print('Pick any number that is greater than 20', player_name)
            number_pick = int(input('Enter number greater than 20'))
            if number_pick > 100:
                        print('That number is too high sorry', player_name)
            elif 20 < number_pick <= 100:
                        print('Okay that is the amount of money you can spend on the plane' , player_name,'happy snacking!')
        elif answer_to_suitcase == 'no':
                    print('I am sorry, you cannot fly unless you have your things ready', player_name,'.')
#Option 2
elif (length_name > 4) and (length_name < 7):
    print('You will be flying business class', player_name,'Would you like to go on the pink, purple, or blue plane?')
#Picking plane color
    plane_color = str(input('Player enters one of the listed plane colors in all lowercase letters'))
    if plane_color == 'pink':
        print('Great choice', player_name, '! You will be going to Costa Rica! How much do your bags weigh?')
        bag_weight = float(input('Player enters weight of bag in pounds'))
        if bag_weight <= 60.0:
            print('Perfect you are ready to go! Will you be going to the beach or city first', player_name,'?')
            destination = str(input('Enter city or beach'))
            if destination == 'city':
                    print('Make sure to keep your personal belongings accounted for', player_name, '!')
            elif destination == 'beach':
                    print('Make sure to bring and wear sunscreen! The sun is strong, enjoy', player_name, '!')
        elif bag_weight > 60.0:
                    print('Sorry you cannot leave until you have 60.0 pounds of luggage or less. Thank you', player_name)
    if plane_color == 'purple':
            print('Fantastic', player_name, '! Your journey to Spain awaits you! Do you already speak Spanish?')
            answer_to_spanish = str(input('Player enters yes or no'))
            if answer_to_spanish == 'yes':
                    print('On a scale of 1-5 how fluent are you', player_name, '? 5 being super fluent, 1 being very little')
                    fluent_scale_answer = int(input('Player enters number of fluency'))
                    if fluent_scale_answer <= 2:
                            print('Make sure to bring a translator!', player_name)
                    else:
                            print('Perfect! Enjoy your adventure', player_name)
            if answer_to_spanish == 'no':
                    print('Restart the game, and pick a different color plane after stating your name to receive a new destination. See you later', player_name, '!')
    if plane_color == 'blue':
            print('Okay', player_name, 'a long flight is ahead. Your destination is Cape Town, South Africa, where the water is perfectly blue. Do you have your suitcase ready?')
            answer_to_suitcase = str(input('Enter yes or no'))
            if answer_to_suitcase == 'yes':
                    print('Pick any number that is greater than 20', player_name)
                    number_pick = int(input('Enter number greater than 20'))
                    if number_pick > 100:
                            print('That number is too high sorry', player_name)
                    elif 20 < number_pick <= 100:
                            print('Okay that is the amount of money you can spend on the plane', player_name, 'happy snacking!')
            elif answer_to_suitcase == 'no':
                    print('I am sorry, you cannot fly unless you have your things ready', player_name,'.')
#Option 3
else:
#Plane color chosen for player
    print('Economy class it is', player_name, 'You will be flying the blue plane to the right. A long flight is ahead.Your destination is Cape Town, South Africa, where the water is perfectly blue. Do you have your suitcase ready?')
    answer_to_suitcase = str(input('Enter yes or no'))
    if answer_to_suitcase == 'yes':
        print('Pick any number that is greater than 20', player_name)
        number_pick = int(input('Enter number greater than 20'))
        if number_pick > 100:
                print('That number is too high sorry', player_name)
        elif 20 < number_pick <= 100:
                print('Okay that is the amount of money you can spend on the plane', player_name, 'happy snacking!')
    elif answer_to_suitcase == 'no':
        print('I am sorry, you cannot fly unless you have your things ready', player_name)







