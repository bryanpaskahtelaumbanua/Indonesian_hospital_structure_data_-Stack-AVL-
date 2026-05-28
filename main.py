import pandas as pd
from AVL_Tree import AVLTree
from Stack import Stack

data = pd.read_csv(
    "C://Users//Bryan//OneDrive - Institut Teknologi Sumatera//TUBES_STRUKDAT//Hospital_Indonesia_Cleaned.csv"
)

avl = AVLTree()
root = None
history_stack = Stack(100)

for _, row in data.iterrows():
    root = avl.insert(root, row.to_dict())

def search_by_name(data, keyword):
    return data[
        data["hospital_name"].str.contains(keyword, case=False, na=False)
    ]

while True:
    print("\n===================================")
    print("SISTEM DATA RUMAH SAKIT INDONESIA")
    print("===================================")
    print("1. Create / Insert Rumah Sakit")
    print("2. Read / Search Rumah Sakit")
    print("3. Update Rumah Sakit")
    print("4. Delete Rumah Sakit")
    print("5. Undo Last Operation")
    print("6. Lihat History Stack")
    print("7. Inorder Traversal")
    print("8. Preorder Traversal")
    print("9. Postorder Traversal")
    print("10. Exit")

    choice = input("Pilih menu: ")

    if choice == "1":
        new_data = {
            "hospital_id": int(input("Hospital ID: ")),
            "hospital_name": input("Nama Rumah Sakit: "),
            "province": input("Provinsi: "),
            "city": input("Kota/Kabupaten: "),
            "address": input("Alamat: "),
            "hospital_type": input("Tipe RS: "),
            "hospital_class": input("Kelas RS: "),
            "blu_status": input("Status BLU: "),
            "ownership": input("Kepemilikan: "),
            "total_beds": int(input("Total Tempat Tidur: ")),
            "total_services": int(input("Total Layanan: ")),
            "total_staff": int(input("Total Tenaga Kerja: "))
        }

        root = avl.insert(root, new_data)

        history_stack.push({
            "operation": "INSERT",
            "data": new_data
        })

        print("Data berhasil ditambahkan.")

    elif choice == "2":
        keyword = input("Masukkan nama rumah sakit: ")
        result = search_by_name(data, keyword)

        if not result.empty:
            print(result)
        else:
            print("Nama tidak ditemukan di dataset awal.")

        hospital_id = int(input("\nMasukkan hospital_id untuk detail AVL: "))
        hospital = avl.search(root, hospital_id)

        if hospital:
            print("\nData ditemukan:")
            for key, value in hospital.items():
                print(f"{key}: {value}")
        else:
            print("Data tidak ditemukan.")

    elif choice == "3":
        hospital_id = int(input("Masukkan hospital_id yang ingin diupdate: "))
        old_data = avl.search(root, hospital_id)

        if old_data:
            old_data_copy = old_data.copy()

            print("\nKosongkan input jika tidak ingin mengubah data.")

            updated_data = {}

            hospital_name = input("Nama baru: ")
            province = input("Provinsi baru: ")
            city = input("Kota/Kabupaten baru: ")
            address = input("Alamat baru: ")
            hospital_type = input("Tipe RS baru: ")
            hospital_class = input("Kelas RS baru: ")
            blu_status = input("Status BLU baru: ")
            ownership = input("Kepemilikan baru: ")
            total_beds = input("Total Tempat Tidur baru: ")
            total_services = input("Total Layanan baru: ")
            total_staff = input("Total Tenaga Kerja baru: ")

            if hospital_name:
                updated_data["hospital_name"] = hospital_name
            if province:
                updated_data["province"] = province
            if city:
                updated_data["city"] = city
            if address:
                updated_data["address"] = address
            if hospital_type:
                updated_data["hospital_type"] = hospital_type
            if hospital_class:
                updated_data["hospital_class"] = hospital_class
            if blu_status:
                updated_data["blu_status"] = blu_status
            if ownership:
                updated_data["ownership"] = ownership
            if total_beds:
                updated_data["total_beds"] = int(total_beds)
            if total_services:
                updated_data["total_services"] = int(total_services)
            if total_staff:
                updated_data["total_staff"] = int(total_staff)

            avl.update(root, hospital_id, updated_data)

            history_stack.push({
                "operation": "UPDATE",
                "old_data": old_data_copy,
                "new_data": updated_data
            })

            print("Data berhasil diupdate.")
        else:
            print("Data tidak ditemukan.")

    elif choice == "4":
        hospital_id = int(input("Masukkan hospital_id yang ingin dihapus: "))
        deleted_data = avl.search(root, hospital_id)

        if deleted_data:
            history_stack.push({
                "operation": "DELETE",
                "data": deleted_data.copy()
            })

            root = avl.delete(root, hospital_id)
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    elif choice == "5":
        if history_stack.is_empty():
            print("Tidak ada operasi untuk di-undo.")
        else:
            last_operation = history_stack.pop()
            operation = last_operation["operation"]

            if operation == "INSERT":
                hospital_id = last_operation["data"]["hospital_id"]
                root = avl.delete(root, hospital_id)
                print("Undo INSERT berhasil.")

            elif operation == "DELETE":
                root = avl.insert(root, last_operation["data"])
                print("Undo DELETE berhasil.")

            elif operation == "UPDATE":
                old_data = last_operation["old_data"]
                hospital_id = old_data["hospital_id"]
                avl.update(root, hospital_id, old_data)
                print("Undo UPDATE berhasil.")

    elif choice == "6":
        print("\nHistory Stack:")
        history_stack.display()

    elif choice == "7":
        print("\nInorder Traversal:")
        inorder_data = avl.inorder(root)

        for hospital in inorder_data[:20]:
            print(
                hospital["hospital_id"],
                "-",
                hospital["hospital_name"]
            )

    elif choice == "8":
        print("\nPreorder Traversal:")
        avl.preorder(root)
        print()

    elif choice == "9":
        print("\nPostorder Traversal:")
        avl.postorder(root)
        print()

    elif choice == "10":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid.")