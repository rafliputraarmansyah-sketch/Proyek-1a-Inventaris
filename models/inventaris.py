from .produk import Produk

class Inventaris:
    def __init__(self):
        self.data_produk = {} # pakek dictionary biar kompleksitasnya O(1)

    def tambah_produk(self, produk):
        if produk.id_produk in self.data_produk:
            return False # ID nya tu udah ada

        self.data_produk[produk.id_produk] = produk
        return True

    def cari_produk(self, id_produk):
        return self.data_produk.get(id_produk)

    def hapus_produk(self, id_produk):
        if id_produk in self.data_produk:
            del self.data_produk[id_produk]
            return True
        return False