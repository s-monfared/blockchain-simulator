import csv
import subprocess
import time
from datetime import datetime
import os

monitorInteration = 100


def get_docker_stats():
    output = subprocess.run(['docker', 'stats', '--no-stream'], stdout=subprocess.PIPE)
    # print(output.stdout.decode('utf-8').splitlines())
    return output.stdout.decode('utf-8').splitlines()

def parse_stats(stats):
    headers = stats[0].split()
    rows = [row.split() for row in stats[1:]]
    # time_stamp = datetime.now()
    time_stamp = time.time()
    rows[0].append(time_stamp)
    rows[1].append(time_stamp)
    rows[2].append(time_stamp)
    return headers, rows

def write_to_csv(headers, rows, filename):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

def write_to_csv2(rows, filename):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(headers)
        writer.writerows(rows)

if __name__ == '__main__':
    filename = 'docker_stats.csv'
    # start_time = time.time()
    # print("start_time: ", start_time)
    # now = datetime.now()
    # start_time = now.strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]
    Sample_counter = 0
    # start_time = datetime.now()
    # print("time stamp:", start_time, "Sample counter:", Sample_counter)


    headers, rows = parse_stats(get_docker_stats())
    headers = ['Container_ID', 'Name', 'CPU_percentage', 'Mem_usage', '/', 'Mem_Limit', 'Mem_percentage', 'Net_I', '/', 'Net_O', 'Block_I', '/', 'Block_O', 'PIDS', 'Time_stamp']


    if os.path.getsize(filename) == 0:
        # print("The file is empty.")
        write_to_csv(headers, rows, filename)
    else:
        # print("The file is not empty.")
        write_to_csv2(rows, filename)


    
    # write_to_csv(headers, rows, filename)
    Sample_counter = 1

    while Sample_counter < monitorInteration:
        # time_stamp = datetime.now()
        # print("time stamp:", time_stamp, "Sample counter:", Sample_counter)
        headers, rows = parse_stats(get_docker_stats())
        write_to_csv2(rows, filename)
        Sample_counter = Sample_counter + 1
        # time.sleep(0.7)

    # end_time = time.time()
    # end_time = datetime.now()
    # print("time stamp:", end_time, "Sample counter:", Sample_counter)
    # headers, rows = parse_stats(get_docker_stats())
    # write_to_csv(headers, rows, filename)

    # print("start_time: ", start_time)
    # print("end_time: ", end_time)
    # print("duration:", end_time - start_time)

