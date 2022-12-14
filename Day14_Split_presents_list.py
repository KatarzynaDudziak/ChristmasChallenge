
def split_gifts(gifts):
    splitted_str = gifts.split(', ')[:-1]

    assigned_gifts = []
    for i in splitted_str:
        assigned_gifts.append(i.replace(' ', ', ').replace(',', ' =>', 1))
    return assigned_gifts


def split_gifts_one_line_solution(gifts):
     l = [i.replace(' ', ', ').replace(',', ' =>', 1) for i in gifts.split(', ')[:-1]]
     return l


def main():
    gifts = "Kuba klocki klawiatura dron quad, Alicja komputer samochod mysz, "\
            "Janina ksiazka traktor, Tomek kuchenka koparka flamastry, "

    for i in split_gifts(gifts):
        print(i)
    print(20 * '-')
    for i in split_gifts_one_line_solution(gifts):
        print(i)

if __name__=='__main__':
    main()
