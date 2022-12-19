class Box:
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def calculate_needed_wrapping_paper(self):
        return round((2 * ((self.height * self.length) + (self.height * self.width)
                 + (self.length * self.width)))/100)


def main():
    dict_of_boxes = {
        'small' : Box(10, 13, 15),
        'medium' : Box(20, 15, 10),
        'big' : Box(30, 25, 20)
    }

    for name, box in dict_of_boxes.items():
        print(f'We need {box.calculate_needed_wrapping_paper()} m of paper to pack {name} box.')

if __name__=='__main__':
    main()
