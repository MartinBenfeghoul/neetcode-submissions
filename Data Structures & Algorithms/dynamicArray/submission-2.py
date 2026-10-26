class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None for i in range(capacity)]
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        size = self.getSize()
        capacity = self.getCapacity()
        if size == capacity:
            self.resize()
        self.set(size, n)
        print(self.arr)

    def popback(self) -> int:
        size = self.getSize()
        n = self.get(size-1)
        self.set(size-1, None)
        return n

    def resize(self) -> None:
        self.arr = self.arr + [None for i in range(self.capacity)]
        self.capacity *= 2

    def getSize(self) -> int:
        return sum(1 if n is not None else 0 for n in self.arr)
    
    def getCapacity(self) -> int:
        return self.capacity
