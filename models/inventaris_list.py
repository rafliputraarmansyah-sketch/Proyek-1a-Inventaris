from .produk import Produk

class InventarisList:
    def __init__(self):
        self.data_produk = [] # pakek list biasa untuk versi yg lambatnya O(N)

    def tambah_produk(self, produk):
        for p in self.data_produk:
            if p.id_produk == produk.id_produk:
                return False
        self.data_produk.append(produk)
        return True

    def cari_produk(self, id_produk):
        for p in self.data_produk:
            if p.id_produk == id_produk:
                return p
        return None

    def hapus_produk(self, id_produk):
        for i in range(len(self.data_produk)):
            if self.data_produk[i].id_produk == id_produk:
                self.data_produk.pop(i)
                return True
        return False