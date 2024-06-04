import random
# Procedure menu()
def menu():
    print("1. TAMBAH")
    print("2. TOLAK")
    print("3. DARAB")
    print("4. BAHAGI")
    print("5. TAMAT")
    
# Function dptPilihanPengguna()
def dptPilihanPengguna():
    noPilihan = 0
    while (noPilihan < 1) or (noPilihan > 5):
         noPilihan = int(input("Pilihan anda [1 hingga 5]: "))
    return noPilihan

# Function dptDuaNombor()
def dptDuaNombor():
    nombor1 = random.randint(1, 100)
    nombor2 = random.randint(1, 100)
    return nombor1, nombor2

# Procedure kiraCetak()
def kiraCetak(jenisOperator, a, b):
    score=0

    if jenisOperator == 1:
        print(str(a)+"+"+str(b)+"=")
        tambah = int(input("Jawapan : "))
        answer_1 = a+b
        if answer_1 == tambah:
            print("CORRECT! GOOD JOB!\n")
            score = score + 1

        else:
            print("INCORRECT!\n")
            print("Answer: " + str(a) + " + " + str(b) + " = " + str(a + b) +"\n")

    elif jenisOperator == 2:
        print(str(a)+"-"+str(b)+"=")
        tolak = int(input("Jawapan : "))
        answer_2 = a-b
        if answer_2 == tolak:
            print("CORRECT! GOOD JOB!\n")
            score = score + 1

        else:
            print("INCORRECT!\n")
            print("Answer: " + str(a) + " - " + str(b) + " = " + str(a - b) +"\n")

    elif jenisOperator == 3:
        print(str(a)+"x"+str(b)+"=")
        darab = int(input("Jawapan : "))
        answer_3 = a*b
        if answer_3 == darab:
            print("CORRECT! GOOD JOB!\n")
            score = score + 1

        else:
            print("INCORRECT!\n")
            print("Answer: " + str(a) + " * " + str(b) + " = " + str(a * b) +"\n")

    elif jenisOperator == 4:
        print(str(a)+"/"+str(b)+"=")
        bahagi = float(input("Jawapan : "))
        answer_4 = a/b
        if answer_4 == bahagi:
            print("CORRECT! GOOD JOB!\n")
            score = score + 1

        else:
            print("INCORRECT!\n")
            print("Answer: " + str(a) + " / " + str(b) + " = " + format((a / b),".2f") +"\n")
    

# main ----------------------------------------------------------------------------
aktif = 1
while aktif == 1:
    menu()
    jenisOperasi = dptPilihanPengguna()
    if jenisOperasi == 5:
        aktif = 0
    else:
        [nom1, nom2] = dptDuaNombor()
        kiraCetak(jenisOperasi, nom1, nom2)