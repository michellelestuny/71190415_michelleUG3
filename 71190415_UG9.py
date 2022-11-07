class PriorityQueueSortedList:

    def __init__(self):
        self._data = []
    
    def peek(self):
        print(self._data[0])

    def add(self, n, p):

        if len(self._data):

            pointer = 0
            while self._data[pointer][1] < p:
                pointer += 1

            self._data.insert(pointer, (n, p))


        else:
            self._data.append((n, p))

    def update(self, p, n):
        pointer = 0

        while self._data[pointer][1] != p:
            pointer += 1

        self._data[pointer] = (n, p)
    
    def remove(self):
        del self._data[0]

    def removePriority(self, p):
        pointer = 0

        while self._data[pointer][1] != p:
            pointer += 1
        del self._data[pointer]

    def printIsiQueue(self):
        print("Isi semua Queue: ", end="")

        for i in self._data[:-1]:
            print("{}," .format(i), end=" ")
        print("{}" .format(self._data[-1]))


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)

sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")

sortedList.remove()
sortedList.removePriority(4)

sortedList.peek()
sortedList.printIsiQueue()