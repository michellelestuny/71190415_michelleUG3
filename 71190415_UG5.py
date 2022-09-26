class Mobil:
    merk = ''
    tipe = ''
    kapasitasBBM = 0.0
    jenisbahanbakar = 'None'
    isi = ''
    def __init__(self,merkk,tipee):
        self.merk = merkk
        self.tipe = tipee
    def setMerk(self,merk):
        self.merk = merkk
    def setTipe(self,tipe):
        self.tipe = tipee
    def setKapasitas(self,kapasitasBBM):
        self.kapasitasBBM = kapasitasBBM
    def setJenis(self,jenisbahanbakar):
        self.jenisbahanbakar = jenisbahanbakar
    def getMerk(self):
        return self.merk
    def getTipe(self):
        return self.tipe
    def getKapasitas(self):
        return self.kapasitasBBM
    def getJenis(self):
        return self.jenisbahanbakar
    def isiBBM(self,isii):
        if self.getJenis() == 0 and self.getKapasitas() == 0:
            print('ERORRRR!! belum ada inputan jenis bahan bakar dan kapasitsas BBM')
        else:
            print('Total pembayaran: ', str(self.getKapasitas() * isii))
    def  printInfo(self):
        print('=========Info=======\n','merk: ', self.getMerk(), '\ntipe :', self.getTipe(),'\nBahan Bakar: ', self.getJenis(), '\nKapasitas BBM: ', self.getKapasitas())
if __name__ == '__main__':
    mobil1 = Mobil('Toyota','avanza')
    mobil1.printInfo()
    mobil2 = Mobil('Nissan','Grand Livina')
    mobil2.setJenis('bensin')
    mobil2.setKapasitas(20)
    mobil2.printInfo()
    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)