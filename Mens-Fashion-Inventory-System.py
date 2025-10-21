from tabulate import tabulate

products = [
    {"id": 1, "name": "Kemeja Formal Putih", "category": "Kemeja", "size": "L", "brand": "Executive", "price": 189000, "stock": 20},
    {"id": 2, "name": "Kaos Polo", "category": "Kaos", "size": "M", "brand": "LaCoste", "price": 450000, "stock": 15},
    {"id": 3, "name": "Celana Chino", "category": "Celana", "size": "32", "brand": "Uniqlo", "price": 399000, "stock": 25},
    {"id": 4, "name": "Jaket Bomber", "category": "Jaket", "size": "XL", "brand": "Alpha", "price": 650000, "stock": 10},
    {"id": 5, "name": "Jeans Slim Fit", "category": "Celana", "size": "34", "brand": "Levi's", "price": 599000, "stock": 18},
    {"id": 6, "name": "Hoodie Gaming", "category": "Hoodie", "size": "L", "brand": "Razer", "price": 550000, "stock": 12},
    {"id": 7, "name": "Batik Modern", "category": "Kemeja", "size": "M", "brand": "Danar Hadi", "price": 350000, "stock": 8},
    {"id": 8, "name": "Tank Top Gym", "category": "Kaos", "size": "M", "brand": "Under Armour", "price": 225000, "stock": 22},
    {"id": 9, "name": "Kaos Levi's Classic", "category": "Kaos", "size": "L", "brand": "Levi's", "price": 275000, "stock": 30},
    {"id": 10, "name": "Kaos Uniqlo Premium", "category": "Kaos", "size": "M", "brand": "Uniqlo", "price": 199000, "stock": 35},
    {"id": 11, "name": "Jaket LaCoste Sport", "category": "Jaket", "size": "L", "brand": "LaCoste", "price": 890000, "stock": 8},
    {"id": 12, "name": "Jaket Under Armour Training", "category": "Jaket", "size": "XL", "brand": "Under Armour", "price": 750000, "stock": 10},
    {"id": 13, "name": "Hoodie LaCoste Premium", "category": "Hoodie", "size": "L", "brand": "LaCoste", "price": 680000, "stock": 12},
    {"id": 14, "name": "Celana Cargo Parasut", "category": "Jaket", "size": "XL", "brand": "Alpha", "price": 376000, "stock": 10},
    {"id": 15, "name": "Lacoste Slim Fit Stretch Jeans", "category": "Celana", "size": "34", "brand": "Levi's", "price": 499000, "stock": 18},
]

trash_bin = []
update_history = []
update_counter = 0
create_history = []
create_counter = 0
delete_counter = 0
# ==================== 1. MAIN PROGRAM ====================
def main():
    while True:
        print("\n" + "="*50)
        print(" "*10 + "Manajemen Inventaris Toko Pakaian Pria Varkhani")
        print("="*50)
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. EXIT PROGRAM")
        
        # Tampilkan notifikasi
        if trash_bin:
            print(f"\nTrash Bin: {len(trash_bin)} item")
        if update_history:
            print(f"Update History: {len(update_history)} perubahan")
        if create_history:
            print(f"Create History: {len(create_history)} produk ditambahkan")
        
        choice = input("\nPilih menu utama (1-5): ")
        
        if choice == "1":
            read_menu()
        elif choice == "2":
            create_menu()
        elif choice == "3":
            update_menu()
        elif choice == "4":
            delete_menu()
        elif choice == "5":
            print("\nFarewell Mas Admin!")
            break
        else:
            print("Pilihan tidak valid!")

def show_products_table(product_list):
    sorted_products = product_list.copy()
    n = len(sorted_products)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_products[j]["id"] > sorted_products[j+1]["id"]:
                sorted_products[j], sorted_products[j+1] = sorted_products[j+1], sorted_products[j]
    
    table = []
    for p in sorted_products:
        row = [p["id"], p["name"], p["category"], p["size"], 
               p["brand"], f"Rp{p['price']:,}", p["stock"]]
        table.append(row)
    
    print(tabulate(table, headers=["ID", "Nama", "Kategori", "Size", "Brand", "Harga", "Stok"], tablefmt="grid"))

def sort_products_manually(product_list, sort_by):
    sorted_list = product_list.copy()
    n = len(sorted_list)
    
    for i in range(n):
        for j in range(0, n-i-1):
            ganti_posisi = False
            
            if sort_by == "id":
                if sorted_list[j]["id"] > sorted_list[j+1]["id"]:
                    ganti_posisi = True
            elif sort_by == "name":
                if sorted_list[j]["name"].lower() > sorted_list[j+1]["name"].lower():
                    ganti_posisi = True
            elif sort_by == "category":
                if sorted_list[j]["category"].lower() > sorted_list[j+1]["category"].lower():
                    ganti_posisi = True
            elif sort_by == "brand":
                if sorted_list[j]["brand"].lower() > sorted_list[j+1]["brand"].lower():
                    ganti_posisi = True
            elif sort_by == "price":
                if sorted_list[j]["price"] > sorted_list[j+1]["price"]:
                    ganti_posisi = True
            elif sort_by == "stock":
                if sorted_list[j]["stock"] > sorted_list[j+1]["stock"]:
                    ganti_posisi = True
            
            if ganti_posisi:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    return sorted_list

# ==================== 2. READ MENU ====================
def read_menu():
    while True:
        print("\nMENU LIHAT PRODUK")
        print("-" * 35)
        print("1. Tampilkan Seluruh Data Produk")
        print("2. Tampilkan Produk Tertentu by id (Satu Produk)")
        print("3. Tampilkan Sort Semua Produk by Kategori")
        print("4. Tampilkan Sort Semua Produk by Brand")
        print("5. Kembali ke Menu Utama")
        
        sub_choice = input("\nPilih sub-menu (1-5): ")
        
        if sub_choice == "1":
            read_all_products()
        elif sub_choice == "2":
            read_specific_product()
        elif sub_choice == "3":
            sort_products_by_category()
        elif sub_choice == "4":
            sort_products_by_brand()
        elif sub_choice == "5":
            print("Kembali ke menu utama...")
            return
        else:
            print("Pilihan tidak valid!")

