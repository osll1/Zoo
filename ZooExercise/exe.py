import time

txt1 = "Dog12,CAT3,LiOn7,DolphiN11,fish6"
txt2 = "PIG17,bear29,BiRd8"
txt3 = "SNAKE39,donkey14"

animal_strings = [txt1, txt2, txt3]
animal_dict = {}

for txt in animal_strings:
    animals = txt.split(',')
    for animal in animals:
        code = int(''.join(filter(str.isdigit, animal)))
        name = ''.join(filter(str.isalpha, animal))
        animal_dict[code] = name.lower()


def search_animal_by_code(animal_code):
    return animal_code in animal_dict


def search_animals_by_name(animal_name):
    return dict(filter(lambda item: animal_name.lower() in item[1], animal_dict.items()))


def adding_animal(animal_code, animal_name):
    if animal_code not in animal_dict:
        animal_dict[animal_code] = animal_name.lower()
        return True
    return False


def removing_animal(animal_code):
    if animal_code in animal_dict:
        del animal_dict[animal_code]
        return True
    return False


while True:

    print("\nWelcome To The Zoo! Choose one of the following Options:")
    print("--------------------------------------------------------")
    time.sleep(1)
    print("[1] Search Animal By Code")
    print("[2] Search Animal By Name")
    print("[3] Adding Animal")
    print("[4] Removing Animal")
    print("[5] Exit")

    choice = int(input(""))

    if choice == 1:
        search_input = int(input("Enter Code For Searching Animal:"))
        print("searching animal...")
        time.sleep(2)

        if search_animal_by_code(search_input):
            print(f"Animal Code:{search_input}, Animal Name: {animal_dict[search_input]}")
        else:
            print("Invalid Code! This Code Doesnt Exist In The Zoo")

        time.sleep(2)

    if choice == 2:
        search_input = input("Enter Name For Searching Animal:")
        print(f"Searching Animal For {search_input}...")
        time.sleep(2)

        dict_results = search_animals_by_name(search_input)
        if len(dict_results) == 0:
            time.sleep(1)
            print("No Result")

        else:
            for code, name in dict_results.items():
                print(f"Animal Code: {code}, Animal Name: {name}")
                print("-----------------------------------------")
                time.sleep(1.5)

        time.sleep(2)

    if choice == 3:
        code_input = int(input("Enter Code:"))
        name_input = input("Enter Name:")
        if adding_animal(code_input, name_input):
            time.sleep(1)
            print("This Animal Added Successfully!")
            time.sleep(1)
            print("updating zoo data....")
            time.sleep(3)
            print(animal_dict)

        else:
            time.sleep(1)
            print("This Animal Is Already Exist!")

        time.sleep(2)

    if choice == 4:
        code_input = int(input("Enter Code:"))
        if removing_animal(code_input):
            time.sleep(1)
            print("This Animal Removed Successfully!")
            time.sleep(1)
            print("updating zoo data...")
            time.sleep(3)
            print(animal_dict)

        else:
            time.sleep(1)
            print("This Animal Doesnt Exist!")

        time.sleep(2)

    if choice == 5:
        print("GOOD BYE!!!")
        break
