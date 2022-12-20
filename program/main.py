# ===============================================================
# =*                   Nama Anggota Kelompok                   *=
# ===============================================================
# =*1. Wuri Wilatiningsih     (121140167)                      *=
# =*2. Andrean Syahrezi       (121140169)                      *=     
# =*3. M. Bintang Erlangga H. (121140171)                      *=
# =*4. Farhan Apri Kesuma     (121140179)                      *=
# =*5. Muhammad Fabil         (121140189)                      *=
# ===============================================================
# =* Link GitHub: https://github.com/parhannn/Matvek-40167.git *=
# ===============================================================
# =*        Program Penyelesaian SPL dengan Gauss-Jordan       *=
# ===============================================================

# Impor file test case
from TestCase import TestCase1 as Case1
from TestCase import TestCase2 as Case2

# Impor file sistem operasi
import os

# Fungsi untuk menampilkan matriks
def PrintMatrix(Matrix, NumOfRow):
    for i in range(NumOfRow):
        print(*Matrix[i])

# Fungsi untuk mereduksi matriks menjadi bentuk eselon baris tereduksi.
def GaussianJordanOperation(Matrix, NumOfRow):
    i = 0
    j = 0
    k = 0
    c = 0
    flag = 0
 
    # Melakukan operasi dasar
    for i in range(NumOfRow):
        if (Matrix[i][i] == 0):
 
            c = 1
            while ((i + c) < NumOfRow and Matrix[i + c][i] == 0):
                c += 1
            if ((i + c) == NumOfRow):
 
                flag = 1
                break
 
            j = i
            for k in range(1 + NumOfRow):
 
                temp = Matrix[j][k]
                Matrix[j][k] = Matrix[j+c][k]
                Matrix[j+c][k] = temp
 
        for j in range(NumOfRow):
 
            # Termasuk semua i == j
            if (i != j):
                # Mengubah Matriks menjadi bentuk eselon baris tereduksi (matriks diagonal)
                p = Matrix[j][i] / Matrix[i][i]
 
                k = 0
                for k in range(NumOfRow + 1):
                    Matrix[j][k] = Matrix[j][k] - (Matrix[i][k]) * p
 
    return flag
 
# Fungsi untuk mencetak hasil yang diinginkan jika ada solusi unik, 
# jika tidak, tidak mencetak solusi atau solusi tak terbatas
# tergantung masukan yang diberikan.
def PrintResult(Matrix, NumOfRow, flag):
 
    if (flag == 2):# Jika flag == 2, maka solusi tak terbatas
        print("Infinite Solutions Exists")
    elif (flag == 3):# Jika flag == 3, maka tidak memiliki solusi
        print("No Solution Exists")
 
    # Mencetak solusi dengan membagi konstanta dengan elemen diagonal masing-masing
    else:
        for i in range(NumOfRow):
            print(Matrix[i][NumOfRow] / Matrix[i][i], end=" ")
 
# Untuk memeriksa apakah solusi tak terbatas atau tidak memiliki solusi
def CheckConsistency(Matrix, NumOfRow, flag):
 
    # flag == 2 untuk solusi tak terbatas
    # flag == 3 untuk tidak ada solusi
    flag = 3
    for i in range(NumOfRow):
        sum = 0
        for j in range(NumOfRow):
            sum = sum + Matrix[i][j]
        if (sum == Matrix[i][j]):
            flag = 2
 
    return flag

