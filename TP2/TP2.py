while 1 :
    n=input("\n Quelle question ? (1-4)\n")
    if n==str(1):
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

    elif n==str(2):
        from math import pi
        def surf_cercle(R: float):
            """
                Donne le surface d'un cercle
            :param R: rayon du cercle
            :return: la surface
            """
            return pi * R ** 2

        a = surf_cercle(2.5)
        print("la surface vaut", a)

    elif n==str(3):
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

    elif n==str(4):
        def index_max(L: list):
            """
                Donne l'index du maximum d'une liste
            :param L: une liste
            :return: l'index du maximum
            """
            max = 0
            for i, e in enumerate(L):
                if e >= max:
                    max = i
            return max

        serie = [5, 8, 2, 1, 9, 3, 6, 7, 9, 3]
        i = index_max(serie)
        print("Résultat :", i)

    else :
        print('end')
        break