Requisiti:
    Python                          3.10.1
    pymongo                         4.0.1
    Docker Engine                   20.10.12

Istruzioni:
    1    Installare i requisiti
    2    Dare i seguenti comandi da terminale:

        2.1     docker run -p 27017:27017 -d mongo
                salvare il container id che viene stampato a video
                                                                  
        2.2     docker cp <path_to_file>/sensordb.json <container_id>:/tmp/
                modificare il comando inserendo il proprio path al file e il container id salvato precedentemente

        2.3     docker exec <container_id> mongoimport --db db --collection sensordb --file /tmp/sensordb.json --jsonArray
                modificare il comando con il proprio container id

    3   Eseguire lo script python (inserendo il proprio path al file)
        py <path_to_file>/challenge.py