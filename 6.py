class Tovar:
    def __init__(self, nazvanie, magazin, tsena):
        self.__nazvanie = nazvanie
        self.__magazin = magazin
        self.__tsena = tsena
    def get_nazvanie(self):
        return self.__nazvanie
    def get_magazin(self):
        return self.__magazin
    def get_tsena(self):
        return self.__tsena

class Sklad:
    def __init__(self, tovary):
        self.__tovary = tovary
    def __getitem__(self, index):
        return self.__tovary[index].__dict__
    def sort_by_magazin(self):
        return [t.__dict__ for t in sorted(self.__tovary, key=lambda tov: tov.get_magazin())]
    def sort_by_naimenovanie(self):
        return [t.__dict__ for t in sorted(self.__tovary, key=lambda tov: tov.get_nazvanie())]
    def sort_by_tsena(self):
        return [t.__dict__ for t in sorted(self.__tovary, key=lambda tov: tov.get_tsena())]

tovar1 = Tovar('Яблоко', 'Маг1', 50)
tovar2 = Tovar('Молоко', 'Маг3', 180)
tovar3 = Tovar('Хлеб', 'Маг2', 200)
tovary = [tovar1, tovar2, tovar3]
sklad1 = Sklad(tovary)
print(f'Индекс 0: {sklad1[0]}')
print(f'\nСортировка по названию магазина: {sklad1.sort_by_magazin()}')
print(f'\nСортировка по наименованию товара: {sklad1.sort_by_naimenovanie()}')
print(f'\nСортировка по цене: {sklad1.sort_by_tsena()}')