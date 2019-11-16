from encrypt import encryption, decryption


def main():
    operation = input(("Wybierz operacje (szyfrowanie, "
                       "deszyfrowanie, wyjscie): ")).lower()
    if operation == "wyjscie":
        exit()
    else:
        if operation == "szyfrowanie":
            user_text = input("Podaj tekst: ").lower()
            print("Wynik:", encryption(user_text))
        elif operation == "deszyfrowanie":
            user_text = input("Podaj tekst: ").lower()
            print("Wynik:", decryption(user_text))
        else:
            print("Bledna operacja!")
    main()


main()