# Program Driver
if __name__ == "__main__":
    # Inisialisasi flag
    flag = 0
    # Inisialisasi variabel matriks
    Matrix = []
    # Inisialisasi baris dan kolom
    ManyRow = 0
    ManyColumn = 0

    OperationSystem = os.name # Deklarasi atribut

    while(True):
        match OperationSystem:# Atribut yang berfungsi untuk membersihkan terminal
                              # sebelum menampilkan tampilan menu utama
            case "posix": os.system("clear")# Atribut
            case "nt": os.system("cls")# Atribut

        print("==========================================")
        print("=*Nama : Wuri Wilatiningsih             *=")
        print("=*NIM  : 121140167                      *=")
        print("=*Nama : Andrean Syahrez                *=")
        print("=*NIM  : 121140169                      *=")
        print("=*Nama : M. Bintang Erlangga H.         *=")
        print("=*NIM  : 121140171                      *=")
        print("=*Nama : Farhan Apri Kesuma             *=")
        print("=*NIM  : 121140179                      *=")
        print("=*Nama : Muhammad Fabil                 *=")
        print("=*NIM  : 12114089                       *=")

        # Tampilan menu utama
        print("==========================================")
        print("=*               Main Menu              *=")
        print("==========================================")
        print("1. Input Values from Keyboard\n2. Input Values from Test Case 1\n3. Input Values from Test Case 2\n4. Exit")
        print("==========================================")
        InputMethod = input("(1, 2, 3, 4)==> ")# Memilih metode input apakah ingin dari papan ketik atau file
        print("==========================================")
        match InputMethod:
            case "1":# Input dari user
                # Input baris dan kolom
                ManyRow = int(input("Enter number of rows: "))
                ManyColumn = int(input("Enter number of columns: "))
                print("==========================================")
                print("=*       Enter the entries rowwise      *=")
                print("==========================================")

                # Untuk input dari user
                for i in range(ManyRow):
                    a = []
                    for j in range(ManyColumn):
                        a.append(float(input("=> ")))
                    Matrix.append(a)
                print("==========================================")
                print("=*       Current Augmented Matrix       *=")
                print("==========================================")
                PrintMatrix(Matrix, ManyRow)
                print("==========================================")
                
                # Melakukan transformasi matriks
                flag = GaussianJordanOperation(Matrix, ManyRow)

                # Jika flag == 1, maka akan dicek apakah matriks memiliki
                # solusi tak terbatas atau tidak memiliki solusi
                if(flag == 1):
                    flag = CheckConsistency(Matrix, ManyRow, flag)

                
                # Mencetak bentuk akhir matriks
                print("=*        Final Augmented Matrix        *=")
                print("==========================================")
                PrintMatrix(Matrix, ManyRow)
                print("==========================================")

                # Mencetak solusi spl
                print("=*               Solution               *=")
                print("==========================================")
                PrintResult(Matrix, ManyRow, flag)
                print("\n==========================================")

                if flag != 2 & 3:
                    solution = [0, 0, 0, 0]

                    solution[0] = Matrix[0][4]/Matrix[0][0]
                    solution[1] = Matrix[1][4]/Matrix[1][1]
                    solution[2] = Matrix[2][4]/Matrix[2][2]
                    solution[3] = Matrix[3][4]/Matrix[3][3]

                # Menyimpan bentuk akhir matrtiks ke file arsip berekstensi .txt
                with open('database1.txt', 'w') as file:
                    archive = Matrix

                    file.write("==========================================\n")
                    file.write("=*           Final form matrix          *=\n")
                    file.write("==========================================\n")
                    file.writelines("% s\n" % data for data in archive)
                    file.write("==========================================\n")
                    file.write("=*               Solution               *=\n")
                    file.write("==========================================\n")
                    if flag == 2:
                        file.write("Infinite Solutions Exists\n")
                    elif flag == 3:
                        file.write("No Solution Exists")
                    else:
                        file.writelines("% s\n" % data for data in solution)
                    file.write("==========================================\n")

            case "2":# Input dari File (Referensi == TestCase1 as Case1)
                print("=*       Current Augmented Matrix       *=")
                print("==========================================")
                PrintMatrix(Case1.Matrix, Case1.ManyRow)
                print("==========================================")

                # Melakukan transformasi matriks
                flag = GaussianJordanOperation(Case1.Matrix, Case1.ManyRow)

                if(flag == 1):
                    flag = CheckConsistency(Case1.Matrix, Case1.ManyRow, flag)
                
                # Mencetak bentuk akhir matriks
                print("=*        Final Augmented Matrix        *=")
                print("==========================================")
                PrintMatrix(Case1.Matrix, Case1.ManyRow)
                print("==========================================")

                # Mencetak solusi spl
                print("=*               Solution               *=")
                print("==========================================")
                PrintResult(Case1.Matrix, Case1.ManyRow, flag)
                print("\n==========================================")

                if flag != 2 & 3:
                    solution = [0, 0, 0, 0]

                    solution[0] = Case1.Matrix[0][4]/Case1.Matrix[0][0]
                    solution[1] = Case1.Matrix[1][4]/Case1.Matrix[1][1]
                    solution[2] = Case1.Matrix[2][4]/Case1.Matrix[2][2]
                    solution[3] = Case1.Matrix[3][4]/Case1.Matrix[3][3]
                
                # Menyimpan bentuk akhir matrtiks ke file arsip berekstensi .txt
                with open('database2.txt', 'w') as file:
                    archive = Case1.Matrix

                    file.write("==========================================\n")
                    file.write("=*           Final form matrix          *=\n")
                    file.write("==========================================\n")
                    file.writelines("% s\n" % data for data in archive)
                    file.write("==========================================\n")
                    file.write("=*               Solution               *=\n")
                    file.write("==========================================\n")
                    if flag == 2:
                        file.write("Infinite Solutions Exists\n")
                    elif flag == 3:
                        file.write("No Solution Exists")
                    else:
                        file.writelines("% s\n" % data for data in solution)
                    file.write("==========================================\n")
                
            case "3":# Input dari File (Referensi == TestCase1 as Case1)
                print("=*       Current Augmented Matrix       *=")
                print("==========================================")
                PrintMatrix(Case2.Matrix, Case2.ManyRow)
                print("==========================================")

                # Melakukan transformasi matriks
                flag = GaussianJordanOperation(Case2.Matrix, Case2.ManyRow)

                if(flag == 1):
                    flag = CheckConsistency(Case2.Matrix, Case2.ManyRow, flag)
                
                # Mencetak bentuk akhir matriks
                print("=*        Final Augmented Matrix        *=")
                print("==========================================")
                PrintMatrix(Case2.Matrix, Case2.ManyRow)
                print("==========================================")

                # Mencetak solusi spl
                print("=*               Solution               *=")
                print("==========================================")
                PrintResult(Case2.Matrix, Case2.ManyRow, flag)
                print("\n==========================================")

                if flag != 2 & 3:
                    solution = [0, 0, 0, 0]

                    solution[0] = Case2.Matrix[0][4]/Case2.Matrix[0][0]
                    solution[1] = Case2.Matrix[1][4]/Case2.Matrix[1][1]
                    solution[2] = Case2.Matrix[2][4]/Case2.Matrix[2][2]
                    solution[3] = Case2.Matrix[3][4]/Case2.Matrix[3][3]
                
                # Menyimpan bentuk akhir matrtiks ke file arsip berekstensi .txt
                with open('database3.txt', 'w') as file:
                    archive = Case2.Matrix

                    file.write("==========================================\n")
                    file.write("=*           Final form matrix          *=\n")
                    file.write("==========================================\n")
                    file.writelines("% s\n" % data for data in archive)
                    file.write("==========================================\n")
                    file.write("=*               Solution               *=\n")
                    file.write("==========================================\n")
                    if flag == 2:
                        file.write("Infinite Solutions Exists\n")
                    elif flag == 3:
                        file.write("No Solution Exists")
                    else:
                        file.writelines("% s\n" % data for data in solution)
                    file.write("==========================================\n")
                
            case "4":
                break
        
        print("==========================================")
        print("=*                 Exit?                *=")
        print("==========================================")
        IsDone = input("(y/n)==> ") # Apakah sudah selesai dengan program atau tidak
        if IsDone == "y" or IsDone == "Y":   # Jika ya maka program akan berhenti jika tidak
            break                            # maka  program akan mengulang lagi
    print("==========================================")
    print("=*    Program has stoped, Thank You!    *=")
    print("==========================================")
