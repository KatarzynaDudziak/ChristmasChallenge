from collections import Counter

class Recipe:
    def __init__(self, name, ingredients, description):
        self.name = name
        self.ingredients = ingredients
        self.description = description


def count_ingredients(recip_list):
    counter = Counter()

    for recipe in recip_list:
        counter.update(recipe.ingredients)

    shopping_list = dict(counter)
    return shopping_list


def main():
    recip_list = [
        Recipe(
            "Murzynek", {
                "Maka": 300,
                "Cukier": 100,
                "Jajka": 3,
                "Czekolada": 200,
                "Maslo": 200
            },
            "Piekarnik nagrzać do temp. 160 stopni [...],"),
        Recipe(
            "Piernik",{
                "Maka": 500,
                "Cukier": 180,
                "Miod": 250,
                "Jajka": 1,
                "Mleko": 80,
                "Maslo": 150
            },
            "Piekarnik nagrzać do temp. 180 stopni [...],"),
        Recipe(
            "Sernik", {
                "Maka": 100,
                "Cukier": 200,
                "Jajka": 6,
                "Ser": 1000,
                "Maslo": 200
            },
            "Piekarnik nagrzać do temp. 160 stopni [...]"),
        Recipe(
            "Uszka", {
                "Maka": 300,
                "Woda": 100,
                "Jajka": 1,
                "Sol": 1,
                "Maslo": 200,
                "Grzyby": 150,
                "Cebula": 1
            },
            "Zarobić ciasto z mąki, wody, soli i jajka [...]"),
        Recipe(
            "Barszcz", {
                "Buraki": 1000,
                "Bulion": 1500,
                "Zakwas": 200,
                "Sol": 1
            },
            "Buraki rozdrobnić i zagotować z bulionem [...]"),
        Recipe(
            "Pierogi", {
                "Maka": 300,
                "Woda": 100,
                "Jajka": 1,
                "Kapusta": 500,
                "Grzyby": 50,
                "Cebula": 1
            },
            "Zarobić ciasto z mąki, wody, soli i jajka [...]"),
        Recipe(
            "Karp",{
                "Karp": 1000,
                "Maka": 50,
                "Mleko": 500,
                "Sol": 1,
                "Olej": 500
            },
            "Rybę umyć i pokroić w dzwonki [...]")
    ]

    shopping_list = count_ingredients(recip_list)
    print(f'Shopping list: {shopping_list}')


if __name__=='__main__':
    main()
