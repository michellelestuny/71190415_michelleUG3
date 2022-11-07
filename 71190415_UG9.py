class Node:
    def __init__(self,data,priority):
        self._data = data
        self._priority = priority
class PriorityQueueSortedList:
    def __init__(self):
        pass
        self._queue = []
        self._size = 0
        self._front = 0
    def __str__(self):
            return ' '.join([str(i) for i in self.queue])
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    def __len__(self):
        return self._size
    def add(self, data, priority):
        pass
        baru = Node(data, priority)
        if self.is_empty():
            self._queue.append(data, priority)
        elif self._size == 1:
     # isinya cuma 1, insert sebelum atau setelah head?
            if self._priority._front(0) > priority:
     # insert sebelum head
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            else:
    # insert setelah head
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
        else:
    # cek apakah harus insert depan?
            if self._priority.index(0) > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
# cek apakah harus insert belakang?
            elif self._tail._priority <= priority:
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None
            else:
    # berarti insert di tengah
# letakkan bantu di posisi setelah insertion point
                bantu = self._head
                while bantu._priority < priority:
                    bantu = bantu._next
                 # gunakan bantu2 di posisi sebelum insertion point
                bantu2 = bantu._prev
                baru._next = bantu
                bantu._prev = baru
                bantu2._next = baru
                baru._prev = bantu2
        self._size += 1
    def peek(self,data,priority):
        pass
        if self.is_empty() == True:
                return None
        else:
            return tuple([self._head._data, self._head._priority])
    def update(priobaru, databaru):
        pass
    def remove(self):
        pass
        if self.is_empty() == False:
            answer = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            return answer

        if self._size == 1:
            self._head = None
        else:
            None
        self._size -= 1
    def removewithprio():
        pass
    def printall(self):
        pass
        if self.is_empty() == True:
                print('Priority Queue is empty')
        else:
            bantu = self._head
            while bantu != None:
                print('(', bantu._data, ',', bantu._priority, ')', end=' ')
                bantu = bantu._next
            print()
sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update("Karin", 4)
sortedList.update("Rafi", 3)
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()