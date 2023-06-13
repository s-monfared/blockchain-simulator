# blockchain-simulator
Simulating and testing Algorand blockchain platform.
The prerequisites for running this project are Docker and Python3.
After installing the prerequisites, you need to open the terminal and go to the sandbox directory. By running 
./sandbox up dev -v 
the Algorand blockchain network will start. If you wish to run the network with different configuration, you need to change the files and save it and then run the 
./sandbox down dev
Next, you need to clean the previous network by running 
./sandbox clean dev
Then you can start the new network. 
After starting the network, you can see the list of the nodes by running this command:
./sandbox goal account list
In order to get the mnemoic for a node, you can use this command:
./sandbox goal account export -a [ACCT]
instead of [ACCT] you need to write the public address of a node.
Next you need to replace the new mnemoic with the ones already in the project. First you need to update the creator_mnemoic in the createApp.py. Next, you need to update it in the workloadAndCallApp.py so that can have access to one of the nodes in the network to send a message to the blockchain.
When the network is running, you can move to the autoRun.py and run it using the following command:
python autorun.py
This file will aytomatically start the sandbox network, create the application, start the resource monitoring module, start the workload and submit the transactions to the network. Then it will analyze the results, calculate the average of resource utilizations and then save the results. 
By running
python plot.py
you can plot the figures to help you compare the experiments.
