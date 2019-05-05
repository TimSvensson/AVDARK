
class memory:
    def __init__(self, size):
        self.size = size
        self.data = [0] * self.size

        #def __repr__(self):
        #    pass

    def __str__(self):
        s = "<{}, self.size: {}\n", self.__class__.__name__, self.size)
        lbound = 0
        while lbound < self.size:
            rbound = lbound + 10 < self.size ? lbound + 10 : self.size
            s += "".format()

        return s
        return "<{}, self.size: {}, self.data: {}>".format(
            self.__class__.__name__, self.size, self.data)
    

    def store(self, data, address):
        if address < 0 or address > self.size:
            return
        self.data[address] = data
    
    def load(self, address):
        if address < 0 or address > self.size:
            return None
        return self.data[address]

if __name__ == "__main__":
    m = memory(4)
    m.store(1,2)
    m.store(10,3)
    print(m)
