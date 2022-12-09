
class Address:
    def __init__(self, street, number, flat_number, city, zip_code):
        self.street = street
        self.number = number
        self.flat_number = flat_number
        self.city = city
        self.zip_code = zip_code

    def count_vowels(self):
        return count(self.street + self.number + self.city)


def count(text):
    vowels = 'aeiouy'
    amount_of_vowels = 0

    for char in text.lower():
        if char in vowels:
            amount_of_vowels += 1
    return amount_of_vowels


def main():
    list_of_address = [
        Address(
            "Serniczkowa",
            "4B",
            2,
            "Krakow",
            "02-326"
        ),
        Address(
            "Pierniczkowa",
            "289A",
            55,
            "Gdansk",
            "02-326"
        ),
        Address(
            "Barszczykowa",
            "234",
            5,
            "Rzeszow",
            "37-326"
        ),
        Address(
            "Uszkowa",
            "43H",
            5,
            "Wroclaw",
            "02-326"
        ),
        Address(
            "Cukierkowa",
            "23I",
            5,
            "Poznan",
            "02-326"
        )
    ]
    count = 0
    for address in list_of_address:
        count += address.count_vowels() 
    print(f'Santa has to pay {count * 2} zl')

if __name__=='__main__':
    main()
