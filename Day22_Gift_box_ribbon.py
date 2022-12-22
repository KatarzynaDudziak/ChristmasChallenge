import math

class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_ribbon_amount_with_supply(self):
        first_side = 2 * self.length + 2 * self.width
        second_side = 2 * self.length + 2 * self.height
        first_side_with_supply = first_side + first_side * 1/2
        second_side_with_supply = second_side + second_side * 1/2
        return first_side_with_supply + second_side_with_supply


def main():
    box = Box(10, 13, 15)
    boxes_amount = 5

    ribbon_ammount = box.calculate_ribbon_amount_with_supply()
    needed_ribbon_in_meter = math.ceil((boxes_amount * (ribbon_ammount/100)))

    print(f'Santa needs {needed_ribbon_in_meter}m of ribbon.')


if __name__=='__main__':
    main()
