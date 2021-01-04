import os
from storage.b import BMode as b
from storage.hash import HashMode as hash
from storage.isam import ISAMMode as isam
from storage.bplus import BPlusMode as bplus
from storage.avl import avlMode as avl
from storage.json import jsonMode as json
from storage.dict import DictMode as dict
from storage import serealizar



def actualMod(mode):
    if mode == 'avl':
        return avl
    elif mode == 'b':
        return b
    elif mode == 'bplus':
        return bplus
    elif mode == 'dict':
        return dict
    elif mode == 'isam':
        return isam
    elif mode == 'json':
        return json
    elif mode == 'hash':
        return hash



