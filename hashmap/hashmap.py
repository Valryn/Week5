class HashMap:

    @property
    def size(self):
        return self.__size

    @property
    def slots(self):
        return self.__slots

    @property
    def data(self):
        return self.__data

    def __init__(self):
        self.__size = 11;
        self.__slots = [None] * self.size
        self.__data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None or self.slots[hashvalue] is "deleted":
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def delete(self, key):
        target = self.hashfunction(key, len(self.slots))

        while self.slots[target] != key:
            target = self.rehash(target, len(self.slots))

        self.slots[target] = "deleted"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashMap()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[44] = "goat"
H[31] = "cow"
H[55] = "pig"
H[11] = "collider1"
H[22] = "collider2"
H.delete(11)
H[11] = "collider3"
print(H.slots)
print(H.data)
# H.put(12, "Sparkle")
print(H.get(12))
print(H[31])
print(H[22])
print(H[11])
