import pymongo
import string    
import random
import traceback

try:
    #   collegamento a mongo
    conn_str = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    #   seleziono db e collection
    db = client.db
    coll = db["sensordb"]
except BaseException as e:
    print(traceback.format_exc())

#   ritorna una stringa casuale [a-z0-9] di lunghezza = size
def getRandom(size):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k = size))

#   popola il database con i 10 documenti
def popolateDB():
    try:
        coll.delete_many({})
        #   creo una lista di appoggio per fare in modo che alcuni documenti condividano la stessa stringa
        allDeviceList = []

        for x in range(10):
            devices = []
            #   creazione della lista devices
            for y in range(random.randint(1, 100)):
                deviceToAdd = ""
                #   se la lista di appoggio non è vuota e se random mi restituisce un numero divisibile per due
                #   aggiungo un device presente in un altro documento, altrimenti lo genero random
                if len(allDeviceList) > 0 and random.randint(1, 100) % 2 == 0:
                    deviceToAdd = random.choice(allDeviceList)
                else:
                    deviceToAdd = getRandom(16)
                devices.append(deviceToAdd)
            #   creo il documento finale
            obj = {
                "deviceid": getRandom(5),
                "devices": devices,
                "epoch": random.randint(1,1609459200)
            }
            #   aggiorno la lista di appoggio
            allDeviceList += devices
            #   inserisco il documento
            coll.insert_one(obj)
        print("Ok")
    except BaseException as e:
        print(traceback.format_exc())

try:
    popolateDB()
    result = []
    count = 0
    #   scorro tutti i documenti
    cursor = coll.find({})
    for obj in cursor:
        #   scorro la lista devices
        for device in obj["devices"]:
            #   uso un contatore per avere la lunghezza della lista con ripetizioni
            count = count + 1
            #   aggiungo la stringa alla lista finale solo se non è già presente
            if device not in result : result.append(device)
    print("Lista senza ripetizioni :: " + str(result))
    print("Lunghezza lista senza ripetizioni :: " + str(len(result)))
    print("Lunghezza lista con ripetizioni :: " + str(count))
except BaseException as e:
    print(traceback.format_exc())
