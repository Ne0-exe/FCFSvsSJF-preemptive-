import pickle
import matplotlib.pyplot as plt
import random
import numpy as np

x = []
y = []
dic_list = pickle.load(open("Dic_List.p", "rb"))

class SJF:

    def manager(self, id, burst, arrive, id_lst):
        queue = []
        for i in range(len(burst)):
            temp = []
            temp.extend([i+1, arrive[i], burst[i], 0]) #0 - niezakonczony proces, 1 - zakonczony
            queue.append(temp)
        SJF.schedule(self, queue)


#stworzylem tablice 'queue' zawierajaca 100 tablic, kazda na razie zawiera 4 pozycje
#queue = [[id, arrive, burst, 0/1],[ , , , ],[ , , , ],[ , , , ],....]


    def schedule(self, queue):
        begin = []
        stop = []
        sTime = 0
        queue.sort(key=lambda x:x[1]) #sortuje po arrival

        for i in range(len(queue)):
            ready = []
            temp = []
            normal = []
            for a in range(len(queue)):
                if(queue[a][1] <= sTime) and (queue[a][3] == 0): # jezeli arrive <= czasu sTime i proces nie jest zakonczony (0)
                    temp.extend([queue[a][0], queue[a][1], queue[a][2]]) #to rozszerzam tablice temp o wartosci: id, arrive, burst
                    ready.append(temp) #tworze tablice tablic ready z powyzszymi pozycjami
                    temp= []
                elif queue[a][3] == 0: #rowniez jesli proces nie jest wykonany (0)
                    temp.extend([queue[a][0], queue[a][1], queue[a][2]]) #to rozszerzam tablice temp o wartosci: id, arrive, burst
                    normal.append(temp) #tworze tablice tablic normal z powyzszymi pozycjami
                    temp = []
            if len(ready) != 0: #jezeli dlugosc tablicy ready jest rozna od 0
                ready.sort(key=lambda x:x[2]) #to sortuje po burst
                begin.append(sTime) #do tablicy begin dodaje sTime
                sTime = sTime + ready[0][2] #do wartosci sTime dodaje burst_time
                eTime = sTime
                stop.append(eTime) #do tablicy stop dodaje eTime
                for b in range(len(queue)):
                    if queue[b][0] == ready[0][0]: #jezeli id w queue jest rowne id w tablicy ready
                        break
                queue[b][3] = 1 #w innym wypadku zaznacz koniec procesu w tablicy queue (1)
                queue[b].append(eTime) #do tablicy queue dodaj 5. wartosc - eTime (czas realizacji?)
            elif len(ready) == 0: # rowniez jesli dlugosc tablicy ready = 0
                if sTime < normal[0][1]: # jesli sTime < arrive time
                    sTime = normal[0][1] #sTime = arrive time
                begin.append(sTime) # do tablicy begin dodaj kolejna wartosc
                sTime = sTime + normal[0][2] #do wartosci sTime dodaje burst_time
                eTime = sTime
                stop.append(eTime) #do tablicy stop dodaje eTime
                for b in range(len(queue)):
                    if queue[b][0] == ready[0][0]: #jezeli id w queue jest rowne id w tablicy ready
                        break
                queue[b][3] = 1 #w innym wypadku zaznacz koniec procesu w tablicy queue (1)
                queue[b].append(eTime) #do tablicy queue dodaj 5. wartosc - eTime, zakonczenie procesu
        tTime = SJF.TurnaroundTime(self, queue) #do zmiennej tTime (turnaround) dodaje czas realizacji
        wTime = SJF.WaitingTime(self, queue) # do zmiennej wTime (waiting time) dodaje czas oczekiwania
        SJF.PrintData(self, queue, tTime, wTime) #wypisuje dane
    def TurnaroundTime(self, queue):
        total_turnaround = 0 #calkowity czas realizacji
        for a in range(len(queue)):
            turnaround_time = queue[a][4] - queue[a][1] #zakonczenie - przybycie
            total_turnaround += turnaround_time
            queue[a].append(turnaround_time) # do tablicy tablic queue dodaje 6. wartosc - czas realizacji
        average_turnaround = total_turnaround/len(queue) #sredni czas realizacji

        return average_turnaround

    def WaitingTime(self, queue):
        total_waiting = 0
        for b in range(len(queue)):
            waiting_time = queue[b][5] - queue[b][2] # turnaround - burst
            total_waiting += waiting_time
            queue[b].append(waiting_time) # do tablicy tablic queue dodaje 7. wartosc - czas oczekiwania
        average_waiting = total_waiting/len(queue) # sredni czas oczekiwania

        return average_waiting

    def PrintData(self, queue, average_turnaround, average_waiting):
        global Total_average_waiting
        global Total_average_turnaround
        queue.sort(key=lambda x:x[0]) #sortuje po ID

        print("ID Procesu\tPrzybycie\tBurst\tZakonczony?\tCzas zakonczenia\tCzas realizacji\tCzas oczekiwania")

        for i in range(len(queue)):
            for a in range(len(queue[i])):
                print(queue[i][a], end="\t\t")
            print()
        print("Sredni czas realizacji ", average_turnaround)
        Total_average_turnaround += average_turnaround
        print("Sredni czas oczekiwania ", average_waiting, "s")
        Total_average_waiting += average_waiting
        y.append(average_waiting)


Total_average_waiting = 0
Total_average_turnaround = 0
for i in range(len(dic_list)):
    burst = []
    arrive = []
    id_lst = []
    id = 1
    x.append(i)
    for key, val in dic_list[i].items():
        burst.append(val)
        arrive.append(key)
        id_lst.append(id)
        id += 1
    sjf = SJF()
    sjf.manager(id, burst, arrive, id_lst)



print("OSTATECZNIE SREDNI CZAS OCZEKIWANIA WYNIOSL => ", Total_average_waiting/100, "s")
print("OSTATECZNIE SREDNI CZAS REALIZACJI WYNIOSL => ", Total_average_turnaround/100, "s")

# TWORZENIE GRAFU
y_mean = [np.mean(y)]*len(x)
fig, ax = plt.subplots()
mean_line = ax.plot(x, y_mean, label='Mean', linestyle='--')
plt.plot(x, y)
plt.xlabel("Nr cyklu")
plt.ylabel("Średni czas oczekiwania cyklu")
plt.title("SJF(np) - średni czas oczekiwania 100 cykli")
plt.show()
print("Średni czas oczekiwania"
      " używajac SFJ wyniosl: ", Total_average_waiting/100, 's')
print("Średni czas realizacji"
      " używajac SFJ wyniosl: ", Total_average_turnaround/100, 's')
# ----------------------------------------
