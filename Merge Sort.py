import time


def mergeSort(list_elemente):
    if len(list_elemente) > 1:

        mijloc = len(list_elemente) // 2

        l = list_elemente[:mijloc]
        r = list_elemente[mijloc:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                list_elemente[k] = l[i]
                i += 1
            else:
                list_elemente[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            list_elemente[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            list_elemente[k] = r[j]
            j += 1
            k += 1


if __name__ == '__main__':
    list_elemente = []
    fisier = open("lista_elemente.in", "r")
    linie = fisier.readline().strip().split(' ')
    for i in range(len(linie)):
        list_elemente.append(linie[i])
    fisier.close()

    start_time = time.time()
    mergeSort(list_elemente)
    print("Timpul de procesare este de: %.3f seconds " % (time.time() - start_time))

    scriere_fisier = open("lista_finala.out", "w")
    for j in range(len(list_elemente)):
        scriere_fisier.write(str(list_elemente[j]))
        scriere_fisier.write(' ')
    scriere_fisier.close()
