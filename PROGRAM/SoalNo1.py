def bubble_sort(data):
    n = len(data)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(0, n - i - 1):
            if data[j]["Nama"] > data[j + 1]["Nama"]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        
        if not swapped:
            break
    
    return data

data = [
    {"Nama": "Fahmi", "Alamat": "Jakarta"},
    {"Nama": "Romi", "Alamat": "Solo"},
    {"Nama": "Andri", "Alamat": "Jakarta"},
    {"Nama": "Fadillah", "Alamat": "Banyuwangi"},
    {"Nama": "Ruli", "Alamat": "Bandung"},
    {"Nama": "Rudi", "Alamat": "Bali"},
    {"Nama": "Dendi", "Alamat": "Purwokerto"},
    {"Nama": "Zaki", "Alamat": "Madiun"}
]

data_sorted_bubble = bubble_sort(data)

print("Hasil pengurutan menggunakan Bubble Sort:")
print("Nama\tAlamat")
for item in data_sorted_bubble:
    print(f"{item['Nama']}\t{item['Alamat']}")