def read_all_products():
    print("\nSELURUH DATA PRODUK AKTIF")
    print("-" * 50)
    
    if not products:
        print("Tidak ada produk tersedia")
        if trash_bin:
            print(f"Ada {len(trash_bin)} produk di Trash Bin")
        return
    
    print("\nOPSI SORTING:")
    print("1. Sort by ID (Default)")
    print("2. Sort by Nama")
    print("3. Sort by Kategori")
    print("4. Sort by Brand")
    print("5. Sort by Harga (Termurah)")
    print("6. Sort by Harga (Termahal)")
    print("7. Sort by Stok (Terkecil)")
    print("8. Sort by Stok (Terbesar)")
    
    sort_choice = input("\nPilih sorting (Enter untuk default): ")
    
    if sort_choice == "2":
        sorted_products = sort_products_manually(products, "name")
        sort_info = "Sorted by: Nama"
    elif sort_choice == "3":
        sorted_products = sort_products_manually(products, "category")
        sort_info = "Sorted by: Kategori"
    elif sort_choice == "4":
        sorted_products = sort_products_manually(products, "brand")
        sort_info = "Sorted by: Brand"
    elif sort_choice == "5":
        sorted_products = sort_products_manually(products, "price")
        sort_info = "Sorted by: Harga (Termurah)"
    elif sort_choice == "6":
        sorted_products = sort_products_manually(products, "price")
        sorted_products.reverse()
        sort_info = "Sorted by: Harga (Termahal)"
    elif sort_choice == "7":
        sorted_products = sort_products_manually(products, "stock")
        sort_info = "Sorted by: Stok (Terkecil)"
    elif sort_choice == "8":
        sorted_products = sort_products_manually(products, "stock")
        sorted_products.reverse()
        sort_info = "Sorted by: Stok (Terbesar)"
    else:
        sorted_products = sort_products_manually(products, "id")
        sort_info = "Sorted by: ID (Default)"
    
    table_data = []
    for p in sorted_products:
        row = [p["id"], p["name"], p["category"], p["size"], 
               p["brand"], f"Rp {p['price']:,}", p["stock"]]
        table_data.append(row)
    
    headers = ["ID", "Nama Produk", "Kategori", "Size", "Brand", "Harga", "Stok"]
    print(f"\n{sort_info}")
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    
    total_value = 0
    for p in products:
        total_value += p["price"] * p["stock"]
    
    print(f"\nTotal: {len(products)} produk aktif | Nilai: Rp {total_value:,}")
    
    if trash_bin:
        print(f"Trash Bin: {len(trash_bin)} item")

def read_specific_product():
    print("\nCARI PRODUK TERTENTU")
    
    try:
        product_id = int(input("Masukkan ID produk: "))
    except:
        print("ID harus berupa angka!")
        return
    
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    
    if product:
        print("\nPRODUK DITEMUKAN (Status: AKTIF)")
        details = [
            ["ID", product["id"]],
            ["Nama", product["name"]],
            ["Kategori", product["category"]],
            ["Size", product["size"]],
            ["Brand", product["brand"]],
            ["Harga", f"Rp {product['price']:,}"],
            ["Stok", product["stock"]],
            ["Status", "Aktif"]
        ]
        print(tabulate(details, headers=["Field", "Value"], tablefmt="grid"))
    else:
        in_trash = None
        for p in trash_bin:
            if p["id"] == product_id:
                in_trash = p
                break
        
        if in_trash:
            print("\nPRODUK ADA DI TRASH BIN!")
            details = [
                ["ID", in_trash["id"]],
                ["Nama", in_trash["name"]],
                ["Kategori", in_trash["category"]],
                ["Status", "Di Trash Bin"],
                ["Delete Order", in_trash.get("delete_order", "Unknown")]
            ]
            print(tabulate(details, headers=["Field", "Value"], tablefmt="grid"))
            print("\nGunakan menu DELETE > Manage Trash Bin > Restore untuk mengembalikan")
        else:
            print("\nDATA PRODUK TIDAK VALID!")
            print(f"Produk dengan ID {product_id} tidak ditemukan.")

def sort_products_by_category():
    print("\nPRODUK SORTED BY KATEGORI")
    print("-" * 50)
    
    if not products:
        print("Tidak ada produk tersedia")
        return
    
    sorted_products = sort_products_manually(products, "category")
    
    current_category = None
    category_count = {}
    category_value = {}
    
    for p in sorted_products:
        cat = p["category"]
        if cat not in category_count:
            category_count[cat] = 0
            category_value[cat] = 0
        category_count[cat] += 1
        category_value[cat] += p["price"] * p["stock"]
    
    for p in sorted_products:
        if current_category != p["category"]:
            if current_category is not None:
                print()
            
            current_category = p["category"]
            print(f"\nKATEGORI: {current_category}")
            print(f"Total: {category_count[current_category]} produk | Nilai: Rp {category_value[current_category]:,}")
            print("-" * 80)
            
            headers = ["ID", "Nama", "Size", "Brand", "Harga", "Stok"]
            category_products = []
            for prod in sorted_products:
                if prod["category"] == current_category:
                    category_products.append([
                        prod["id"],
                        prod["name"],
                        prod["size"],
                        prod["brand"],
                        f"Rp {prod['price']:,}",
                        prod["stock"]
                    ])
            
            print(tabulate(category_products, headers=headers, tablefmt="simple"))
    
    print("\n" + "="*50)
    print("Urutan produk berdasarkan kategori:")
    summary_table = []
    for cat in sorted(category_count.keys()):
        summary_table.append([
            cat,
            category_count[cat],
            f"Rp {category_value[cat]:,}"
        ])
    
    print(tabulate(summary_table, headers=["Kategori", "Jumlah Produk", "Total Nilai"], tablefmt="grid"))
    
    total_products = len(products)
    total_value = sum(p["price"] * p["stock"] for p in products)
    print(f"\nGRAND TOTAL: {total_products} produk | Nilai: Rp {total_value:,}")

