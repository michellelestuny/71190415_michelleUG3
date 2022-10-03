class nodetabungan:
    def __init__(self, no_rekening, nama, saldo):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None
class SLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def _len_ (self):
        return self._size
    def isEmpty (self):
        return self.size == 0
    def insert_head(self, no_rekening, nama, saldo):
        baru = nodetabungan(no_rekening, nama, saldo)
        if self.isEmpty():
            self.no_rekening = baru
            self.nama = baru
            self.saldo = baru
        else:
            baru.next = self.head
            self.head = baru
        self.size += 1
    def filter(self, saldo):
        baru = nodetabungan(None, None, saldo)
        if self.isEmpty() == True:
            return None
        else:
            if self.saldo == baru and self.saldo <= baru:
                return self.saldo == None
    def delete(self, no_rekening, nama, saldo):
        baru = nodetabungan(no_rekening, nama, saldo)
        if self.isEmpty() == True:
            return None
        else:
            if baru == self.head:
                hapus =  self.head
                self.head = self.head.next
                del hapus
            else:
                del baru
            self.size -= 1
    def update(self, saldo):
        baru = nodetabungan(None, None, saldo)
        if self.isEmpty() == True:
            return None
        else:
            if baru == 0 and baru >= 100:
                self.update = baru / 100 * self.saldo
                return self.update
            else:
                print("Maaf besaran persen harus diantara 0-100")
    def print(self):
        bantu = self.head
        while bantu != None:
            print('no rekening: ', bantu.no_rekening, '\nnama: ', bantu.nama, '\nsaldo: ', bantu.saldo)
            bantu = bantu.next
            
slnc = SLNC()
slnc.insert_head(201,'hanif',250000)
slnc.insert_head(110,'yudha',150000)
slnc.print()
slnc.filter(150000)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()