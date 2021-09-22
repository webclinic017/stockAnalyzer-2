import requests
import pandas as pd


#Returns current block height
def getBlockheight():
    url = 'http://umbrel.local:3002/api/blocks/tip/height'
    req = requests.get(url)
    data = req.json()
    print(data)
    return data

#Returns current block height
def getCurrentBlockHash():
    url = 'http://umbrel.local:3002/api/blocks/tip/hash'
    req = requests.get(url)
    data = req.json()
    print(data)
    return data

#Returns details of a block by block height
def getDetailsByBlockHeight(height):
    url = 'http://umbrel.local:3002/api/block/:' + height
    req = requests.get(url)
    data = req.json()
    print(data)
    return data

#Returns details of a block by Hash
def getDetailsByBlockHash(hash):
    url = 'http://umbrel.local:3002/api/block/:' + hash
    req = requests.get(url)
    data = req.json()
    print(data)
    return data

#Returns details of a transaction by a given transaction id
def getTransactionDetails(transactionID):
    url = 'http://umbrel.local:3002/api/tx/:' + transactionID
    req = requests.get(url)
    data = req.json()
    print(data)
    return data

#Returns details of a transaction by a given transaction id
def getCirculatingSupply():
    url = 'http://umbrel.local:3002/api/blockchain/coins'
    req = requests.get(url)
    data = req.json()
    print(data)
    return data


#Returns the network hash rate, estimated over the last 1, 7, 30, 90, and 365 days.
def getHashrate():
    url = 'http://umbrel.local:3002/api/mining/hashrate'
    req = requests.get(url)
    data = req.json()
    print(data)
    return data

#Returns the network hash rate, estimated over the last 1, 7, 30, 90, and 365 days.
def getDiffAdjEst():
    url = 'http://umbrel.local:3002/api/mining/diff-adj-estimate'
    req = requests.get(url)
    data = req.json()
    print(data)
    return data


#Returns details for the specified extended public key, including related keys and addresses.Optional params:
def getConnectionsAndDetails(extendedPublicKey):
    url = 'http://umbrel.local:3002/api/util/xyzpub/:' + extendedPublicKey
    req = requests.get(url)
    data = req.json()
    print(data)
    return data

