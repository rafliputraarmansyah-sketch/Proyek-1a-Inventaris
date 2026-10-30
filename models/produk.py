class Produk:
    def __init__(self, id_produk, nama, harga, stok):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"{self.id_produk} | {self.nama} | Rp{self.harga} | Stok: {self.stok}"