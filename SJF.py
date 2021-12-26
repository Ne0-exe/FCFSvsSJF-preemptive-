import pickle

dic_list = pickle.load(open("Dic_List.p", "rb"))

for i in range(len(dic_list)):
    lst = []  # lista potrzebnego czasu na wykonanie
    order = []
    timer = 0  # dazy do momentu przybycia ostatniego procesu (po dodaniu casu na wykonanie)
    for key, val in dic_list[i].items():
        lst.append(val)  # dodaję do tablicy potrzebny czas na wykonanie
        if key == 0:  # proces początkowy
            order.insert(0, val)
            lst[i] -= 1  # odejmuje sekunde
            order[0] -= 1
            timer += 1
        else:
            if key == timer:
                for a in range(len(order)-2, 0):
                    order.append(lst[i])
                    l = len(order) - 1
                    if order[l] < order[a]:
                        order[l], order[a] = order[a], order[l]
                    else:
                        continue
                order[0] -= 1
                timer += 1
                print(order)
            else:
                timer += 1
    print("Skonczylem cykl nr", i)

print("skonczylem")
print(order)
