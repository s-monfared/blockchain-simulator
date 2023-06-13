import csv
import os
import pandas as pd
from matplotlib import pyplot as plt

average_data = pd.read_csv("docker_average.csv")

diagram1Label = "new-block"
diagram1LabelToShow = "Each-Transaction"
diagram1Time = []
diagram1CPU = []
diagram1Memory = []
diagram1NetI = []
diagram1NetO = []
diagram1DiskR = []
diagram1DiskW = []

diagram2Label = "High"
diagram2LabelToShow = "Each-Round"
diagram2Time = []
diagram2CPU = []
diagram2Memory = []
diagram2NetI = []
diagram2NetO = []
diagram2DiskR = []
diagram2DiskW = []

for i in range (0, average_data.time_stamp.size):
    if (average_data.workloadLabel[i] == diagram1Label):
        diagram1Time.append(average_data.time_stamp[i])
        diagram1CPU.append(average_data.cpu[i])
        diagram1Memory.append(average_data.memory[i])
        diagram1NetI.append(average_data.netI[i])
        diagram1NetO.append(average_data.netO[i])
        diagram1DiskR.append(average_data.diskR[i])
        diagram1DiskW.append(average_data.diskW[i])
    elif (average_data.workloadLabel[i] == diagram2Label):
        diagram2Time.append(average_data.time_stamp[i])
        diagram2CPU.append(average_data.cpu[i])
        diagram2Memory.append(average_data.memory[i])
        diagram2NetI.append(average_data.netI[i])
        diagram2NetO.append(average_data.netO[i])
        diagram2DiskR.append(average_data.diskR[i])
        diagram2DiskW.append(average_data.diskW[i])


# colorList = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# #     CPU
# legend = 'Workload traffic: ', diagram1LabelToShow
# plt.plot(diagram1Time, diagram1CPU, color='blue', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("CPU percentage")
# legend = 'Workload traffic: ', diagram2LabelToShow
# plt.plot(diagram2Time, diagram2CPU, color='red', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("CPU percentage")

# #     Memory
# legend = 'Workload traffic: ', diagram1LabelToShow
# plt.plot(diagram1Time, diagram1Memory, color='blue', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Memory percentage")
# legend = 'Workload traffic: ', diagram2LabelToShow
# plt.plot(diagram2Time, diagram2Memory, color='red', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Memory percentage")

# #     NetI
# legend = 'Workload traffic: ', diagram1LabelToShow
# plt.plot(diagram1Time, diagram1NetI, color='blue', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Network input (KB)")
# legend = 'Workload traffic: ', diagram2LabelToShow
# plt.plot(diagram2Time, diagram2NetI, color='red', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Network input (KB)")

# #     NetO
# legend = 'Workload traffic: ', diagram1LabelToShow
# plt.plot(diagram1Time, diagram1NetO, color='blue', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Network output (KB)")
# legend = 'Workload traffic: ', diagram2LabelToShow
# plt.plot(diagram2Time, diagram2NetO, color='red', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Network output (KB)")

# #     DiskR
# legend = 'Workload traffic: ', diagram1LabelToShow
# plt.plot(diagram1Time, diagram1DiskR, color='blue', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Disk Read (KB)")
# legend = 'Workload traffic: ', diagram2LabelToShow
# plt.plot(diagram2Time, diagram2DiskR, color='red', label=legend)
# plt.xlabel("Time stamp (S)")
# plt.ylabel("Disk Read (KB)")

#     DiskW
legend = 'Workload traffic: ', diagram1LabelToShow
plt.plot(diagram1Time, diagram1DiskW, color='blue', label=legend)
plt.xlabel("Time stamp (S)")
plt.ylabel("Disk Write (KB)")
legend = 'Workload traffic: ', diagram2LabelToShow
plt.plot(diagram2Time, diagram2DiskW, color='red', label=legend)
plt.xlabel("Time stamp (S)")
plt.ylabel("Disk Write (KB)")


plt.legend()
plt.show()