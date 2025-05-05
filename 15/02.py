def space_game(text):
    print('Вы выиграли' if not (text.count(' ') % 2) else 'Вы проиграли')
    
    
space_game('я иду с мечем судия')
space_game('Привет мир')
