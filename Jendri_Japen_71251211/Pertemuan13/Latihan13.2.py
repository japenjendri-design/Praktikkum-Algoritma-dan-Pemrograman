def biodata():
    data = ('Jendri M Japen', '71251211', 'Yogyakarta')

    print("NIM: ", data[1])
    print("NAMA: ", data[0])
    print("ALAMAT: ", data[2])

    print("NIM: ", tuple(data[1]))
    
    nama_depan = data[0].split()[0]
    print("NAMA DEPAN: ", tuple(nama_depan[1:]))

    nama_tabola_bale = tuple(reversed(data[0].split()))
    print("NAMA TERBALIK: ", nama_tabola_bale)

biodata()


