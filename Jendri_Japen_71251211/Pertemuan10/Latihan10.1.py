def bandingkan_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))

    print("=== HASIL PERBANDINGAN ===\n")

    for i in range(max_len):
        baris1 = lines1[i].strip() if i < len(lines1) else ""
        baris2 = lines2[i].strip() if i < len(lines2) else ""

        if baris1 != baris2:
            print(f"Perbedaan pada baris ke-{i+1}:")
            print(f"File 1: {baris1}")
            print(f"File 2: {baris2}")
            print("-" * 40)

file_a = "file1.txt"
file_b = "file2.txt"

bandingkan_file(file_a, file_b)