def sort_products_by_brand():
    print("\nPRODUK SORTED BY BRAND")
    print("-" * 50)
    
    if not products:
        print("Tidak ada produk tersedia")
        return
    
    sorted_products = sort_products_manually(products, "brand")
    
    current_brand = None
    brand_count = {}
    brand_value = {}
    brand_categories = {}
    
    for p in sorted_products:
        brand = p["brand"]
        if brand not in brand_count:
            brand_count[brand] = 0
            brand_value[brand] = 0
            brand_categories[brand] = []
        
        brand_count[brand] += 1
        brand_value[brand] += p["price"] * p["stock"]
        
        if p["category"] not in brand_categories[brand]:
            brand_categories[brand].append(p["category"])
    
    for p in sorted_products:
        if current_brand != p["brand"]:
            if current_brand is not None:
                print()
            
            current_brand = p["brand"]
            categories_list = ", ".join(brand_categories[current_brand])
            
            print(f"\n BRAND: {current_brand}")
            print(f"Kategori: {categories_list}")
            print(f"Total: {brand_count[current_brand]} produk | Nilai: Rp {brand_value[current_brand]:,}")
            print("-" * 80)
            
            headers = ["ID", "Nama", "Kategori", "Size", "Harga", "Stok"]
            brand_products = []
            for prod in sorted_products:
                if prod["brand"] == current_brand:
                    brand_products.append([
                        prod["id"],
                        prod["name"],
                        prod["category"],
                        prod["size"],
                        f"Rp {prod['price']:,}",
                        prod["stock"]
                    ])
            
            print(tabulate(brand_products, headers=headers, tablefmt="simple"))
    
    print("\n" + "="*50)
    print(" SUMMARY BY BRAND:")
    
    brand_sorted_by_value = []
    for brand in brand_count.keys():
        brand_sorted_by_value.append({
            "brand": brand,
            "count": brand_count[brand],
            "value": brand_value[brand]
        })
    
    n = len(brand_sorted_by_value)
    for i in range(n):
        for j in range(0, n-i-1):
            if brand_sorted_by_value[j]["value"] < brand_sorted_by_value[j+1]["value"]:
                brand_sorted_by_value[j], brand_sorted_by_value[j+1] = brand_sorted_by_value[j+1], brand_sorted_by_value[j]
    
    summary_table = []
    for item in brand_sorted_by_value:
        summary_table.append([
            item["brand"],
            item["count"],
            f"Rp {item['value']:,}",
            len(brand_categories[item["brand"]])
        ])
    
    print(tabulate(summary_table, headers=["Brand", "Jumlah Produk", "Total Nilai", "Jumlah Kategori"], tablefmt="grid"))
    
    max_products_brand = None
    max_count = 0
    for brand, count in brand_count.items():
        if count > max_count:
            max_count = count
            max_products_brand = brand
    
    max_value_brand = None
    max_value = 0
    for brand, value in brand_value.items():
        if value > max_value:
            max_value = value
            max_value_brand = brand
    
    print("\nTOP BRAND:")
    print(f"Produk Terbanyak: {max_products_brand} ({max_count} produk)")
    print(f"Nilai Tertinggi: {max_value_brand} (Rp {max_value:,})")
    
    total_products = len(products)
    total_value = sum(p["price"] * p["stock"] for p in products)
    print(f"\n GRAND TOTAL: {total_products} produk | Nilai: Rp {total_value:,}")

# ==================== 3. CREATE MENU ====================
def create_menu():
    while True:
        print("\nMENU TAMBAH PRODUK")
        print("-" * 35)
        print("1. Tambah Data Produk Baru (Single)")
        print("2. Clone & Modify Product")
        print("3. Bulk Add Product Variants")
        print("4. View Create History")
        print("5. Kembali ke Menu Utama")
        
        if create_history:
            print(f"\nTotal {len(create_history)} produk telah ditambahkan")
        
        sub_choice = input("\nPilih sub-menu (1-5): ")
        
        if sub_choice == "1":
            add_new_product()
        elif sub_choice == "2":
            clone_and_modify_product()
        elif sub_choice == "3":
            bulk_add_product_variants()
        elif sub_choice == "4":
            view_create_history()
        elif sub_choice == "5":
            print("Kembali ke menu utama...")
            return
        else:
            print("Pilihan tidak valid!")

def add_new_product():
    global create_counter
    try:
        new_id = int(input("\nMasukkan ID Produk (Primary Key): "))
        if new_id <= 0:
            print("ID tidak ditemukan!")
            return
    except:
        print("ID harus angka!")
        return
    
    for p in products:
        if p["id"] == new_id:
            print(f"ID {new_id} sudah dipakai oleh produk aktif: '{p['name']}'.")
            print("Gunakan ID lain atau update produk tersebut di menu UPDATE.")
            return

    for p in trash_bin:
        if p["id"] == new_id:
            print(f"ID {new_id} ada di Trash Bin untuk produk: '{p['name']}'.")
            print("Gunakan ID lain atau restore produk dari Trash di menu DELETE.")
            return

    name = input("Nama: ").strip()
    if not name:
        print("Nama tidak boleh kosong!")
        return

    category = input("Kategori: ").strip()
    if not category:
        print("Kategori tidak boleh kosong!")
        return

    size = input("Size: ").upper().strip()
    if not size:
        print("Size tidak boleh kosong!")
        return

    brand = input("Brand: ").strip()
    if not brand:
        print("Brand tidak boleh kosong!")
        return

    try:
        price = int(input("Harga: Rp "))
        stock = int(input("Stok: "))
    except:
        print("Harga/Stok harus angka!")
        return

    review = [
        ["ID (PK)", new_id],
        ["Nama", name],
        ["Kategori", category],
        ["Size", size],
        ["Brand", brand],
        ["Harga", f"Rp{price:,}"],
        ["Stok", stock]
    ]
    print("\nREVIEW DATA PRODUK BARU (Manual ID)")
    print(tabulate(review, headers=["Field","Value"], tablefmt="pretty"))

    if input("Simpan? (YA/TIDAK): ").upper() == "YA":
        products.append({
            "id": new_id,
            "name": name,
            "category": category,
            "size": size,
            "brand": brand,
            "price": price,
            "stock": stock
        })

        create_counter += 1
        create_history.append({
            "order": create_counter,
            "product_id": new_id,
            "product_name": name,
            "method": "Single Add (Manual ID)"
        })
        print("Produk ditambahkan dengan ID manual!")
    else:
        print("Batal disimpan")

