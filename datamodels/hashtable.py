stock_prices = []
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

    for element in stock_prices:
        if element[0] == "":
            print(element[1])


stock_prices2 = {}
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

    for element in stock_prices:
        if element[0] == "":
            print(element[1])


            #integer index vs string index
            #dictionary python specific implementation of hashtable
            #look up by key is o(1)
            #insertion/deletion is o(1)

def get_hash(key):
    h = 0
    for char in key: 
        h += ord(char)
        return h % 100

#finding numbers on ascii via hash

get_hash('')

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key: 
            h += ord(char)
            return h % self.MAX

    def __setitem__ (self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__ (self, key):
        h = self.get_hash(key)
        return self.arr[h]





t = HashTable()
t.get_hash()
t.add()


#operater functions python documentation