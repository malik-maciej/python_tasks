from mlist import MLista
from utils import operations, set_capacity


def main():
    capacity = set_capacity()
    if capacity == 0:
        print("Zly rozmiar listy")
        main()
    my_list = MLista(capacity)
    operations(my_list)


main()
