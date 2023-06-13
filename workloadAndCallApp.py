import random
import time
from datetime import datetime
import base64
from algosdk.future import transaction
from algosdk import account, mnemonic
from algosdk.v2client import algod
from pyteal import *
import csv
import subprocess
import os

iterationCallApp = 90
firstQuarterSleepTime = 0.01
secondQuarterSleepTime = 0.01
thirdQuarterSleepTime = 0.01
forthQuarterSleepTime = 0.01
workloadLabel = 'new-block'

# sleepTimeCallApp = 0.02

# iterationCallApp * sleepTimeCallApp
sleepTimeCheckConfirmation = 0.1

creator_mnemoic = "barrel bring team follow grass edit crouch square eternal verb light theme practice patient deer script theory crouch kite inform license hurdle curtain abandon chapter"
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
transactionsList = []
appId = 1


# iterationCheckConfirmation = 6



def wait_for_confirmation(client, transaction_id, timeout):
    start_round = client.status()["last-round"] + 1
    current_round = start_round

    while current_round < start_round + timeout:
        try:
            pending_txn = client.pending_transaction_info(transaction_id)
        except Exception:
            return
        if pending_txn.get("confirmed-round", 0) > 0:
            return pending_txn
        elif pending_txn["pool-error"]:
            raise Exception('pool error: {}'.format(pending_txn["pool-error"]))
        client.status_after_block(current_round)
        current_round += 1
    raise Exception("pending tx not found in timeout rounds, timeout value = : {}".format(timeout))

def check_for_confirmation(client):

    for item in transactionsList[:]:
    # start_round = client.status()["last-round"] + 1
    # current_round = start_round
    # while current_round < start_round + timeout:
        try:
            pending_txn = client.pending_transaction_info(item)
        except Exception:
            return
        if pending_txn.get("confirmed-round", 0) > 0:
            # return pending_txn
            print("--------------------------------------------")
            print("Transaction confirmed:", item)
            print("confirmed-round:", pending_txn['confirmed-round'])
            print("--------------------------------------------")
            transactionsList.remove(item)

        # elif pending_txn["pool-error"]:
            # raise Exception('pool error: {}'.format(pending_txn["pool-error"]))
    # client.status_after_block(current_round)
    # current_round += 1
    # raise Exception("pending tx not found in timeout rounds, timeout value = : {}".format(timeout))


def format_state(state):
    formatted = {}
    # print(state)
    # print("///////////////////////////////")
    for item in state:
        # print(item)
        key = item['key']
        value = item['value']
        formatted_key = base64.b64decode(key).decode('utf-8')

        if value['type'] == 1:
            if formatted_key == 'voted':
                formatted_value = base64.b64decode(value['bytes']).decode('utf-8')

            else:
                formatted_value = value['bytes']
            formatted[formatted_key] = formatted_value
        else:
            formatted[formatted_key] = value['uint']
    return formatted

def read_global_state(client, addr, app_id):
    results = client.account_info(addr)
    apps_created = results['created-apps']
    for app in apps_created:
        if app['id'] == app_id:
            return format_state(app['params']['global-state'])
    return {}


def call_app(algod_client, private_key, index, app_args):
    sender = account.address_from_private_key(private_key)
    params = algod_client.suggested_params()
    txn = transaction.ApplicationNoOpTxn(sender, params, index, app_args)
    signed_txn = txn.sign(private_key)
    tx_id = signed_txn.transaction.get_txid()
    transactionsList.append(tx_id)
    algod_client.send_transactions([signed_txn])
    # wait_for_confirmation(client, tx_id, 5)
    check_for_confirmation(algod_client)
    print("Application called")
    print("--------------------------------------------")

def get_docker_stats():
    output = subprocess.run(['sudo', 'docker', 'stats', '--no-stream'], stdout=subprocess.PIPE)
    # print(output.stdout.decode('utf-8').splitlines())
    return output.stdout.decode('utf-8').splitlines()

def parse_stats(stats):
    headers = stats[0].split()
    rows = [row.split() for row in stats[1:]]
    return headers, rows

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

