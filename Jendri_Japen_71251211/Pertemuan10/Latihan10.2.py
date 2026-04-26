def quiz(nama_file):
    file = open(nama_file, 'r')
    soal_list = file.readlines()
    file.close()

    print("nama file1:", nama_file)

    for data in soal_list:
        soal, jawaban_benar = data.strip().split("||")
        
        print(soal.strip())
        jawaban_user = input("Jawab: ")

        if jawaban_user.strip().lower() == jawaban_benar.strip().lower():
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")
        print()

quiz("soal.txt")