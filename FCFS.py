import pickle
import matplotlib.pyplot as plt
import random
import numpy as np

dic_list = pickle.load(open("Dic_List.p", "rb"))

average_cycle = 0  # srednia dla jednego ze stu "cyklów" 100 procesów
average_full = 0  # średnia 100 cyklów
x = []
y = []

# ----------------FCFS--------------------
print("Średni czas cyklu nr ")
for i in range(len(dic_list)):
    for key, val in dic_list[i].items():
        if key == 0:
            continue  # czas oczekiwania = 0, wiec nic nie dodajemy
        else:
            average_cycle += val
    print('\t', i + 1, "\t\t", average_cycle/100)
    x.append(i)
    y.append(average_cycle/100)
    average_full += average_cycle/100
    average_cycle = 0


# TWORZENIE GRAFU
y_mean = [np.mean(y)]*len(x)
fig, ax = plt.subplots()
mean_line = ax.plot(x, y_mean, label='Mean', linestyle='--')
plt.plot(x, y)
plt.xlabel("Nr cyklu")
plt.ylabel("Średni czas oczekiwania cyklu")
plt.title("FCFS - średni czas oczekiwania 100 cykli")
plt.show()
print("Średni czas oczekiwania"
      " używajac FCFS wyniosl: ", average_full/100, 's')
# ----------------------------------------