def clone_and_modify_product():
    global products, create_history, create_counter
    
    if not products:
        print("Tidak ada produk untuk di-clone")
        return
    
    print("\nCLONE & MODIFY PRODUCT")
    print("-" * 40)
    print("Fitur ini memudahkan menambah variasi produk yang sudah ada")
    
    print("\n PRODUK TERSEDIA UNTUK DI-CLONE:")
    show_products_table(products)
    
    try:
        source_id = int(input("\nID produk yang akan di-clone: "))
    except:
        print("ID harus angka!")
        return
    
    source_product = None
    for p in products:
        if p["id"] == source_id:
            source_product = p
            break
    
    if not source_product:
        print(f"Produk dengan ID {source_id} tidak ditemukan!")
        return
    
    print(f"\n Produk ditemukan: {source_product['name']}")
    print("\n MODIFIKASI PRODUK CLONE")
    print("Catatan: Kosongkan untuk menggunakan nilai yang sama")
    print("-" * 50)
    
    new_id = 1
    all_ids = []
    for p in products:
        all_ids.append(p["id"])
    for p in trash_bin:
        all_ids.append(p["id"])
    if all_ids:
        new_id = max(all_ids) + 1
    
    print(f" ID Produk Clone (Otomatis): {new_id}")
    
    new_name = input(f"Nama ({source_product['name']}): ").strip()
    if not new_name:
        new_name = source_product['name']
    
    for product in products:
        if product["name"].lower() == new_name.lower():
            print(f"\n Produk dengan nama '{new_name}' sudah ada!")
            print("Saran nama:")
            print(f"- {source_product['name']} V2")
            print(f"- {source_product['name']} - Variant")
            return
    
    new_category = input(f"Kategori ({source_product['category']}): ").strip()
    if not new_category:
        new_category = source_product['category']
    
    new_size = input(f"Size ({source_product['size']}): ").strip().upper()
    if not new_size:
        new_size = source_product['size']
    
    new_brand = input(f"Brand ({source_product['brand']}): ").strip()
    if not new_brand:
        new_brand = source_product['brand']
    
    print(f"\nHarga produk asli: Rp {source_product['price']:,}")
    price_choice = input("1. Gunakan harga sama\n2. Input harga baru\nPilih (1-2): ")
    
    if price_choice == "2":
        try:
            new_price = int(input("Harga baru: Rp "))
        except:
            print("Harga tidak valid! Menggunakan harga asli.")
            new_price = source_product['price']
    else:
        new_price = source_product['price']
    
    try:
        new_stock = int(input(f"Stok ({source_product['stock']}): ") or source_product['stock'])
    except:
        new_stock = source_product['stock']
    
    print("\n PERBANDINGAN PRODUK")
    print("-" * 50)
    
    comparison_data = [
        ["Field", "Produk Asli", "Produk Clone"],
        ["ID", source_product['id'], new_id],
        ["Nama", source_product['name'], new_name],
        ["Kategori", source_product['category'], new_category],
        ["Size", source_product['size'], new_size],
        ["Brand", source_product['brand'], new_brand],
        ["Harga", f"Rp {source_product['price']:,}", f"Rp {new_price:,}"],
        ["Stok", source_product['stock'], new_stock]
    ]
    
    print(tabulate(comparison_data, headers="firstrow", tablefmt="fancy_grid"))
    
    if input("\nSimpan produk clone? (YA/TIDAK): ").upper() == "YA":
        cloned_product = {
            "id": new_id,
            "name": new_name,
            "category": new_category,
            "size": new_size,
            "brand": new_brand,
            "price": new_price,
            "stock": new_stock
        }
        
        products.append(cloned_product)
        
        create_counter += 1
        create_history.append({
            "order": create_counter,
            "product_id": new_id,
            "product_name": new_name,
            "method": f"Cloned from ID {source_id}",
            "source_product": source_product['name']
        })
        
        print(f"\n PRODUK BERHASIL DI-CLONE!")
        print(f"   ID Baru: {new_id}")
        print(f"   Nama: {new_name}")
        print(f"   Cloned from: {source_product['name']} (ID: {source_id})")
    else:
        print("Clone produk dibatalkan")

def bulk_add_product_variants():
    global products, create_history, create_counter
    
    print("\n BULK ADD PRODUCT VARIANTS")
    print("-" * 40)
    print("Fitur ini untuk menambah produk yang sama dengan variasi size")
    
    print("\n INPUT DATA PRODUK BASE")
    print("-" * 35)
    
    base_name = input("Nama Produk Base (tanpa size): ").strip()
    
    if not base_name:
        print("Nama produk tidak boleh kosong!")
        return
    
    base_category = input("Kategori: ").strip()
    base_brand = input("Brand: ").strip()
    
    try:
        base_price = int(input("Harga: Rp "))
    except:
        print("Harga tidak valid!")
        return
    
    print("\n PILIH SIZE VARIANTS")
    print("-" * 35)
    
    if "celana" in base_category.lower():
        size_options = ["28", "29", "30", "31", "32", "33", "34", "35", "36"]
        print("Size tersedia untuk Celana: 28-36")
    else:
        size_options = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
        print("Size tersedia: XS, S, M, L, XL, XXL, XXXL")
    
    print("\nPilih size yang akan ditambahkan:")
    print("Format: pisahkan dengan koma (contoh: S,M,L,XL)")
    print(f"Opsi: {', '.join(size_options)}")
    
    size_input = input("\nMasukkan size: ").upper().replace(" ", "")
    selected_sizes = size_input.split(",")
    
    valid_sizes = []
    for size in selected_sizes:
        if size:
            valid_sizes.append(size)
    
    if not valid_sizes:
        print(" Tidak ada size yang dipilih!")
        return
    
    print(f"\n Akan membuat {len(valid_sizes)} varian: {', '.join(valid_sizes)}")
    
    print("\n INPUT STOK PER SIZE")
    print("-" * 35)
    print("Pilihan input stok:")
    print("1. Stok sama untuk semua size")
    print("2. Input stok per size")
    
    stock_choice = input("\nPilih (1-2): ")
    
    size_stocks = {}
    
    if stock_choice == "1":
        try:
            uniform_stock = int(input("Stok untuk semua size: "))
            for size in valid_sizes:
                size_stocks[size] = uniform_stock
        except:
            print("Input stok tidak valid!")
            return
    else:
        for size in valid_sizes:
            try:
                stock = int(input(f"Stok untuk size {size}: "))
                size_stocks[size] = stock
            except:
                print(f" Stok tidak valid untuk size {size}! Set ke 0")
                size_stocks[size] = 0
    
    new_products = []
    
    all_ids = []
    for p in products:
        all_ids.append(p["id"])
    for p in trash_bin:
        all_ids.append(p["id"])
    
    start_id = max(all_ids) + 1 if all_ids else 1
    
    for i, size in enumerate(valid_sizes):
        full_name = f"{base_name} - {size}"
        
        duplicate = False
        for p in products:
            if p["name"].lower() == full_name.lower():
                duplicate = True
                break
        
        if duplicate:
            print(f"Skip: '{full_name}' sudah ada")
            continue
        
        new_product = {
            "id": start_id + i,
            "name": full_name,
            "category": base_category,
            "size": size,
            "brand": base_brand,
            "price": base_price,
            "stock": size_stocks[size]
        }
        new_products.append(new_product)
    
    if not new_products:
        print("\n Tidak ada produk baru untuk ditambahkan (semua sudah ada)")
        return
    
    print(f"\n PREVIEW {len(new_products)} PRODUK BARU:")
    print("-" * 50)
    
    preview_table = []
    for p in new_products:
        preview_table.append([
            p["id"], p["name"], p["size"], f"Rp {p['price']:,}", p["stock"]
        ])
    
    print(tabulate(preview_table, headers=["ID", "Nama", "Size", "Harga", "Stok"], tablefmt="grid"))
    
    total_stock = sum(p["stock"] for p in new_products)
    total_value = sum(p["price"] * p["stock"] for p in new_products)
    
    print(f"\n Summary:")
    print(f"Total Variants: {len(new_products)}")
    print(f"Total Stok: {total_stock} pcs")
    print(f"Total Nilai: Rp {total_value:,}")
    
    if input("\nSimpan semua produk? (YA/TIDAK): ").upper() == "YA":
        added_count = 0
        for new_prod in new_products:
            products.append(new_prod)
            added_count += 1
        
        create_counter += 1
        create_history.append({
            "order": create_counter,
            "product_id": f"{start_id} - {start_id + len(new_products) - 1}",
            "product_name": base_name,
            "method": "Bulk Variants",
            "variants_added": len(new_products),
            "sizes": ", ".join(valid_sizes)
        })
        
        print(f"\nBERHASIL MENAMBAHKAN {added_count} PRODUK!")
        print(f"Base Product: {base_name}")
        print(f"Sizes: {', '.join(valid_sizes)}")
        print(f"ID Range: {start_id} - {start_id + added_count - 1}")
    else:
        print("Bulk add dibatalkan")

