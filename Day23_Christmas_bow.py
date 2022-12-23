def draw_bow(length):
    board = [['   '] * length for _ in range(length)]
    
    for i in range(length):
        board[i][0] = '\033[94m' + ' * '
        board[i][length - 1] = ' * ' + '\033[94m'
    for i in range(length):
        board[i][i] = ' * ' + '\033[94m'
        board[i][length - 1 - i] = ' * ' + '\033[94m'
    return board

def main():
    length = 15
    board = draw_bow(length)
    for i in board:
        print(''.join(i))

if __name__=='__main__':
    main()
