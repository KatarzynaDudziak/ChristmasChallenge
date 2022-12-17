
def draw_christmas_ball(length, radius, a, b):
    board = [[' '] * length for _ in range(length)]

    for x in range(length):
        for y in range(length):
            if ((x - a)**2 + (y - b)**2 - radius**2 <= 5):
                board[x][y] = '\033[94m' + 'B'
            else:
                board[x][y] = '\033[92m' + '.'

    board[a - (radius + 1)][b] = '\033[93m' + 'O'
    return board

def main():
    radius = 8
    a = 12
    b = 11
    length = 25
    christmas_ball = draw_christmas_ball(length, radius, a, b)

    for i in christmas_ball:
        print(' '.join(i))

if __name__=='__main__':
    main()
