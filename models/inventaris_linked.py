from .produk import Produk

# Linked list butuh "Node" untuk nyimpen data dan link ke data berikutnya
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class InventarisLinkedList:
    def __init__(self):
        self.head = None # Kepala dari linked list

    def tambah_produk(self, produk):
        # Cek duplikat dulu (harus ngecek satu-satu = O(N))
        temp = self.head
        while temp:
            if temp.data.id_produk == produk.id_produk:
                return False 
            temp = temp.next
        
        # Kalo ga ada duplikat, tambahin di paling depan biar cepet
        node_baru = Node(produk)
        node_baru.next = self.head
        self.head = node_baru
        return True

    def cari_produk(self, id_produk):
        temp = self.head
        while temp: # Pencarian lambat O(N)
            if temp.data.id_produk == id_produk:
                return temp.data
            temp = temp.next
        return None

    def hapus_produk(self, id_produk):
        temp = self.head
        prev = None
        
        while temp: # Penghapusan lambat O(N) karena harus dicari dulu
            if temp.data.id_produk == id_produk:
                if prev:
                    prev.next = temp.next # Hapus di tengah/akhir
                else:
                    self.head = temp.next # Hapus di depan
                return True
            prev = temp
            temp = temp.next
            
        return False