import csv
import os
from matplotlib import pyplot as plt
import pandas as pd
from statistics import mean

docker_data = pd.read_csv("docker_stats.csv")
experiment_data = pd.read_csv("experiment_data.csv")

sumCPU = 0
sumMem = 0
sumNetIn = 0
sumNetOut = 0
sumDiskRead = 0
sumDiskWrite = 0

counter = 0

CPUList = []
timeStampList = []
# 2D list: j = #cols and i = #rows

twoDcpu = []
twoDmem = []
twoDnetI = []
twoDnetO = []
twoDdiskR = []
twoDdiskW = []

twoDtime = []
# c = 0
legendList = []
for j in range (0, experiment_data.start_time.size):
    if (experiment_data.toAverage[j] == 'Yes'):
        twoDcpu.append([])
        twoDmem.append([])
        twoDnetI.append([])
        twoDnetO.append([])
        twoDdiskR.append([])
        twoDdiskW.append([])

        twoDtime.append([])
        legendList.append(experiment_data.workloadLabel[j])
        for i in range (0, docker_data.Time_stamp.size):
            if ((docker_data.Name[i] == 'algorand-sandbox-algod') & (docker_data.Time_stamp[i] > experiment_data.start_time[j]) & (docker_data.Time_stamp[i] < experiment_data.end_time[j])):
                my_string = docker_data.CPU_percentage[i]
                new_string = my_string[:-1]
                double_num = float(new_string)
                twoDcpu[counter].append(double_num)

                my_string = docker_data.Time_stamp[i]
                double_num = float(my_string)
                twoDtime[counter].append(double_num)


                my_string = docker_data.Mem_percentage[i]
                new_string = my_string[:-1]
                double_num = float(new_string)
                twoDmem[counter].append(double_num)
                
                
                my_string = docker_data.Net_I[i]
                if (my_string[len(my_string) - 2] == 'M'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                    double_num = double_num * 1000
                elif (my_string[len(my_string) - 2] == 'k'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                else:
                    new_string = my_string[:-1]
                    double_num = float(new_string)
                # sumNetIn = sumNetIn + double_num
                twoDnetI[counter].append(double_num)

                
                # sumNetIn = double_num


                my_string = docker_data.Net_O[i]  
                if (my_string[len(my_string) - 2] == 'M'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                    double_num = double_num * 1000
                elif (my_string[len(my_string) - 2] == 'k'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                else:
                    new_string = my_string[:-1]
                    double_num = float(new_string)
                # sumNetOut = sumNetOut + double_num
                twoDnetO[counter].append(double_num)

                # sumNetOut = double_num

                my_string = docker_data.Block_I[i]
                if (my_string[len(my_string) - 2] == 'M'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                    double_num = double_num * 1000
                elif (my_string[len(my_string) - 2] == 'k'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                else:
                    new_string = my_string[:-1]
                    double_num = float(new_string)
                    
                twoDdiskR[counter].append(double_num)

                # sumDiskRead = sumDiskRead + double_num
                # sumDiskRead = double_num

                my_string = docker_data.Block_O[i]
                if (my_string[len(my_string) - 2] == 'M'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                    double_num = double_num * 1000
                elif (my_string[len(my_string) - 2] == 'k'):
                    new_string = my_string[:-2]
                    double_num = float(new_string)
                else:
                    new_string = my_string[:-1]
                    double_num = float(new_string)
                # sumDiskWrite = sumDiskWrite + double_num
                # sumDiskWrite = double_num
                twoDdiskW[counter].append(double_num)


        counter = counter + 1
    
# print(counter)
    experiment_data.loc[j, 'toAverage'] = 'No'
    # Write the modified dataframe back to the CSV file
    experiment_data.to_csv("experiment_data.csv", index=False)

        # Modify the value of a cell
        # if (counter != 0):
        #     experiment_data.loc[j, 'AvgCPU_Percentage'] = round(sumCPU/counter, 2)
        #     experiment_data.loc[j, 'AvgMem_Percentage'] = round(sumMem/counter, 2)
        #     experiment_data.loc[j, 'NetInput'] = round(sumNetIn, 2)
        #     experiment_data.loc[j, 'NetOut'] = round(sumNetOut, 2)
        #     experiment_data.loc[j, 'DiskRead'] = round(sumDiskRead, 2)
        #     experiment_data.loc[j, 'DiskWrite'] = round(sumDiskWrite, 2)
        #     experiment_data.loc[j, 'isAnalysed'] = 'Yes'


            # Write the modified dataframe back to the CSV file
            # experiment_data.to_csv("experiment_data.csv", index=False)



colorList = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# print(twoDtime[7])
# for i in range (0, len(twoDtime[7])):
#     print(twoDtime[7][i])
#     print("//////////////////////////")
# print(len(twoDtime[7]))
# counter = 0
# for i in range (0, len(twoDtime[7])):
#     print(twoDtime[7][i])
#     print("//////////////////////////")
#     counter = counter + 1

# print(counter)

for i in range(0, len(twoDtime)):
    firstTimeStamp = twoDtime[i][0]
    for j in range(0, len(twoDtime[i])):
        twoDtime[i][j] = round((twoDtime[i][j] - firstTimeStamp), 2)

finalTime = []
finalCPU = []
finalMemory = []
finalNetI = []
finalNetO = []
finalDiskR = []
finalDiskW = []

tempTime = []
tempCPU = []
tempMemory = []
tempNetI = []
tempNetO = []
tempDiskR = []
tempDiskW = []

# print(len(twoDtime))

# print(len(twoDtime[3]))

counter = 0
for j in range (0, len(twoDtime[0])): # 0 < j < 22
    for i in range (0, len(twoDtime)): # 0 < i < 9
        if (j < len(twoDtime[i])):
            tempTime.append(twoDtime[i][j])
            # print("//////////////////////////////")
            # print(tempTime)
            tempCPU.append(twoDcpu[i][j])
            tempMemory.append(twoDmem[i][j])
            tempNetI.append(twoDnetI[i][j])
            tempNetO.append(twoDnetO[i][j])
            tempDiskR.append(twoDdiskR[i][j])
            tempDiskW.append(twoDdiskW[i][j])

    # print(tempTime)
    if (tempTime):
        finalTime.append(round(mean(tempTime), 2))
        finalCPU.append(round(mean(tempCPU), 2))
        finalMemory.append(round(mean(tempMemory), 2))
        finalNetI.append(round(mean(tempNetI), 2))
        finalNetO.append(round(mean(tempNetO), 2))
        finalDiskR.append(round(mean(tempDiskR), 2))
        finalDiskW.append(round(mean(tempDiskW), 2))

    tempTime.clear()
    tempCPU.clear()
    tempMemory.clear()
    tempNetI.clear()
    tempNetO.clear()
    tempDiskR.clear()
    tempDiskW.clear()

# print(len(finalTime))

# print(finalTime)

def write_to_csv(headers, row, filename):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(row)

def write_to_csv2(row, filename):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(headers)
        writer.writerow(row)

for i in range (0, len(finalTime)):

    filename = 'docker_average.csv'
    headers = ['time_stamp', 'cpu', 'memory', 'netI', 'netO', 'diskR', 'diskW', 'workloadLabel']
    row = [finalTime[i], finalCPU[i], finalMemory[i], finalNetI[i], finalNetO[i], finalDiskR[i], finalDiskW[i], legendList[0]]

    if os.path.getsize(filename) == 0:
        # print("The file is empty.")
        write_to_csv(headers, row, filename)
    else:
        # print("The file is not empty.")
        write_to_csv2(row, filename)
    
#     legend = 'Workload traffic: ', legendList[i]

#     plt.plot(twoDtime[i], twoDcpu[i], color=colorList[i%10], label=legend)
#     plt.xlabel("Time stamp")
#     plt.ylabel("CPU percentage")

#     # plt.plot(twoDtime[i], twoDmem[i], color=colorList[i%10], label=legend)
#     # plt.xlabel("Time stamp")
#     # plt.ylabel("Memory percentage")

#     # plt.plot(twoDtime[i], twoDnetI[i], color=colorList[i%10], label=legend)
#     # plt.xlabel("Time stamp")
#     # plt.ylabel("Network Input")

#     # plt.plot(twoDtime[i], twoDnetO[i], color=colorList[i%10], label=legend)
#     # plt.xlabel("Time stamp")
#     # plt.ylabel("Network Output")

    

# plt.legend()
# plt.show()

