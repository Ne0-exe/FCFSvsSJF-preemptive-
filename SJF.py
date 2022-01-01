import pickle

dic_list = pickle.load(open("Dic_List.p", "rb"))


class SJF:
    def manager(self, id_lst, burst, arrive):
        queue = []
        for i in range(100):
            temp = [id_lst[i], arrive[i], burst[i], 0]  # 0 - niezakonczony proces, 1 - zakonczony
            queue.append(temp)
            temp = []
        SJF.schedule(self, queue)

    def schedule(self, queue):
        begin = []
        stop = []
        sTime = 0
        queue.sort(key=lambda x: x[1])  # sortuje po arrival
        for i in range(len(queue)):
            ready = []
            temp = []
            normal = []
            for a in range(len(queue)):
                if (queue[a][1] <= sTime) and (queue[a][3] == 0):
                    temp.extend([queue[a][0], queue[a][1], queue[a][2]])
                    ready.append(temp)
                    temp = []
                elif queue[a][3] == 0:
                    temp.extend([queue[a][0], queue[a][1], queue[a][2]])
                    normal.append(temp)
                    temp = []
            if len(ready) != 0:
                ready.sort(key=lambda x: x[2])  # sortuje po burst
                begin.append(sTime)
                sTime = sTime + ready[0][2]
                eTime = sTime
                stop.append(eTime)
                for a in range(len(queue)):
                    if queue[a][0] == ready[0][0]:
                        break
                    queue[a][3] = 1
                    queue[a].append(eTime)
            elif len(ready) == 0:
                if sTime < normal[0][1]:
                    sTime = normal[0][1]
                begin.append(sTime)
                sTime = sTime + normal[0][2]
                eTime = sTime
                stop.append(eTime)
                for a in range(len(queue)):
                    if queue[a][0] == ready[0][0]:
                        break
                    queue[a][3] = 1
                    queue[a].append(eTime)
            tTime = SJF.TurnaroundTime(self, queue)
            wTime = SJF.WaitingTime(self, queue)
            SJF.PrintData(self, queue, tTime, wTime)

    def TurnaroundTime(self, queue):
        total_turnaround = 0
        for i in range(len(queue)):
            turnaround_time = queue[i][4] - queue[i][1]  # zakonczenie - przybycie
            total_turnaround = total_turnaround + turnaround_time
            queue[i].append(turnaround_time)
        average_turnaround = total_turnaround / len(queue)
        return average_turnaround

    def WaitingTime(self, queue):
        total_waiting = 0
        for i in range(len(queue)):
            waiting_time = queue[i][5] - queue[i][2]  # turnaround - burst
            total_waiting = total_waiting + waiting_time
            queue[i].append(waiting_time)
        average_waiting = total_waiting / len(queue)
        return average_waiting

    def PrintData(self, queue, average_turnaround, average_waiting):
        queue.sort(key=lambda x: x[0])  # sortuje po ID

        print("ID Procesu Przybycie Burst   Zakonczenie Czas realizacji Czas oczekiwania")

        for i in range(len(queue)):
            for a in range(len(queue[i])):
                print(queue[i][a], end="				")
            print()
        print("Sredni czas realizacji ", average_turnaround)


for i in range(1):
    burst_lst = []
    arrive_lst = []
    id_lst = []
    id = 1
    for key, val in dic_list[i].items():
        burst_lst.append(val)
        arrive_lst.append(key)
        id_lst.append(id)
        id += 1
    sjf = SJF()
    sjf.manager(id_lst, burst_lst, arrive_lst)