def main():
    algod_client = algod.AlgodClient(algod_token, algod_address)
    creator_private_key = mnemonic.to_private_key(creator_mnemoic)

    # print("Initial time:", time.time())

    # print("Initial time:", datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    startTime = time.time()
    # startTime = datetime.now()
    # startTime = now.strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]
    # filename = 'docker_stats.csv'
    # print("Monitoring the resource usage for the first time")
    # headers, rows = parse_stats(get_docker_stats())
    # write_to_csv(headers, rows, filename)



    sleepTime = 0
    for i in range (0, iterationCallApp):
        Key = random.randint(100,999)
        Value = random.randint(100,999)
        print("--------------------------------------------")
        print("Calling application #", i + 1)
        call_app(algod_client, creator_private_key, appId, app_args=["KeyValue", Key, Value])
        # print("be jaye call app ino print kon")

        if (i < iterationCallApp / 4):
            sleepTime = firstQuarterSleepTime
        elif (iterationCallApp / 4 < i < iterationCallApp / 2):
            sleepTime = secondQuarterSleepTime
        elif (iterationCallApp / 2 < i < 3 * iterationCallApp / 4):
            sleepTime = thirdQuarterSleepTime
        else:
            sleepTime = forthQuarterSleepTime

        print("Sleep for " ,sleepTime, " seconds...")
        time.sleep(sleepTime)

        


        # print("Monitoring the resource usage # ", i + 1)
        # headers, rows = parse_stats(get_docker_stats())
        # write_to_csv2(headers, rows, filename)


    # for i in range (0, iterationCheckConfirmation):
    #     if not transactionsList:
    #         break
    #     print("--------------------------------------------")
    #     print("Sleep for" ,sleepTimeCheckConfirmation, "seconds #", i + 1)
    #     time.sleep(sleepTimeCheckConfirmation)
    #     check_for_confirmation(algod_client)

    while (transactionsList):
        print("--------------------------------------------")
        print("Sleep for" ,sleepTimeCheckConfirmation, "seconds #", i + 1)
        time.sleep(sleepTimeCheckConfirmation)
        check_for_confirmation(algod_client)
        # print("Monitoring the resource usage while waiting for confirmation ")
        # headers, rows = parse_stats(get_docker_stats())
        # write_to_csv2(headers, rows, filename)


    print(transactionsList)

    endTime = time.time()
    # endTime = datetime.now()
    # endTime = now.strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]

    print("Experiment start: ", startTime)
    print("Experiment end: ", endTime)
    print("Experiment duration: ", endTime - startTime)


    notAssigned = 'notAssigned'
    filename = 'experiment_data.csv'
    headers = ['start_time', 'end_time', 'experiment_duration', 'appId', 'iterationCallApp', 'firstQuarterSleepTime', 'secondQuarterSleepTime', 'thirdQuarterSleepTime', 'forthQuarterSleepTime', 'sleepTimeCheckConfirmation', 'AvgCPU_Percentage', 'AvgMem_Percentage', 'NetInput', 'NetOut', 'DiskRead', 'DiskWrite', 'toAnalyze', 'toAverage', 'workloadLabel']
    row = [startTime, endTime, endTime - startTime, appId, iterationCallApp, firstQuarterSleepTime, secondQuarterSleepTime, thirdQuarterSleepTime, forthQuarterSleepTime, sleepTimeCheckConfirmation, notAssigned, notAssigned, notAssigned, notAssigned, notAssigned, notAssigned, 'Yes', 'Yes', workloadLabel]

    if os.path.getsize(filename) == 0:
        # print("The file is empty.")
        write_to_csv(headers, row, filename)
    else:
        # print("The file is not empty.")
        write_to_csv2(row, filename)



    # filename = 'experiment_start_end.csv'


    # print("New Global state:")
    # var = read_global_state(algod_client, account.address_from_private_key(creator_private_key), appId)["Key"]
    # print("Key: ", base64.b64decode(var).decode('utf-8'))
    # var2 = read_global_state(algod_client, account.address_from_private_key(creator_private_key), appId)["Value"]
    # print("Value: ", base64.b64decode(var2).decode('utf-8'))

    # return "successful"

if __name__ == "__main__":
    main()





