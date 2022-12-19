class Box:
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def __repr__(self):
        return(f'{self.height}, {self.length}, {self.width}')

    def calculate_needed_wrapping_paper_for_one_box(self):
        return (2 * ((self.height * self.length) + (self.height * self.width)
                 + (self.length * self.width))/10000)


def main():
    small = Box(10, 13, 15),
    medium = Box(20, 15, 10),
    big = Box(30, 25, 20)

    dict_of_boxes = {
        5 : Box(10, 13, 15),
        10 : Box(20, 15, 10),
        3 : Box(30, 25, 20)
    }

    sum_of_needed_wrapping_paper = 0

    for number_of_boxes, box in dict_of_boxes.items():
        sum_of_needed_wrapping_paper += (box.calculate_needed_wrapping_paper_for_one_box()) * number_of_boxes
    print(f'We need {round(sum_of_needed_wrapping_paper)}m2 of paper to pack all the boxes.')

if __name__=='__main__':
    main()
