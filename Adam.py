class ReservasiHotel:
    def __init__(self):
        self.reservasi = {}

    def buat_reservasi(self):
        nama = input("Masukkan nama Anda: ")
        tanggal_checkin = input("Masukkan tanggal check-in (YYYY-MM-DD): ")
        tanggal_checkout = input("Masukkan tanggal check-out (YYYY-MM-DD): ")
        kamar = input("Masukkan jenis kamar yang diinginkan (Standard/Deluxe/VIP): ")
        
        # Simpan data reservasi
        self.reservasi[nama] = {
            'Tanggal Check-in': tanggal_checkin,
            'Tanggal Check-out': tanggal_checkout,
            'Jenis Kamar': kamar
        }
        print(f"Reservasi berhasil untuk {nama}!")

    def tampilkan_reservasi(self):
        if not self.reservasi:
            print("Belum ada reservasi.")
            return
        print("\nDaftar Reservasi:")
        for nama, detail in self.reservasi.items():
            print(f"Nama: {nama}")
            for key, value in detail.items():
                print(f"{key}: {value}")
            print("-" * 30)

    def batalkan_reservasi(self):
        nama = input("Masukkan nama reservasi yang ingin dibatalkan: ")
        if nama in self.reservasi:
            del self.reservasi[nama]
            print(f"Reservasi untuk {nama} telah dibatalkan.")
        else:
            print(f"Tidak ada reservasi dengan nama {nama}.")

def menu():
    hotel = ReservasiHotel()
    while True:
        print("\n--- Sistem Manajemen Reservasi Hotel ---")
        print("1. Buat Reservasi")
        print("2. Tampilkan Reservasi")
        print("3. Batalkan Reservasi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            hotel.buat_reservasi()
        elif pilihan == '2':
            hotel.tampilkan_reservasi()
        elif pilihan == '3':
            hotel.batalkan_reservasi()
        elif pilihan == '4':
            print("Terima kasih telah menggu