def view_create_history():
    if not create_history:
        print("\n Belum ada create history.")
        return
    print("\nCREATE HISTORY")
    recent = create_history[::-1][:10]
    rows = []
    for h in recent:
        rows.append([
            h.get("order","-"),
            h.get("product_id","-"),
            h.get("product_name","-"),
            h.get("method","-"),
            h.get("variants_added","-") if "variants_added" in h else "-"
        ])
    print(tabulate(rows, headers=["Order","Product ID","Product Name","Method","Variants"], tablefmt="grid"))
    print(f"Total History: {len(create_history)}")

# ==================== 4. UPDATE MENU ====================
def update_menu():
    while True:
        print("\nMENU UPDATE PRODUK")
        print("-" * 35)
        print("1. Update Data Produk (Single)")
        print("2. Bulk Update by Brand")
        print("3. Bulk Update by Category") 
        print("4. Lihat Update History")
        print("5. Kembali ke Menu Utama")
        
        if update_history:
            print(f"\n Total {len(update_history)} perubahan tercatat")
        
        sub_choice = input("\nPilih sub-menu (1-5): ")
        
        if sub_choice == "1":
            update_product_data()
        elif sub_choice == "2":
            bulk_update_by_brand()
        elif sub_choice == "3":
            bulk_update_by_category()
        elif sub_choice == "4":
            view_update_history()
        elif sub_choice == "5":
            print("  Kembali ke menu utama...")
            return
        else:
            print(" Pilihan tidak valid!")

def update_product_data():
    global update_history, update_counter
    
    if not products:
        print(" Tidak ada produk untuk diupdate")
        if trash_bin:
            print(f"  Ada {len(trash_bin)} produk di Trash Bin yang bisa di-restore")
        return
    
    print("\n PRODUK AKTIF:")
    show_products_table(products)
    
    try:
        product_id = int(input("\nID produk yang akan diupdate: "))
    except:
        print(" ID harus angka!")
        return
    
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    
    if not product:
        print(f"\n DATA PRODUK YANG KAMU CARI TIDAK ADA (ID: {product_id})")
        
        in_trash = False
        for p in trash_bin:
            if p["id"] == product_id:
                in_trash = True
                break
        
        if in_trash:
            print(f"  Produk dengan ID {product_id} ada di Trash Bin")
            print("   Gunakan menu DELETE > Manage Trash Bin > Restore untuk mengembalikan")
        
        return
    
    print(f"\n Produk ditemukan: {product['name']}")
    
    if input("\nApakah lanjut di update? (YA/TIDAK): ").upper() != "YA":
        return
    
    print("\n UPDATE (kosongkan jika tidak diubah):")
    changes = {}
    old_values = {}
    
    fields_text = ["name", "category", "size", "brand"]
    for field in fields_text:
        new_val = input(f"{field.title()} ({product[field]}): ").strip()
        if new_val:
            old_values[field] = product[field]
            changes[field] = new_val
    
    fields_num = ["price", "stock"]
    for field in fields_num:
        val = input(f"{field.title()} ({product[field]}): ").strip()
        if val:
            try:
                old_values[field] = product[field]
                changes[field] = int(val)
            except:
                print(f" {field.title()} harus angka!")
    
    if not changes:
        print(" Tidak ada perubahan!")
        return
    
    print("\n Perubahan:")
    for key, value in changes.items():
        print(f"  {key}: {product[key]} → {value}")
    
    if input("\nApakah mau di update? (YA/TIDAK): ").upper() == "YA":
        update_counter += 1
        history_entry = {
            "update_no": update_counter,
            "product_id": product["id"],
            "product_name": product["name"],
            "changes": {},
            "type": "Single Update"
        }
        
        for key, new_value in changes.items():
            history_entry["changes"][key] = {
                "old": old_values[key],
                "new": new_value
            }
            product[key] = new_value
        
        update_history.append(history_entry)
        print("DATA BERHASIL DIUPDATE!")
        print(f" Update tersimpan di history (Update #{update_counter})")
    else:
        print("Update dibatalkan!")

