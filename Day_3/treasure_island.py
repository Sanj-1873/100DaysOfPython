print('Welcome to Treasure Island.\nYour mission is to find the treaasure.\n')
question_1 = input('Left or Right?')
question_1 = question_1.upper()
if(question_1 != 'LEFT' ):
    print('\nFall into a hole.\nGame Over.')
else:
    question_2 = input('Swim or Wait?\n')
    question_2 = question_2.upper()
    if(question_2 != 'WAIT'):
        print('\nAttacked by trout.\nGame Over.\n')
    else:
        question_3 = input('\nWhich door? (Red, Blue, or Yellow)\n')
        question_3 = question_3.upper()
        if(question_3 == 'BLUE'):
            print('\nEaten by beasts.\nGame Over.')
        elif(question_3 == 'RED'):
            print('\nBurned by fire.\nGame Over.')
        elif(question_3 == 'YELLOW'):
            print('\nYou Win!\n')
        else:
            print('Game Over.')