# Sistem Pengelolaan Data Rumah Sakit Indonesia Menggunakan AVL Tree dan Stack

## Deskripsi Proyek

Proyek ini merupakan implementasi struktur data **AVL Tree** dan **Stack** dalam sistem pengelolaan data rumah sakit di Indonesia. Dataset yang digunakan berisi informasi rumah sakit seperti nama rumah sakit, lokasi, tipe rumah sakit, kelas rumah sakit, jumlah tempat tidur, layanan, dan tenaga kerja.

AVL Tree digunakan sebagai struktur utama penyimpanan data untuk mendukung proses pencarian, penambahan, penghapusan, dan pembaruan data secara efisien dengan kompleksitas rata-rata `O(log n)`.

Stack digunakan untuk menyimpan riwayat operasi CRUD sehingga sistem dapat melakukan fitur **Undo** menggunakan konsep **LIFO (Last In First Out)**.

---

# Dataset

Dataset yang digunakan:

**Hospital Data in Indonesia**

Dataset berisi:

* Nama rumah sakit
* Provinsi
* Kota/Kabupaten
* Alamat
* Tipe rumah sakit
* Kelas rumah sakit
* Status BLU
* Kepemilikan
* Total tempat tidur
* Total layanan
* Total tenaga kerja

Jumlah data setelah preprocessing:

* ±3148 data rumah sakit

---

# Struktur Folder Proyek

```
└── Hospital_Indonesia_Cleaned.csv
└── avl_tree.py
└── stack.py
└── data_preprocessing.py
└── main.py
└── README.md
```

---

# Pipeline Sistem

## 1. Data Preprocessing

Tahapan preprocessing dilakukan untuk membersihkan dataset sebelum digunakan pada AVL Tree.

Proses preprocessing meliputi:

* Rename nama kolom
* Pengecekan missing values
* Pengecekan duplicate values
* Filtering kategori tidak valid
* Membersihkan noise pada:

  * `hospital_type`
  * `hospital_class`
  * `blu_status`
  * `ownership`

Dataset hasil preprocessing disimpan menjadi:

```text
Hospital_Indonesia_Cleaned.csv
```

---

## 2. Exploratory Data Analysis (EDA)

EDA dilakukan untuk memahami distribusi data rumah sakit di Indonesia.

Visualisasi yang dibuat:

* Distribusi rumah sakit berdasarkan provinsi
* Distribusi tipe rumah sakit
* Distribusi kelas rumah sakit
* Distribusi status BLU
* Distribusi kepemilikan rumah sakit

Visualisasi peta Indonesia menggunakan:

* `geopandas`
* `matplotlib`

---

## 3. Implementasi AVL Tree

AVL Tree digunakan sebagai struktur utama penyimpanan data rumah sakit.

### Key AVL

```text
hospital_id
```

### Operasi AVL

* Insert
* Search
* Update
* Delete
* Inorder Traversal
* Preorder Traversal
* Postorder Traversal

---

## 4. Implementasi Stack

Stack digunakan untuk menyimpan riwayat operasi CRUD pada AVL Tree.

### Operasi Stack

* Push
* Pop
* Peek
* Is Empty
* Is Full
* Size

### Fungsi Stack

Stack digunakan untuk:

* Undo Insert
* Undo Update
* Undo Delete
---

# Integrasi Sistem

Sistem diintegrasikan melalui file:

```text
main.py
```

Alur sistem:

```text
CSV Dataset
      ↓
   main.py
   /     \
AVL Tree  Stack
```

---

# Fitur Sistem

## 1. Create / Insert Rumah Sakit

Menambahkan data rumah sakit baru ke AVL Tree.

## 2. Read / Search Rumah Sakit

Mencari data rumah sakit berdasarkan:

* nama rumah sakit
* hospital_id

## 3. Update Rumah Sakit

Mengubah data rumah sakit yang sudah ada.

## 4. Delete Rumah Sakit

Menghapus data rumah sakit dari AVL Tree.

## 5. Undo Last Operation

Membatalkan operasi CRUD terakhir menggunakan Stack.

## 6. Inorder Traversal

Menampilkan data rumah sakit secara terurut berdasarkan `hospital_id`.

## 7. Preorder Traversal

Menampilkan struktur AVL Tree setelah balancing.

## 8. Postorder Traversal

Traversal AVL dengan urutan:

* Left
* Right
* Root

## 9. Lihat History Stack

Menampilkan isi Stack riwayat operasi.

---

# Cara Menjalankan Program

## 1. Install Dependency

```bash
pip install pandas matplotlib geopandas
```

---

## 2. Jalankan Program

```bash
python main.py
```

---

# Contoh Menu Sistem

```text
===================================
SISTEM DATA RUMAH SAKIT INDONESIA
===================================
1. Create / Insert Rumah Sakit
2. Read / Search Rumah Sakit
3. Update Rumah Sakit
4. Delete Rumah Sakit
5. Undo Last Operation
6. Lihat History Stack
7. Inorder Traversal
8. Preorder Traversal
9. Postorder Traversal
10. Exit
```

---

# Konsep Struktur Data yang Digunakan

## AVL Tree

AVL Tree merupakan Binary Search Tree yang menjaga keseimbangan tinggi subtree menggunakan rotasi:

* Left Rotation
* Right Rotation

AVL Tree menjaga balance factor:

```text
-1 ≤ balance factor ≤ 1
```

## Stack

Stack menggunakan konsep:

```text
LIFO (Last In First Out)
```

Operasi terakhir yang masuk ke stack akan menjadi operasi pertama yang diambil kembali untuk proses Undo.

---

# Kesimpulan

Implementasi AVL Tree memungkinkan proses pencarian dan manipulasi data rumah sakit dilakukan secara efisien dengan kompleksitas `O(log n)`.

Stack berhasil digunakan untuk menyimpan riwayat operasi CRUD sehingga sistem dapat melakukan fitur Undo dengan konsep LIFO.

Kombinasi AVL Tree dan Stack menghasilkan sistem pengelolaan data rumah sakit yang efisien, terstruktur, dan interaktif.

---

# Author

Bryan Telaumbanua
Institut Teknologi Sumatera
Program Studi Sains Data
