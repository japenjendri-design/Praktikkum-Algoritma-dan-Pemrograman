try:
    file1 = input("Masukan nama file pertama: ")
    file2 = input("Masukan nama file kedua: ")

    f1 = open(file1, "r")
    f2 = open(file2, "r")

    teks1 = f1.read().lower().split()
    teks2 = f2.read().lower().split()

    set1 = set(teks1)
    set2 = set(teks2)

    kata_sama = set1.intersection(set2)

    print("\nKata-kata yang muncul pada kedua file:")

    for kata in kata_sama:
        print(kata)
    f1.close()
    f2.close()
except FileExistsError:
    print("Error: File tidak ditemukan atau tidak terbaca.")
