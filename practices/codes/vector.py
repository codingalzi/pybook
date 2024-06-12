class Vector(list):
    def __init__(self, items):
        
        super().__init__(items)
        
        self.len = self.__len__()
            
    def __add__(self, other):

        if self.len != other.len:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        new_list = []
        
        for i in range(self.len):
            item = self[i] + other[i]
            new_list.append(item)

        return Vector(new_list)

    def append(self, item):
        super().append(item)
        self.len = self.__len__()

    def pop(self, idx=-1):
        super().pop(idx)
        self.len = self.__len__()
    
    def dot(self, other):
        if self.len != other.len:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        sum = 0
        for i in range(self.len):
            sum += self[i] * other[i]

        return sum
    
def dot(x, y):
    assert isinstance(x, Vector) and isinstance(y, Vector)
    
    return x.dot(y)