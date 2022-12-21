
def main():
    places = 10
    reindeers = 100

    print(f'Before switch: places = {places}')
    print(f'Before switch: reindeers = {reindeers}')

    places, reindeers = reindeers, places

    print(f'After switch: places = {places}')
    print(f'After switch: reindeers = {reindeers}')

if __name__=='__main__':
    main()
