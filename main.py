from models.produk import Produk
from models.inventaris import Inventaris

def main():
    inv = Inventaris()

    while True:
        print("\n=== SISTEM INVENTARIS TOKO ===")
        print("1. Tambah Barang")
        print("2. Cari Barang")
        print("3. Hapus Barang")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == '1':
            id_produk = input("ID Produk: ")
            nama = input ("Nama: ")
            harga = input ("Harga: ")
            stok = input("Stok: ")

            brg = Produk(id_produk, nama, harga, stok)
            if inv.tambah_produk(brg):
                print(">> Barang berhasil ditambah!")
            else:
                print(">> Gagal, ID udah terdaftar.")

        elif pilih == '2':
            id_produk = input("Masukkan ID yg dicari: ")
            hasil = inv.cari_produk(id_produk)
            if hasil:
                print(">> Ditemukan: ", hasil)
            else:
                print(">> Barang ga ketemu.")

        elif pilih == '3':
            id_produk = input("Masukkan ID yg mau dihapus: ")
            if inv.hapus_produk(id_produk):
                print(">> Barang  berhasil dihapus!")
            else:
                print(">> Gagal, ID ga ketemu.")

        elif pilih == '0':
            print("Program selesai.")
            break
        else:
            print(">> Pilihan salah.")

if __name__ == "__main__":
    main()