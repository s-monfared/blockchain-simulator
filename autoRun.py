import time

import subprocess

import os
import signal

# os.chdir('sandbox')
# os.system('./sandbox reset dev')
# os.chdir('..')
# os.system('python createApp.py')
# time.sleep(20)


for i in range(0, 1):

    os.chdir('sandbox')

    os.system('./sandbox down dev')

    # os.system('./sandbox reset dev')

    os.system('./sandbox up dev')

    os.chdir('..')

    # time.sleep(1)

    # os.system('python createApp.py')

    # time.sleep(1)

    # os.system('python plugin-resource-monitor.py')
    process = subprocess.Popen(['python', 'resource-monitor.py'])
    # terminal1.communicate('python', 'plugin-resource-monitor.py')
    # subprocess.run(['python', 'plugin-resource-monitor.py'])

    time.sleep(3)

    os.system('python workloadAndCallApp.py')

    time.sleep(1)

    os.system('python analyze.py')

    # time.sleep(1)

    process.send_signal(signal.SIGINT)

    # time.sleep(1)


# time.sleep(1)

os.system('python average_experiments.py')