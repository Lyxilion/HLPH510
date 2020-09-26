while 1:
    m = input("\n Quelle question ? (1-4)\n")
    if m == str(1):
        def ligne_car(n: int, ca: str):
            """
                Repete , fois le char ca
            :param n: nombre de repetition
            :param ca: le char
            :return: none
            """
            print(ca * n)
            return None

        ligne_car(3, "a")

    elif m == str(2):
        from math import pi


        def surf_cercle(r: float):
            """
                Donne le surface d'un cercle
            :param r: rayon du cercle
            :return: la surface
            """
            return pi * r ** 2

        print("la surface vaut", surf_cercle(2.5))

    elif m == str(3):
        def vol_boite(x1: float, x2: float, x3: float):
            """
                Donne le volume d'une boite
            :param x1: dimension 1
            :param x2: dimension 2
            :param x3: dimension 3
            :return:
            """
            return round(x1 * x2 * x3, 2)

        print(vol_boite(5.2, 7.7, 3.3))

    elif m == str(4):
        def index_max(tab: list):
            """
                Donne l'index du maximum d'une liste
            :param tab: une liste
            :return: l'index du maximum
            """
            maxi = tab[0]
            index = 0
            for i, e in enumerate(tab):
                if e >= maxi:
                    index = i
                    maxi = e
            return index

        serie = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3]
        index_max(serie)
        print("Résultat :", index_max(serie))

    else:
        print('end')
        break
