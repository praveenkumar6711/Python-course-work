moves=30
while moves>1:
    status = input("[w] in or [C]ontinue: ").upper()
    if status == 'W':
        print("You won the match")
        break

    moves-=1
    print(f'{moves} moves are left')

else:
    print("Game over")
    
