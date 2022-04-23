'''
Description: Assignment number 1 course CSE 210, Programming with Classes. 
             This is a program that allows to play the classic tictactoe game.

Date:   April 21, 2022.
Author: Carlos Garcia Vera.
'''

## 1.- Functions

# 1.1.- Main
def main():
    boxes = [1,2,3,4,5,6,7,8,9]
    show_game(boxes)
    symbol = input('Who first, x or o? ')
    win  = False
    draw = False
    while not win and not draw:
        boxes = get_move(symbol,boxes)
        show_game(boxes)
        win,who = exist_winner(boxes)
        draw    = exist_draw(boxes)
        if symbol=='x':
            symbol='o'
        else:
            symbol='x'
    if draw:
        print('It was a draw, there are no winners or losers.')
    else:
        print(f'The player with {who} is the winner.')


# 1.2- Create image
def show_game(boxes):
    print('')
    print('+-+-+-+')
    print(f'|{boxes[0]}|{boxes[1]}|{boxes[2]}|')
    print('+-+-+-+')
    print(f'|{boxes[3]}|{boxes[4]}|{boxes[5]}|')
    print('+-+-+-+')
    print(f'|{boxes[6]}|{boxes[7]}|{boxes[8]}|')
    print('+-+-+-+')
    print('')

# 1.3.- To register a move
def get_move(symbol,boxes):
    position = int(input(f"Player with {symbol} has to choose a square (1 to 9): "))
    boxes[position - 1] = symbol
    return boxes

# 1.4.- Determines if there is a winner
def exist_winner(boxes):
    if  boxes[0] == boxes[1] == boxes[2]=='x' or boxes[3] == boxes[4] == boxes[5]=='x' or boxes[6] == boxes[7] == boxes[8]=='x' or boxes[0] == boxes[3] == boxes[6]=='x' or boxes[1] == boxes[4] == boxes[7]=='x' or boxes[2] == boxes[5] == boxes[8]=='x' or boxes[0] == boxes[4] == boxes[8]=='x' or boxes[2] == boxes[4] == boxes[6]=='x':
        who = 'x'
        status=True
    elif  boxes[0] == boxes[1] == boxes[2]=='o' or boxes[3] == boxes[4] == boxes[5]=='o' or boxes[6] == boxes[7] == boxes[8]=='o' or boxes[0] == boxes[3] == boxes[6]=='o' or boxes[1] == boxes[4] == boxes[7]=='o' or boxes[2] == boxes[5] == boxes[8]=='o' or boxes[0] == boxes[4] == boxes[8]=='o' or boxes[2] == boxes[4] == boxes[6]=='o':
        who = 'o'
        status=True
    else:
        status=False
        who = 'nobody'
    return status,who

# 1.5.- Determines if there is a draw using sets in python
def exist_draw(boxes):
    boxes_set = set(boxes)
    ref_set   = {1,2,3,4,5,6,7,8,9}
    return ref_set.isdisjoint(boxes_set)

## 2.- Program

if __name__ == "__main__":
    main()