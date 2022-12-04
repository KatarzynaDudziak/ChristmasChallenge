
     # Mikołaj postanowił w tym roku skorzytać z pomocy nowoczesnych technologii
     # i zamiast rozwozić wszystkie prezenty, niektóre przesłać przez Internet.
     # Do tego celu musi zamienić nazwy prezentów w strumienie bitów!
     # Pomoż Mikołajowi! Przygotuj kod, który zamieni nazwy prezentów na ciąg zer i jedynek.
     # Dla każdej litery nazwy prezentu znajdz kod UTF-8, a później zamień go na system binarny.
     # Dla każdego prezentu wypisz na ekran ciąg zer i jedynek. Każdy prezent w oddzielnej linijce.
     # Możesz napisać funkcję zamieniającą numer znaku na system binarny samodzielnie,
     # albo znaleźć odpowiednią funkcję w bibliotece Twojego języka.


def print_as_binary(gifts):
    for gift in gifts:
        print(f'{gift} = {convert_gift_to_binary(gift)}')


def convert_gift_to_binary(gift):
    binary_list = []
    for char in gift:
        binary_list.append(bin(ord(char))[2: ])
    return binary_list


def main():
    gifts = ["Parfum", "Socks", "Sweather", "Cup",
        "Hat", "Tea", "Coffee", "Clock", "Bag",
        "Book", "Wallet", "Cream", "Earrings"]

    print_as_binary(gifts)

if __name__=='__main__':
    main()
