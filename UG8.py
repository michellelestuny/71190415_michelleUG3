class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = "" #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
       self.size = size
       self.queue = [None for i in range(size)]
       self.front = self.rear = -1
       
    def __len__(self): #mengembalikan ukuran Queue
        pass
        return self._size

    def is_empty(self): #mengecek apakah Queue kosong ?
        pass
        return self._size == 0

    def dequeue(self): #menghapus data paling depan (front)
        pass
        if (self.front == -1):
            print("Antrian kosong")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def enqueue(self, namaPelanggan): #menambah data ke list
        pass
        if ((self.rear + 1) % self.size == self.front):
            print(" Antrian penuh")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def resize(self, cap): #mengubah ukuran queue pada list
        pass
        # tulis kode anda di sini
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        pass
        if (self.front == -1):
            print("Antrian kosong")
        elif (self.rear >= self.front):
            print("Yang ada pada antrian adalah:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Yang ada pada antrian adalah:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Antrian penuh")
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

