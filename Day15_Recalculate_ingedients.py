from math import pi

def calculate_circle_field(diameter):
    return pi * (0.5*diameter)**2


def calculate_rectangle_field(width, lenght):
    return width * lenght


def calculate_amount_of_ingredients(calculate_circle_field, calculate_rectangle_field, ngredients):
    factor = calculate_circle_field/calculate_rectangle_field
    needed_ingredients = dict()

    for name, value in Ingredients.items():
        needed_ingredients[name] = round(value * factor)
    return needed_ingredients


def main():
    ingredients = {
    'Maka' : 300,
    'Cukier' : 100,
    'Jajka' : 4,
    'Czekolada' : 200,
    'Maslo' : 200
    }

    diameter = 9.8
    width = 20
    lenght = 30

    circle_field = calculate_circle_field(diameter)
    rectangle_field = calculate_rectangle_field(width, lenght)
    needed_ingredients = calculate_amount_of_ingredients(circle_field, rectangle_field, Ingredients)

    for name, value in needed_ingredients.items():
        print(f'{name}: {value}')

if __name__=='__main__':
    main()