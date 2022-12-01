from math import sqrt


def count_distance_between_two_cities(city1, city2):
    distance = sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)
    return distance


def calculate_distance_between_cities(list_of_cities):
    distance_between_first_and_second = count_distance_between_two_cities(list_of_cities[0], list_of_cities[1])
    distance_between_second_and_third = count_distance_between_two_cities(list_of_cities[1], list_of_cities[2])

    distance = distance_between_first_and_second + distance_between_second_and_third
    return distance


def calculate_needed_fuel(distance):
    amount_of_fuel = (20 * distance) / 10
    return amount_of_fuel
    

def main():
    list_of_cities = [(1,1), (4,5), (11,5)]

    distance = calculate_distance_between_cities(list_of_cities)
    amount_of_fuel = calculate_needed_fuel(distance)
    print(f'Santa needs {amount_of_fuel} of fuel to cover the entire route.')


if __name__ == "__main__":
    main()
