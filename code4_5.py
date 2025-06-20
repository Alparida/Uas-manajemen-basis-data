print(" ALparida ")
wide_column_db = {
    "produk1": {"nama": "Laptop", "harga": 8000000, "stok": 10},
    "produk2": {"nama": "komputer", "harga": 5000000, "stok": 25},
    "produk3": {"nama": "sepatu", "harga": 3000000, "stok": 15},
    "produk4": {"nama": "LCD", "harga": 2000000, "stok": 8},
    "produk5": {"nama": "Headphone", "harga": 750000, "stok": 30}
}

print(f"{'ID':<10} {'Nama':<15} {'Harga':<12} {'Stok':<5}")

print("-" * 45)


for row_key, columns in wide_column_db.items():
    nama = columns.get("nama", "-")
    harga = columns.get("harga", 0)
    stok = columns.get("stok", 0)
    print(f"{row_key:<10} {nama:<15} {harga:<12} {stok:<5}")
