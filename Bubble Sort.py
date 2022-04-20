import time


def bubbleSort(list_elemente):
    n = len(list_elemente)
    interschimbare = True
    while interschimbare:
        interschimbare = False
        for i in range(n - 1):
            if list_elemente[i] > list_elemente[i + 1]:
                list_elemente[i], list_elemente[i + 1] = list_elemente[i + 1], list_elemente[i]
                interschimbare = True


if __name__ == '__main__':
    list_elemente = []
    fisier = open("lista_elemente.in", "r")
    linie = fisier.readline().strip().split(' ')
    for i in range(len(linie)):
        list_elemente.append(linie[i])
    fisier.close()

    start_time = time.time()
    bubbleSort(list_elemente)
    print("Timpul de procesare este de: %.3f seconds " % (time.time() - start_time))

    scriere_fisier = open("lista_finala.out", "w")
    for j in range(len(list_elemente)):
        scriere_fisier.write(str(list_elemente[j]))
        scriere_fisier.write(' ')
    scriere_fisier.close()
