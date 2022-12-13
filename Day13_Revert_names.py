def reverse_name(list_of_names):
    name_reversed_list = []
    for name in list_of_names:
        name_reversed_list.append(name[::-1].lower().capitalize())
    return name_reversed_list

def main():
    list_of_names = ["Uisaj", "Aisak", "Aisa", "Kemot", "Lahcim"]
    
    for name in reverse_name(list_of_names):
        print(name)

if __name__=='__main__':
    main()