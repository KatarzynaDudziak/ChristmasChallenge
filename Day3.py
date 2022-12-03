from random import choice


def draw_christmas_tree(height):
    empty_places = height - 1
    amount_of_stars = 1
    for _ in range(height):
        print((empty_places * ' ') + choose_sign(amount_of_stars))
        empty_places -= 1
        amount_of_stars += 2


def choose_sign(amount_of_stars):
    signs = ['*', 'O', '#', '@']
    s = ''
    for sign in range(0, amount_of_stars):
        s += choice(signs)
    return(s)


def main():
    draw_christmas_tree(20)
    

if __name__=='__main__':
    main()
