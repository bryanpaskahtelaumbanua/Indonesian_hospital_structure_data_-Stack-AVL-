import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

#Loading the dataset
data = pd.read_csv('C://Users//Bryan//OneDrive - Institut Teknologi Sumatera//TUBES_STRUKDAT//Hospital_Indonesia_datasets.csv', sep= ';')
print("===================================Data loaded successfully!===================================")
print(data.columns)
data = data.rename(columns = {
    'id': 'hospital_id',
    'nama': 'hospital_name',
    'propinsi' : 'province',
    'kab' : 'city',
    'alamat' : 'address',
    'jenis' : 'hospital_type',
    'kelas' : 'hospital_class',
    'status_blu' : 'blu_status',
    'kepemilikan' : 'ownership',
    'total_tempat_tidur' : 'total_beds',
    'total_layanan' : 'total_services',
    'total_tenaga_kerja' : 'total_staff'
})

print(data.head())
print(data.info())
print(data.describe())

#Handling missing values
print("\n===================================Check for missing values: ===================================")
print(data.isnull().sum())

#Handling duplicate values
print("\n===================================Check for duplicate values: ===================================")
print(data.duplicated().sum())

#Exploratory Data Analysis (EDA)
print("\n===================================Analyzing unique values in 'hospital_id' column===================================")
print(data['hospital_id'].nunique())

print("\n===================================Cleaning Data===================================")
#Hospital type
valid_type = [
    'Rumah Sakit Umum',
    'Rumah Sakit Khusus Ibu dan Anak',
    'Rumah Sakit Khusus Jiwa',
    'Rumah Sakit Khusus Mata',
    'Rumah Sakit Khusus Gigi dan Mulut',
    'Rumah Sakit Khusus Bedah',
    'Rumah Sakit Khusus Jantung',
    'Rumah Sakit Khusus Paru',
    'Rumah Sakit Khusus Orthopedi',
    'Rumah Sakit Khusus Kanker',
    'Rumah Sakit Khusus THT-KL',
    'Rumah Sakit Khusus Infeksi',
    'Rumah Sakit Khusus Ginjal',
    'Rumah Sakit Khusus Stroke',
    'Rumah Sakit Khusus Otak',
    'Rumah Sakit Ketergantungan Obat',
    'RS Kapal/Bergerak'
]

data = data[
    data['hospital_type'].isin(valid_type)
]

#Hospital class
valid_class = ['A', 'B', 'C', 'D', 'D PRATAMA']

data = data[
    data['hospital_class'].isin(valid_class)
]

#BLU status
valid_blu = ['BLU', 'BLUD', 'Non BLU/BLUD']

data = data[
    data['blu_status'].isin(valid_blu)
]

#Ownership
invalid_owner = ['BLU', 'BLUD', 'Non BLU/BLUD']

data = data[
    ~data['ownership'].isin(invalid_owner)
]

print("\nAfter cleaning:")
print(data.shape)

print("\n===================================Analyzing distribution of column in dataset===================================")
print(data['hospital_type'].value_counts())
print(data['hospital_class'].value_counts())
print(data['blu_status'].value_counts())
print(data['ownership'].value_counts())

print("\n===================================Visualizing Distribution===================================")
#By province
province_count = data['province'].value_counts().reset_index()
province_count.columns = ['province', 'total_hospitals']

gdf = gpd.read_file(
    'C://Users//Bryan//OneDrive - Institut Teknologi Sumatera//TUBES_STRUKDAT//indonesia.geojson'
)

print(gdf.columns)

merged = gdf.merge(
    province_count,
    left_on='state',
    right_on='province',
    how='left'
)

merged['total_hospitals'] = merged['total_hospitals'].fillna(0)

fig, ax = plt.subplots(
    figsize=(20,8),
    facecolor='white'
)

ax.set_facecolor('white')

merged.plot(
    column='total_hospitals',
    cmap='OrRd',
    scheme='quantiles',
    k=5,
    legend=True,
    edgecolor='black',
    linewidth=0.5,
    ax=ax
)

plt.title(
    'Distribusi Rumah Sakit di Indonesia Berdasarkan Provinsi',
    fontsize=18,
    fontweight='bold'
)

plt.axis('off')
plt.show()

#By hospital type
plt.figure(figsize=(12,6))

data['hospital_type'].value_counts().plot(
    kind='barh',
    color='skyblue'
)

plt.xscale('log')

plt.title(
    'Distribusi Tipe Rumah Sakit',
    fontsize=16,
    fontweight='bold'
)

plt.xlabel('Jumlah Rumah Sakit (Log Scale)')
plt.ylabel('Tipe Rumah Sakit')

plt.tight_layout()
plt.show()

#By hospital class
plt.figure(figsize=(7,7))

data['hospital_class'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title(
    'Distribusi Kelas Rumah Sakit',
    fontsize=16,
    fontweight='bold'
)

plt.ylabel('')

plt.show()

#By BLU status
plt.figure(figsize=(7,7))

data['blu_status'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title(
    'Distribusi Status BLU',
    fontsize=16,
    fontweight='bold'
)

plt.ylabel('')

plt.show()

#By ownership
plt.figure(figsize=(12,8))

data['ownership'].value_counts().plot(
    kind='barh',
    color='orange'
)

plt.title(
    'Distribusi Kepemilikan Rumah Sakit',
    fontsize=16,
    fontweight='bold'
)

plt.xlabel('Jumlah Rumah Sakit')
plt.ylabel('Kepemilikan')

plt.tight_layout()
plt.show()

print("\n===================================SAVE CLEANED DATASET===================================")
data.to_csv(
    'C://Users//Bryan//OneDrive - Institut Teknologi Sumatera//TUBES_STRUKDAT//Hospital_Indonesia_Cleaned.csv',
    index=False
)

print("Cleaned dataset saved successfully!")