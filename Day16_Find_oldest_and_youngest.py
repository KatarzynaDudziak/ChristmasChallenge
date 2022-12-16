import datetime

class Child:
    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return (f'{self.name} {self.surname}, date of birth: {self.date_of_birth}')


def sort_by_date_of_birth(list_of_children):
    return sorted(list_of_children, key=lambda x: x.date_of_birth, reverse=True)


def main():
    list_of_children = [
        Child(
            'Jasiu',
            'Kowalski',
            datetime.date(2010, 12, 30)
        ),
        Child(
            'Kasia',
            'Nowak',
            datetime.date(2011, 11, 30)
        ),
        Child(
            'Asia',
            'Wisniewska',
            datetime.date(2010, 12, 31)
        ),
        Child(
            'Tomek',
            'Wojcik',
            datetime.date(2015, 6, 30)
        ),
        Child(
            'Tomek',
            'Zajac',
            datetime.date(2020, 12, 30)
        )
    ]
    children = sort_by_date_of_birth(list_of_children)
    print(f'The youngest child: {children[0]}\nThe oldest child: {children[len(list_of_children) - 1]}')

if __name__=='__main__':
    main()
