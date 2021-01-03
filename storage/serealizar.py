# License:      MIT License
# Notice:       Copyright (c) 2021 TytusDB Team 9
# Developer:    Byron Par
# import pickle
# import threading

# path = 'data/'


# def commit(objeto, nombre):
#     try:
#         file = open(path + nombre + ".bin", "wb+")
#         file.write(pickle.dumps(objeto))
#         file.close()
#     except:
#         ''
#
#
# def rollback(nombre):
#     try:
#         file = open(path + nombre + ".bin", "rb")
#         b = file.read()
#         file.close()
#         return pickle.loads(b)
#     except:
#         return {}
#
#
# def hacerCommit(objeto, nombre):
#     h1 = threading.Thread(target=commit, args=(objeto, nombre), daemon=True)
#     h1.start()
