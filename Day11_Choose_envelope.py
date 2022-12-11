import itertools

class Envelope:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return (f'Envelope of width {self.width} and height {self.height}.')

   
class Gift:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
    
    def __repr__(self):
        return (f'{self.name}')

    def __hash__(self):
        return hash((self.name, self.width, self.height))


def match_gift_with_envelope(list_of_gifts, list_of_envelopes):
    list_of_pairs = itertools.product(list_of_gifts, list_of_envelopes)
    fitting_pairs = dict()

    for pair in list_of_pairs:
        gift = pair[0]
        envelope = pair[1]
        if gift in fitting_pairs:
            continue
        if fits_in(gift, envelope):
            fitting_pairs[gift] = envelope
    return fitting_pairs


def fits_in(gift, envelope):
    if (gift.width <= envelope.width and gift.height <= envelope.height
     or gift.height <= envelope.width and gift.width <= envelope.height):
        return True


def main():
    list_of_gifts = [
        Gift('Parfume', 12, 30),
        Gift('Socks', 10, 10),
        Gift('Book', 30, 25),
        Gift('Clock', 15, 15),
        Gift('Wallet', 5, 10)
    ]

    envelope_small = Envelope(10, 15)
    envelope_medium = Envelope(20, 30)
    envelope_big = Envelope(30, 30)
    
    list_of_envelopes = [envelope_small, envelope_medium, envelope_big]

    fitting_pairs = match_gift_with_envelope(list_of_gifts, list_of_envelopes) 
    for gift, envelope in fitting_pairs.items():
        print(f'The {gift} fits with {envelope}') 


if __name__=='__main__':
    main()
