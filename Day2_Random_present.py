from random import sample

     # Mikołaj postanowił w tym roku skorzystać z pomocy nowoczesnych technologii.
     # Zamiast zastanawiać się, komu jaki prezent dostarczyć postanowił skorzystać z programu.
     # Pomoż Mikołajowi!
     # Przygotuj kod, który z listy dostępnych prezentów wylosuje 3 prezenty i wypisze na ekranie.
     # Odpal program kilka razy - sprawdź, czy na pewno losuje za kazdym razem inne prezenty!
     # Wylosowane prezenty wypisz na ekranie. Zadbaj o to, żeby wylosowane prezenty były unikalne.


def draw_gifts(gifts, amount_of_elements, chosen_range):
    return [sample(gifts, k=amount_of_elements) for _ in range(chosen_range)]


def main():
    gifts = ["Perfume", "Socks", "Sweater", "Cup",
            "Hat", "Tea", "Coffee", "Clock", "Bag",
            "Book", "Wallet", "Cream", "Earrings"]

    drawn_gifts = draw_gifts(gifts, 3, 5)
    print(drawn_gifts)


if __name__=='__main__':
    main()
    