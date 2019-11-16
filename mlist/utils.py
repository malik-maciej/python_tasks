def operations(my_list):
    operation = input(("Wybierz polecenie (pisz, dodaj_element, znajdz, "
                       "pobierz, rozmiar, pojemnosc, usun_powtorzenia, "
                       "odwroc, zwieksz_pojemnosc, zmniejsz_pojemnosc, "
                       "wyjscie): ")).lower()
    if operation == "wyjscie":
        exit()
    else:
        if operation == "pisz":
            my_list.write()
        elif operation == "rozmiar":
            print("Rozmiar listy: ", my_list.get_length())
        elif operation == "pojemnosc":
            print("Pojemnosc listy: ", my_list.get_capacity())
        elif operation == "odwroc":
            my_list.reverse()
        else:
            operations_with_user_value(operation, my_list)
    operations(my_list)


def operations_with_user_value(operation, my_list):
    try:
        if operation == "dodaj_element":
            if not my_list.add_element(set_value()):
                print("Wystapil blad! Lista jest pelna!")
        elif operation == "usun_powtorzenia":
            my_list.remove_duplicates(set_value())
        elif operation == "znajdz":
            result = my_list.get_index(set_value())
            if result == -1:
                print("Nie ma takiego elementu!")
            else:
                print("Index: ", result)
        elif operation == "pobierz":
            result = my_list.get_element(set_value())
            if result == -1:
                print("Podano zly index!")
            else:
                print("Wartosc: ", result)
        elif operation == "zwieksz_pojemnosc":
            if not my_list.increase_capacity(set_value()):
                print("Wystapil blad! Podaj dodatnia liczbe!")
        elif operation == "zmniejsz_pojemnosc":
            if not my_list.reduce_capacity(set_value()):
                print("Wystapil blad! Zla wartosc!")
        else:
            print("Bledna operacja!")
    except ValueError:
        print("Zla wartosc!")


def set_value():
    return int(input("Podaj wartosc: "))


def set_capacity():
    try:
        capacity = int(input("Podaj poczatkowy rozmiar listy: "))
        if capacity < 1:
            return 0
        return capacity
    except ValueError:
        return 0
