import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.produk import Produk
from models.inventaris import Inventaris
from models.inventaris_list import InventarisList
from models.inventaris_linked import InventarisLinkedList

def testing_waktu():
    inv_dic = Inventaris()
    inv_list = InventarisList()
    inv_linked = InventarisLinkedList()
    
    # Kita turunin jadi 20.000 aja ya, kalo 100.000 Linked List bakal lamaaa banget proses dummynya
    jumlah_data = 20000 
    print(f"Lagi generate {jumlah_data} data dummy, tunggu ntar....")
    
    for i in range(jumlah_data):
        p = Produk(f"P{i}", f"Barang {i}", 5000, 10)
        
        inv_dic.data_produk[p.id_produk] = p
        inv_list.data_produk.append(p)
        
        # Bypass cek duplikat khusus buat dummy linked list biar ga error kelamaan
        node_baru = Node(p) if 'Node' in globals() else type('Node', (), {'data': p, 'next': inv_linked.head})()
        inv_linked.head = node_baru
    
    target_id = "P0" # Di linked list karena kita insert di depan, data pertama (P0) jadi yg paling ujung belakang
    
    print("\n--- TEST WAKTU SEARCHING ---")
    
    start = time.perf_counter()
    inv_list.cari_produk(target_id)
    print(f"Pake Array List  (O(N)) : {time.perf_counter() - start:.6f} detik")

    start = time.perf_counter()
    inv_linked.cari_produk(target_id)
    print(f"Pake Linked List (O(N)) : {time.perf_counter() - start:.6f} detik")
    
    start = time.perf_counter()
    inv_dic.cari_produk(target_id)
    print(f"Pake Dictionary  (O(1)) : {time.perf_counter() - start:.6f} detik")

if __name__ == "__main__":
    testing_waktu()