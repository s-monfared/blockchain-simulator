import time
import pandas as pd
import subprocess
import os

docker_data = pd.read_csv("docker_stats.csv")
experiment_data = pd.read_csv("experiment_data.csv")

sumCPU = 0
sumMem = 0
sumNetIn = 0
sumNetOut = 0
sumDiskRead = 0
sumDiskWrite = 0

counter = 0


for j in range (0, experiment_data.start_time.size):
    if (experiment_data.toAnalyze[j] == 'Yes'):
        for i in range (0, docker_data.Time_stamp.size):
            if ((docker_data.Name[i] == 'algorand-sandbox-algod') & (docker_data.Time_stamp[i] > experiment_data.start_time[j]) & (docker_data.Time_stamp[i] < experiment_data.end_time[j])):
                my_string = docker_data.CPU_percentage[i]
                new_string = my_string[:-1]
                double_num = float(new_string)
                sumCPU = sumCPU + double_num

                my_string = docker_data.Mem_percentage[i]
                new_string = my_string[:-1]
                double_num = float(new_string)
                sumMem = sumMem + double_num

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
                sumNetIn = double_num


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
                sumNetOut = double_num

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
                # sumDiskRead = sumDiskRead + double_num
                sumDiskRead = double_num

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
                sumDiskWrite = double_num

                counter = counter + 1

        # Modify the value of a cell
        if (counter != 0):
            experiment_data.loc[j, 'AvgCPU_Percentage'] = round(sumCPU/counter, 2)
            experiment_data.loc[j, 'AvgMem_Percentage'] = round(sumMem/counter, 2)
            experiment_data.loc[j, 'NetInput'] = round(sumNetIn, 2)
            experiment_data.loc[j, 'NetOut'] = round(sumNetOut, 2)
            experiment_data.loc[j, 'DiskRead'] = round(sumDiskRead, 2)
            experiment_data.loc[j, 'DiskWrite'] = round(sumDiskWrite, 2)
            experiment_data.loc[j, 'toAnalyze'] = 'No'


            # Write the modified dataframe back to the CSV file
            experiment_data.to_csv("experiment_data.csv", index=False)

