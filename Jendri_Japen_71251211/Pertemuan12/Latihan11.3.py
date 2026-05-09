def hitung_email(nama_file):
    file = open(nama_file)

    histogram = {}

    for baris in file:
        if baris.startswith("From "):
            kata = baris.split()
            email = kata[1]

            histogram[email] = histogram.get(email, 0) + 1
    print(histogram)

nama = input ("Masukan nama file: ")
hitung_email(nama)
