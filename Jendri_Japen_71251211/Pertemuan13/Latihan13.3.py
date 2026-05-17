def distribusi_jam():
    nama_file = input("Enter a file nime: ")
    file = open(nama_file)

    jam_count = dict()

    for baris in file:
        if baris.startswith("From "):
            kata = baris.split()
            waktu = kata[5]
            jam = waktu.split(":")[0]

            jam_count[jam] = jam_count.get(jam, 0) + 1

    for jam, jumlah in sorted(jam_count.items()):
        print(jam, jumlah)
distribusi_jam()
