playstore = {"Communication": ["WhatsApp", "Telegram", "Line"], "Social": ["WhatsApp", "Instagram", "TikTok"], "Video": ["TikTok", "YouTube"], "Music": ["SPotify"]}
jumlah_kategori = {}
for kategori in playstore:
    for aplikasi in playstore[kategori]:
        if aplikasi not in jumlah_kategori:
            jumlah_kategori[aplikasi] = 1
        else:
            jumlah_kategori[aplikasi] += 1
n = int(input("Masukan nilai n: "))
if n == 1:
    print("\nAplikasi yang hanya muncul di satu kategori:")
    for aplikasi in jumlah_kategori:
        if jumlah_kategori[aplikasi] == 1:
            print(aplikasi)
elif n > 2:
    print("\nAplikasi yang muncul tepat di dua kategori:")
    for aplikasi in jumlah_kategori:
        if jumlah_kategori[aplikasi] == 1:
            print(aplikasi)
else:
    print("Tidak ada kondisi untuk nilai n tersebut.")