def bulk_update_by_brand():
    global update_counter
    if not products:
        print(" Tidak ada produk.")
        return

    # kumpulkan brand
    brands = []
    for p in products:
        if p["brand"] not in brands:
            brands.append(p["brand"])
    if not brands:
        print("Tidak ada brand.")
        return

    print("\nBrand tersedia:")
    for i, b in enumerate(brands, 1):
        cnt = 0
        for p in products:
            if p["brand"] == b: cnt += 1
        print(f"{i}. {b} ({cnt} produk)")
    bsel = input("Pilih brand (nama persis): ").strip()
    targets = []
    for p in products:
        if p["brand"].lower() == bsel.lower():
            targets.append(p)
    if not targets:
        print("Brand tidak ditemukan.")
        return

    print("\nJenis bulk update:")
    print("1. Harga (persentase)  2. Harga (nilai tetap)  3. Stok (+/-)  4. Stok (set)")
    k = input("Pilih (1-4): ")

    entry = {"update_no": None, "product_id": "Multiple", "product_name": f"Brand: {bsel}", "type": "Bulk Update", "changes": "", "affected_products": []}

    if k == "1":
        try: pct = float(input("Persentase (mis: 10 atau -10): "))
        except: print(" Invalid!"); return
        print(f"Konfirmasi ubah harga {len(targets)} produk brand '{bsel}' sebesar {pct}% ?")
        if input("(YA/TIDAK): ").upper() != "YA": return
        update_counter += 1; entry["update_no"] = update_counter; entry["changes"] = f"Harga {pct}%"
        for p in targets:
            old = p["price"]; new = int(old * (1 + pct/100)); p["price"] = new
            entry["affected_products"].append({"id": p["id"], "name": p["name"], "old_price": old, "new_price": new})
        update_history.append(entry); print("Bulk update harga by brand selesai.")

    elif k == "2":
        try: newp = int(input("Harga baru: Rp "))
        except: print(" Invalid!"); return
        print(f"Konfirmasi set harga {len(targets)} produk brand '{bsel}' ke Rp{newp:,}?")
        if input("(YA/TIDAK): ").upper() != "YA": return
        update_counter += 1; entry["update_no"] = update_counter; entry["changes"] = f"Harga set Rp{newp:,}"
        for p in targets:
            old = p["price"]; p["price"] = newp
            entry["affected_products"].append({"id": p["id"], "name": p["name"], "old_price": old, "new_price": newp})
        update_history.append(entry); print("Bulk set harga by brand selesai.")

    elif k == "3":
        try: delta = int(input("Perubahan stok (+/-): "))
        except: print(" Invalid!"); return
        print(f"Konfirmasi ubah stok {len(targets)} produk brand '{bsel}' sebesar {delta:+d}?")
        if input("(YA/TIDAK): ").upper() != "YA": return
        update_counter += 1; entry["update_no"] = update_counter; entry["changes"] = f"Stok {delta:+d}"
        for p in targets:
            old = p["stock"]; new = max(0, old + delta); p["stock"] = new
            entry["affected_products"].append({"id": p["id"], "name": p["name"], "old_stock": old, "new_stock": new})
        update_history.append(entry); print("Bulk update stok by brand selesai.")

    elif k == "4":
        try: ns = int(input("Set stok: "))
        except: print(" Invalid!"); return
        if ns < 0: print(" Tidak boleh negatif!"); return
        print(f"Konfirmasi set stok {len(targets)} produk brand '{bsel}' ke {ns}?")
        if input("(YA/TIDAK): ").upper() != "YA": return
        update_counter += 1; entry["update_no"] = update_counter; entry["changes"] = f"Stok set {ns}"
        for p in targets:
            old = p["stock"]; p["stock"] = ns
            entry["affected_products"].append({"id": p["id"], "name": p["name"], "old_stock": old, "new_stock": ns})
        update_history.append(entry); print("Bulk set stok by brand selesai.")
    else:
        print("Pilihan tidak valid!")

def bulk_update_by_category():
    global products, update_history, update_counter
    
    if not products:
        print("Tidak ada produk untuk diupdate")
        return
    
    categories = []
    for p in products:
        if p["category"] not in categories:
            categories.append(p["category"])
    
    if not categories:
        print(" Tidak ada kategori tersedia")
        return
    
    print("\n BULK UPDATE BY CATEGORY")
    print("-" * 40)
    print("Kategori tersedia:")
    
    for i, cat in enumerate(categories, 1):
        count = 0
        for p in products:
            if p["category"] == cat:
                count += 1
        print(f"{i}. {cat} ({count} produk)")
    
    cat_choice = input("\nPilih kategori (nama): ").strip()
    
    products_in_category = []
    for p in products:
        if p["category"].lower() == cat_choice.lower():
            products_in_category.append(p)
    
    if not products_in_category:
        print(f" Tidak ada produk dalam kategori '{cat_choice}'")
        return
    
    print(f"\n Ditemukan {len(products_in_category)} produk dalam kategori '{cat_choice}':")
    
    table = []
    for p in products_in_category:
        row = [p["id"], p["name"], f"Rp{p['price']:,}", p["stock"]]
        table.append(row)
    
    print(tabulate(table, headers=["ID", "Nama", "Harga", "Stok"], tablefmt="grid"))
    
    print("\nPILIHAN UPDATE:")
    print("1. Update Harga (persentase)")
    print("2. Update Harga (nilai tetap)")
    print("3. Update Stok (tambah/kurang)")
    print("4. Update Stok (set nilai)")
    print("5. Batal")
    
    update_choice = input("\nPilih jenis update (1-5): ")
    
    if update_choice == "1":
        try:
            percent = float(input("Persentase perubahan harga (misal: 10 untuk +10%, -10 untuk -10%): "))
            
            print(f"\nmengubah harga semua produk kategori '{cat_choice}' sebesar {percent}%")
            
            if input("Lanjutkan? (YA/TIDAK): ").upper() == "YA":
                update_counter += 1
                history_entry = {
                    "update_no": update_counter,
                    "product_id": "Multiple",
                    "product_name": f"Kategori: {cat_choice}",
                    "changes": f"Harga diubah {percent}%",
                    "type": "Bulk Update",
                    "affected_products": []
                }
                
                for p in products_in_category:
                    old_price = p["price"]
                    new_price = int(old_price * (1 + percent/100))
                    p["price"] = new_price
                    history_entry["affected_products"].append({
                        "id": p["id"],
                        "name": p["name"],
                        "old_price": old_price,
                        "new_price": new_price
                    })
                
                update_history.append(history_entry)
                print(f"Berhasil update harga {len(products_in_category)} produk!")
                
        except ValueError:
            print(" Input tidak valid!")
    
    elif update_choice == "2":
        try:
            new_price = int(input("Harga baru untuk semua produk: Rp "))
            
            print(f"\nmengubah harga semua produk kategori '{cat_choice}' menjadi Rp{new_price:,}")
            
            if input("Lanjutkan? (YA/TIDAK): ").upper() == "YA":
                update_counter += 1
                history_entry = {
                    "update_no": update_counter,
                    "product_id": "Multiple",
                    "product_name": f"Kategori: {cat_choice}",
                    "changes": f"Harga diset ke Rp{new_price:,}",
                    "type": "Bulk Update",
                    "affected_products": []
                }
                
                for p in products_in_category:
                    old_price = p["price"]
                    p["price"] = new_price
                    history_entry["affected_products"].append({
                        "id": p["id"],
                        "name": p["name"],
                        "old_price": old_price,
                        "new_price": new_price
                    })
                
                update_history.append(history_entry)
                print(f" Berhasil update harga {len(products_in_category)} produk!")
                
        except ValueError:
            print(" Input tidak valid!")
    
    elif update_choice == "3":
        try:
            stock_change = int(input("Perubahan stok (+/- angka, misal: +10 atau -5): "))
            
            print(f"\nmengubah stok semua produk kategori '{cat_choice}' sebesar {stock_change:+d}")
            
            if input("Lanjutkan? (YA/TIDAK): ").upper() == "YA":
                update_counter += 1
                history_entry = {
                    "update_no": update_counter,
                    "product_id": "Multiple",
                    "product_name": f"Kategori: {cat_choice}",
                    "changes": f"Stok diubah {stock_change:+d}",
                    "type": "Bulk Update",
                    "affected_products": []
                }
                
                for p in products_in_category:
                    old_stock = p["stock"]
                    new_stock = max(0, old_stock + stock_change)
                    p["stock"] = new_stock
                    history_entry["affected_products"].append({
                        "id": p["id"],
                        "name": p["name"],
                        "old_stock": old_stock,
                        "new_stock": new_stock
                    })
                
                update_history.append(history_entry)
                print(f"Berhasil update stok {len(products_in_category)} produk!")
                
        except ValueError:
            print("Input tidak valid!")
    
    elif update_choice == "4":
        try:
            new_stock = int(input("Stok baru untuk semua produk: "))
            
            if new_stock < 0:
                print("Stok tidak boleh negatif!")
                return
            
            print(f"\n mengubah stok semua produk kategori '{cat_choice}' menjadi {new_stock}")
            
            if input("Lanjutkan? (YA/TIDAK): ").upper() == "YA":
                update_counter += 1
                history_entry = {
                    "update_no": update_counter,
                    "product_id": "Multiple",
                    "product_name": f"Kategori: {cat_choice}",
                    "changes": f"Stok diset ke {new_stock}",
                    "type": "Bulk Update",
                    "affected_products": []
                }
                
                for p in products_in_category:
                    old_stock = p["stock"]
                    p["stock"] = new_stock
                    history_entry["affected_products"].append({
                        "id": p["id"],
                        "name": p["name"],
                        "old_stock": old_stock,
                        "new_stock": new_stock
                    })
                
                update_history.append(history_entry)
                print(f"Berhasil update stok {len(products_in_category)} produk!")
                
        except ValueError:
            print("Input tidak valid!")
    
    elif update_choice == "5":
        print("Bulk update dibatalkan")
        return

