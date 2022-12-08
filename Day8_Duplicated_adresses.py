
class Address:
    def __init__(self, street, number, flat_number, city, zip_code):
        self.street = street
        self.number = number
        self.flat_number = flat_number
        self.city = city
        self.zip_code = zip_code
    
    def __repr__(self):
        return (f'[Street: {self.street}, '
            f'Number: {self.number}, '
            f'Flat number: {self.flat_number}, '
            f'City: {self.city}, '
            f'Zip code: {self.zip_code}]')

    def __eq__(self, other):
        return isinstance(other, Address) \
            and self.street == other.street \
            and self.number == other.number \
            and self.flat_number == other.flat_number \
            and self.city == other.city \
            and self.zip_code == other.zip_code

    def __hash__(self):
        return hash((self.street, self.number, self.flat_number, self.city, self.zip_code))


def skip_repeated_addresses_using_for_loop(list_of_address):
    new_list = []
    for address in list_of_address:
        if address not in new_list:
            new_list.append(address)
    return new_list


def skip_repeated_addresses_using_set(list_of_address):
    return list(set(list_of_address))


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
            "289",
            55,
            "Gdansk",
            "02-326"
        ),
        Address(
            "Pierniczkowa",
            "289",
            55,
            "Gdansk",
            "02-326"
        ),
        Address(
            "Pierniczkowa",
            "289",
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
            "Uszkowa",
            "43H",
            5,
            "Wroclaw",
            "02-326"
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
            "23",
            5,
            "Poznan",
            "02-326"
        )
    ]
    l1 = skip_repeated_addresses_using_for_loop(list_of_address)
    l2 = skip_repeated_addresses_using_set(list_of_address)
    print('Solution with loop')
    for address in l1:
        print(address)
    print('\nSolution with set')
    for address in l2:
        print(address)

if __name__=='__main__':
    main()