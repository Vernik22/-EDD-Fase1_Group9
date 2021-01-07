# License:      MIT License
# Notice:       Copyright (c) 2021 TytusDB Team 9
# Developer:    Byron Par
import pickle


# import threading


def commit(objeto, direccion):
    try:
        file = open(direccion + "\\data", "wb+")
        file.write(pickle.dumps(objeto))
        file.close()
    except:
        print("Error Commit")


def rollback(direccion):
    try:
        file = open(direccion + "\\data", "rb")
        b = file.read()
        file.close()
        return pickle.loads(b)
    except:
        print("Error Rollback")