def view_update_history():
    print("\nUPDATE HISTORY LOG")
    print("-" * 50)
    
    if not update_history:
        print("Belum ada history update")
        return
    
    reversed_history = update_history[::-1]
    
    for i, entry in enumerate(reversed_history[:10], 1):
        print(f"\n{i}. Update #{entry['update_no']}")
        print(f"Type: {entry['type']}")
        print(f"Product: {entry['product_name']} (ID: {entry['product_id']})")
        
        if entry['type'] == 'Single Update':
            print("Changes:")
            for field, values in entry['changes'].items():
                print(f"- {field}: {values['old']} → {values['new']}")
        elif entry['type'] == 'Bulk Update':
            print(f"Changes: {entry['changes']}")
            print(f"Affected: {len(entry['affected_products'])} produk")
            
            show_details = input("   Lihat detail produk? (y/n): ").lower()
            if show_details == 'y':
                for prod in entry['affected_products']:
                    if 'old_price' in prod:
                        print(f"• {prod['name']}: Rp{prod['old_price']:,} → Rp{prod['new_price']:,}")
                    elif 'old_stock' in prod:
                        print(f"• {prod['name']}: Stok {prod['old_stock']} → {prod['new_stock']}")
    
    print(f"\n Total {len(update_history)} perubahan dalam history")
    
    if len(update_history) > 10:
        print(f"Menampilkan 10 history terbaru dari {len(update_history)} total")

# ==================== 5. DELETE MENU ====================
def delete_menu():
    while True:
        print("\n MENU DELETE PRODUK")
        print("-" * 35)
        print("1. Delete Data Produk")
        print("2. Bulk Delete (by IDs, ke Trash)")
        print("3. Manage Trash Bin")
        print("4. Kembali ke Menu Utama")
        
        if trash_bin:
            print(f"\nTrash Bin berisi {len(trash_bin)} item")
        
        sub_choice = input("\nPilih sub-menu (1-4): ")
        
        if sub_choice == "1":
            delete_product_to_trash()
        elif sub_choice == "2":
            bulk_delete_to_trash()
        elif sub_choice == "3":
            manage_trash_bin()
        elif sub_choice == "4":
            print("Kembali ke menu utama...")
            return
        else:
            print("Pilihan tidak valid!")

def delete_product_to_trash():
    global products, trash_bin, delete_counter
    
    if not products:
        print("Tidak ada produk untuk dihapus")
        return
    
    print("\nPRODUK AKTIF:")
    show_products_table(products)
    
    try:
        product_id = int(input("\nID produk yang akan dihapus: "))
    except:
        print("ID harus angka!")
        return
    
    product = None
    product_index = None
    for i, p in enumerate(products):
        if p["id"] == product_id:
            product = p
            product_index = i
            break
    
    if not product:
        print(f"\nDATA PRODUK YANG KAMU CARI TIDAK ADA (ID: {product_id})")
        return
    
    print(f"\nProduk ditemukan: {product['name']}")
    print(f"Kategori: {product['category']}")
    print(f"Harga: Rp{product['price']:,} | Stok: {product['stock']}")
    
    if input("\nApakah mau lanjut di delete? (YA/TIDAK): ").upper() != "YA":
        return
    
    print("\nProduk akan dipindahkan ke Trash Bin")
    print("(Bisa di-restore dari menu Manage Trash Bin)")
    
    if input("\nApakah mau di delete? (YA/TIDAK): ").upper() == "YA":
        deleted_product = products.pop(product_index)
        
        delete_counter += 1
        deleted_product['delete_order'] = f"Delete #{delete_counter}"
        
        trash_bin.append(deleted_product)
        
        print(f"\n DATA BERHASIL DIDELETE!")
        print(f"'{deleted_product['name']}' dipindahkan ke Trash Bin")
        print(f"Gunakan menu 'Manage Trash Bin' untuk restore atau hapus permanen")
    else:
        print("Delete dibatalkan!")

