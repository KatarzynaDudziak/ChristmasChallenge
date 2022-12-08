
def make_star(lenght):
    board = []
    for _ in range(0, lenght): 
        board.append([' '] * lenght)         
    for i in range(0, lenght):
        board[7][i] = '*'
        board[i][7] = '*'
        if i > 2 and i < 12:
            board[i][i] = '*'
            board[i][lenght - 1 - i] = '*'
    return board


def main():
    lenght = 15
    board = make_star(lenght)
    for star in board:
        print(' '.join(star))


if __name__=='__main__':
    main()