NAMES = 'Input/Names/invited_names.txt'
LETTER = 'Input/Letters/starting_letter.txt'

OUTPUT_LETTER = 'Output/ReadyToSend/letter_for_'

name_list = []
with open(NAMES) as Names:
    names = Names.read()
    name_list = names.split('\n')
    print(name_list)

with open(LETTER) as Letter: 
    for name in name_list:
        with open(OUTPUT_LETTER + name + '.txt', mode='w'):
            base = Letter.read()
            print(base) 