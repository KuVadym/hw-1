from abc import abstractmethod, ABCMeta
import json
import pickle
s = "1. 2, 3, 7"

class Meta(type):
    def __new__(*args):
        return type.__new__(*args)

    def __init__(self, *args):
        self.class_number = self.children_number
        Meta.children_number += 1

Meta.children_number = 0
 
class Cls1(metaclass=Meta):

    def __init__(self, data):

        self.data = data

class Cls2(metaclass=Meta):
    
    def __init__(self, data):

        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)

a, b = Cls1(''), Cls2('')

assert (a.class_number, b.class_number) == (0, 1)

class SerializationInterface():
    def save_data_bin(self, some_data):
        raise NotImplementedError()

    def save_data_json(self, some_data):
        raise NotImplementedError()

class SerializationJson(SerializationInterface):
    def save_data_json(self, some_data):
        file_name = "data.json"
        with open(file_name, "w") as fh:
            json.dump(some_data, fh)

class SerializationBin(SerializationInterface):
    def save_data_bin(self, some_data):
        file_name = "data.bin"
        with open(file_name, "wb") as fh:
            pickle.dump(some_data, fh)




sj = SerializationJson()
sb = SerializationBin()

sj.save_data_json(s)
sb.save_data_bin(s)
file_name = "data.json"
with open(file_name, "r") as fh:
    unpacked = json.load(fh)
print (unpacked)

file_name = "data.bin"
with open(file_name, "rb") as fh:
    unpacked = pickle.load(fh)
print (unpacked)
