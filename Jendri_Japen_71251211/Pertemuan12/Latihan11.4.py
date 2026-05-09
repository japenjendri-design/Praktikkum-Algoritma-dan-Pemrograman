def hitung_domain(nama_file):
    file = open(nama_file)
    domain_count = {}

    for baris in file:
        if baris.startswith("From "):
            kata = baris.split()
            email = kata[1]
            domain = email.split("@")[1]
            domain_count[domain] = domain_count.get(domain, 0) + 1
    print(domain_count)

nama = input("Masukan nama file: ")
hitung_domain(nama)
