while 1 :
    n=input("\n Quelle question ? (1-8)\n")
    if n==str(1):
        print("1. 20 premiers termes de la table de multiplication par 7.")
        for i in range(20):
            print('7x' + str(i) + '=' + str(i * 7))

    elif n==str(2):
        print("table de conversion de sommes d'argent :")
        for i in range(15):
            print(str(2 ** i) + ' euro(s) = ' + str(1.65 * 2 ** i) + ' dollar(s)')

    elif n==str(3):
        print("2. Suite de 12 nombres dont chaque terme est égal au triple du terme précédent :")
        k = 1
        for i in range(12):
            print(str(i + 1) + " : " + str(k))
            k = k * 3

    elif n==str(4):
        print("4. Volume d'un parallélépipède rectangle : ")
        def Volume(l: float, h: float, p: float):
            """
            Calcule le volume d'un parallelepipede rectangle
            :param l: Largeur
            :param h: Hauteur
            :param p: Profondeur
            :return: volume
            """
            return l * h * p
        l=float(input('Largeur = '))
        h=float(input('Hauteur = '))
        p=float(input('Profondeur = '))
        print(Volume(l, h, p))

    elif n==str(5):
        def date(s: int):
            """
            Converti un npmbre de seconde en date
            :param s: nombre de seconde
            :return: string de la date
            """
            j = s // 86400
            s = s % 86400
            h = s // 3600
            s = s % 3600
            m = s // 60
            s = s % 60
            print(str(j) + ' jour(s) ' + str(h) + ' heure(s) ' + str(m) + ' minutes ' + str(s) + ' seconde(s)')
        s = int(input("Nombre de seconde :"))
        date(s)
    elif n==str(6):
        print("20 premiers termes de la table de multiplication par 7 et * = multiple de 3 :")
        for i in range(20):
            print(str(i * 7) + '*' if (i * 7 % 3 == 0) else str(i * 7), end=" ")

    elif n==str(7):
        k = ""
        for i in range(7):
            k += str(i + 1) + " "
            print(k)

    elif n==str(8):
        k = "1 2 3 4 5 6 7"
        for i in range(7):
            print(k)
            k = k[0:-2]
    else :
        print('End')
        break