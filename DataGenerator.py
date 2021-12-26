# MODUŁ ZAWIERAJĄCY PROCES TWORZENIA I SERIALIZACJI DANYCH WEJŚCIOWYCH

import pickle
import random

dic_list = []
counter = 0
while counter < 100:
    dic = {}
    var = random.sample(range(1, 100), 99)
    var.sort()
    for i in range(100):
        if i == 0:
            dic[i] = random.randrange(1, 20)
            continue
        else:
            dic[var[i-1]] = random.randrange(1, 20)
    dic_copy = dic.copy()
    dic_list.append(dic_copy)
    counter += 1

pickle.dump(dic_list, open("Dic_List.p", "wb"))