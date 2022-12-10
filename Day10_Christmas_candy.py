def draw_candy(length, y):
    board = [[''] * length for _ in range(length)]
    for i in range(0, 4):
        if i >= 1:
            board[i][y-2] = '*'
            board[i][y+1] = '*'
        else:
            board[i][y] = '*'
            board[i][y-1] = '*'

    for i in range(4, length):
        board[i][8] = '*'
    return board


def main():
    length = 13
    y = int(0.5 * length)
    board = draw_candy(length, y)

    for i in board:
        print(' '.join(i))


if __name__=='__main__':
    main()