def bulk_delete_to_trash():
    global products, trash_bin, delete_counter

    if not products:
        print("\nTidak ada produk untuk dihapus.")
        return

    print("\nPRODUK AKTIF:")
    show_products_table(products)

    # Input daftar ID
    raw = input("\nMasukkan daftar ID yang akan dihapus (pisahkan dengan koma, contoh: 2,5,7): ").replace(" ", "")
    if not raw:
        print("Daftar ID kosong.")
        return

    # Parse & deduplicate
    parts = raw.split(",")
    unique_ids = []
    for s in parts:
        if s == "":
            continue
        try:
            pid = int(s)
            if pid > 0 and pid not in unique_ids:
                unique_ids.append(pid)
        except:
            print(f"Lewati token bukan angka: '{s}'")

    if not unique_ids:
        print("Tidak ada ID valid.")
        return

    # Kumpulkan target
    targets = []
    not_found = []
    for pid in unique_ids:
        found = None
        for p in products:
            if p["id"] == pid:
                found = p
                break
        if found:
            targets.append(found)
        else:
            not_found.append(pid)

    if not targets:
        print("Tidak ada ID yang cocok dengan produk aktif.")
        if not_found:
            print(f"ID tidak ditemukan: {not_found}")
        return

    # Preview target
    prev = []
    for t in targets:
        prev.append([t["id"], t["name"], t["category"], t["brand"], f"Rp{t['price']:,}", t["stock"]])

    print(f"\nTarget untuk dihapus ke Trash ({len(targets)} item):")
    print(tabulate(prev, headers=["ID","Nama","Kategori","Brand","Harga","Stok"], tablefmt="grid"))

    if not_found:
        print(f"\nID tidak ditemukan (diabaikan): {not_found}")

    # Konfirmasi level 1
    if input("\nLanjut hapus ke Trash? (YA/TIDAK): ").upper() != "YA":
        print("Dibatalkan.")
        return

    # Konfirmasi level 2
    if input("Konfirmasi akhir, hapus semua target ke Trash? (YA/TIDAK): ").upper() != "YA":
        print("Dibatalkan.")
        return

    # Eksekusi: pindahkan ke Trash
    removed = 0
    remaining = []
    id_set = unique_ids  # list ID yang dibidik
    for p in products:
        remove_this = False
        for tid in id_set:
            if p["id"] == tid:
                remove_this = True
                break
        if remove_this:
            item = p.copy()
            delete_counter += 1
            item["delete_order"] = f"Delete #{delete_counter}"
            trash_bin.append(item)
            removed += 1
        else:
            remaining.append(p)

    products = remaining
    print(f"\nBulk delete selesai. {removed} item dipindahkan ke Trash Bin.")
    print("Gunakan 'Manage Trash Bin' untuk restore atau hapus permanen.")

def manage_trash_bin():
    while True:
        print("\n MANAGE TRASH BIN")
        print("-" * 35)
        print("1. Lihat Isi Trash Bin")
        print("2. Restore dari Trash Bin")
        print("3. Hapus Produk dari Trash Bin (Per Item)")
        print("4. Kosongkan Trash Bin")
        print("5. Kembali ke Menu Delete")
        
        if trash_bin:
            print(f"\n Trash berisi {len(trash_bin)} item")
        else:
            print("\n Trash kosong")
        
        choice = input("\nPilih (1-5): ")
        
        if choice == "1":
            view_trash_bin()
        elif choice == "2":
            restore_from_trash()
        elif choice == "3":
            delete_from_trash_permanently()
        elif choice == "4":
            empty_trash_bin()
        elif choice == "5":
            print("Kembali ke menu delete...")
            return
        else:
            print("Pilihan tidak valid!")

def view_trash_bin():
    print("\n ISI TRASH BIN")
    print("-" * 50)
    
    if not trash_bin:
        print("Trash Bin kosong")
        return
    
    table = []
    for i, p in enumerate(trash_bin):
        row = [
            i+1,
            p["id"],
            p["name"],
            p["category"],
            p["size"],
            p["brand"],
            f"Rp{p['price']:,}",
            p["stock"],
            p.get("delete_order", "Unknown")
        ]
        table.append(row)
    
    headers = ["No", "ID", "Nama", "Kategori", "Size", "Brand", "Harga", "Stok", "Delete Order"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    
    print(f"\n Total item di Trash: {len(trash_bin)}")

def restore_from_trash():
    global products, trash_bin
    
    if not trash_bin:
        print("\n Trash Bin kosong, tidak ada yang bisa di-restore")
        return
    
    print("\n PRODUK DI TRASH BIN:")
    view_trash_bin()
    
    try:
        trash_no = int(input("\nNomor urut produk yang akan di-restore (lihat kolom No): "))
        
        if trash_no < 1 or trash_no > len(trash_bin):
            print(" Nomor tidak valid!")
            return
            
        product_to_restore = trash_bin[trash_no - 1]
        
        print(f"\n Produk yang akan di-restore:")
        print(f"ID: {product_to_restore['id']}")
        print(f"Nama: {product_to_restore['name']}")
        print(f"Kategori: {product_to_restore['category']}")
        print(f"Delete Order: {product_to_restore.get('delete_order', 'Unknown')}")
        
        if input("\nRestore produk ini? (YA/TIDAK): ").upper() == "YA":
            restored_product = product_to_restore.copy()
            if 'delete_order' in restored_product:
                del restored_product['delete_order']
            
            products.append(restored_product)
            trash_bin.pop(trash_no - 1)
            
            print(f"\n PRODUK BERHASIL DI-RESTORE!")
            print(f"'{restored_product['name']}' sekarang kembali aktif")
        else:
            print("Restore dibatalkan")
            
    except ValueError:
        print("Input harus angka!")

def delete_from_trash_permanently():
    global trash_bin
    
    if not trash_bin:
        print("\nTrash Bin kosong")
        return
    
    print("\nPRODUK DI TRASH BIN:")
    view_trash_bin()
    
    try:
        trash_no = int(input("\nNomor urut produk yang akan dihapus PERMANEN: "))
        
        if trash_no < 1 or trash_no > len(trash_bin):
            print("Nomor tidak valid!")
            return
        
        product_to_delete = trash_bin[trash_no - 1]
        
        print(f"\n PERINGATAN: Hapus Permanen!")
        print(f"ID: {product_to_delete['id']}")
        print(f"Nama: {product_to_delete['name']}")
        print(f"Kategori: {product_to_delete['category']}")
        print("\nData tidak bisa dikembalikan!")
        
        if input("\nYakin hapus PERMANEN? (YA/TIDAK): ").upper() == "YA":
            deleted = trash_bin.pop(trash_no - 1)
            print(f"\n PRODUK DIHAPUS PERMANEN!")
            print(f"'{deleted['name']}' telah dihapus")
        else:
            print("Penghapusan permanen dibatalkan")
            
    except ValueError:
        print("Input harus angka!")

def empty_trash_bin():
    global trash_bin
    
    if not trash_bin:
        print("\n Trash Bin sudah kosong")
        return
    
    print(f"\n PERINGATAN!")
    print(f"Anda akan menghapus PERMANEN {len(trash_bin)} item dari Trash Bin")
    print("Data tidak bisa dikembalikan!")

    print("\n Item yang akan dihapus:")
    for i, p in enumerate(trash_bin, 1):
        print(f"{i}. {p['name']} (ID: {p['id']})")
    
    if input("\nKosongkan Trash Bin? (YA/TIDAK): ").upper() == "YA":
        count = len(trash_bin)
        trash_bin.clear()
        print(f"\n TRASH BIN DIKOSONGKAN!")
        print(f"{count} item telah dihapus permanen")
    else:
        print("Pengosongan trash dibatalkan")

# ==================== RUN PROGRAM ====================
main()