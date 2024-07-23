NAMA:JENDRIADI | NIM:230401010120 |MATKUL:STRUKTUR DATA DAN ALGORITMA | KELAS:IT-201 | PRODI INFORMATIKA | UNIVERSITAS SIBER ASIA
----------------------------------------------------------------------------------------------------------------------------------
PENJELASAN PROGRAM SOAL NOMOR 1

1.Fungsi bubble_sort(data):

a.Menerima parameter data, yang merupakan list dari dictionary. Setiap dictionary memiliki dua kunci: "Nama" dan "Alamat".

b.Variabel n menyimpan panjang atau jumlah elemen dalam list data.

c.Melakukan loop dari i = 0 hingga n - 2. Iterasi ini mengontrol berapa kali perlu melakukan perbandingan dan pertukaran.

d.Variabel swapped digunakan untuk melacak apakah terjadi pertukaran selama iterasi dalam satu putaran. Jika tidak ada pertukaran yang terjadi (swapped = False), maka iterasi dihentikan lebih awal, karena elemen sudah terurut.

e.Di dalam loop luar, terdapat loop dalam (for j in range(0, n - i - 1)) yang berfungsi untuk melakukan perbandingan dan pertukaran antara dua elemen bersebelahan jika kunci "Nama" pada elemen pertama lebih besar dari kunci "Nama" pada elemen kedua.

f.Jika elemen pada posisi j lebih besar dari elemen pada posisi j + 1, maka dilakukan pertukaran elemen menggunakan teknik multiple assignment Python: data[j], data[j + 1] = data[j + 1], data[j].

g.Setelah melakukan pertukaran, swapped diatur menjadi True.

h.Jika tidak ada pertukaran yang terjadi di suatu iterasi, loop luar dihentikan menggunakan statement break, karena berarti data sudah terurut.
i.Mengembalikan data yang sudah diurutkan.

2.Inisialisasi data:

a.data adalah list yang berisi beberapa dictionary. Setiap dictionary merepresentasikan entitas dengan atribut "Nama" dan "Alamat".

3.Pemanggilan bubble_sort(data):

a.Memanggil fungsi bubble_sort dengan parameter data untuk mengurutkan list data berdasarkan kunci "Nama".

4.Output Hasil Pengurutan:

a.Setelah proses pengurutan selesai, program mencetak hasilnya dengan format tabel yang mencakup kolom "Nama" dan "Alamat" dari setiap elemen dictionary yang telah diurutkan.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PENJELASAN PROGRAM SOAL NOMOR 2

1.Fungsi binary_search(arr, x):

a.Menerima dua parameter: arr (array yang akan dicari) dan x (nilai yang ingin dicari).

b.Pertama-tama, array arr diurutkan menggunakan metode .sort() sebelum pencarian dimulai.

c.Variabel left dan right digunakan untuk menandai rentang pencarian. left diinisialisasi dengan nilai 0 (indeks awal) dan right diinisialisasi dengan panjang arr dikurangi 1 (indeks akhir).

d.Variabel result digunakan untuk menyimpan indeks-indeks di mana nilai x ditemukan dalam array arr.

2.Proses Pencarian Binary:

a.Selama left kurang dari atau sama dengan right, dilakukan iterasi.

b.Variabel mid dihitung sebagai indeks tengah dari rentang left hingga right.

c.Jika nilai di arr[mid] sama dengan x, artinya nilai x ditemukan di arr[mid]:

  1.Indeks mid ditambahkan ke dalam result.
  2.Dilakukan pencarian ke kiri dari mid untuk mencari indeks-indeks sebelumnya yang memiliki nilai x dan ditambahkan ke result.
  3.Dilakukan pencarian ke kanan dari mid untuk mencari indeks-indeks setelahnya yang memiliki nilai x dan ditambahkan ke result.
  4.Hasil result yang berisi indeks-indeks di mana nilai x ditemukan dikembalikan.
  
d.Jika arr[mid] kurang dari x, maka pencarian dilanjutkan di bagian kanan array dengan mengubah left menjadi mid + 1.

e.Jika arr[mid] lebih dari x, maka pencarian dilanjutkan di bagian kiri array dengan mengubah right menjadi mid - 1.

3.Penanganan Hasil Tidak Ditemukan:

a.Jika x tidak ditemukan setelah loop selesai, maka fungsi akan mengembalikan pesan string bahwa "Angka x tidak ada dalam array".

4.Penggunaan Fungsi:

a.Program menggunakan fungsi binary_search untuk mencari nilai x dalam array array dengan nilai yang berbeda-beda (x = 1, x = 50, dan x = 100).

b.Hasil pencarian kemudian dicetak sesuai dengan format yang ditentukan, menunjukkan apakah nilai x ditemukan dan di mana indeksnya, atau bahwa nilai x tidak ditemukan dalam array.
