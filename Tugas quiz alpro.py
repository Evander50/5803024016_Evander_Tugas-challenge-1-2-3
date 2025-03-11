def get_first_item(items):
    return items[0]  


my_list = [10, 20, 30, 40]
print(get_first_item(my_list))

def total_belanja_linear(items):
    total = 0
    for item in items:
        total += item
    return total


def find_pairs(items):
    n = len(items)
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if items[i] == items[j]:
                pairs += 1
    return pairs


belanja = [5, 10, 15, 20]
print("Total belanja (O(n)):", total_belanja_linear(belanja))  
print("Jumlah pasangan sama (O(n²)):", find_pairs(belanja))  

def hitung_total_belanja(harga_barang):
    total = 0
    for harga in harga_barang:
        total += harga
    return to

daftar_belanja = [5000, 7500, 3000, 12000]  
total = hitung_total_belanja(daftar_belanja)
print(f"Total belanja: Rp {total}") 