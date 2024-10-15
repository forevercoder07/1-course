print(" \tDostafka xizmatiga xush kelibsiz! \n O'zingizga kerakli menyuni tanlang.")


def menu():
    print("1. Taomlar ro'yxati.  \n2. Bizning manzilimiz.  \n3. Biz bilan aloqa.")
    son = int(input("Raqamni kiriting: "))
    if son == 1:
        taom()
    elif son == 2:
        manzil()
    elif son == 3:
        aloqa()
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()

def taom():
    print(" \t Taomlar ro'yxati")
    print("1. Lavash. \n2. Pitsa. \n3. Somsa  \n4. Burger  \n5.Menuga qaytish ")
    son = int(input("Kerakli raqamni kiriting: "))
    if son == 1:
        lavash()
    elif son == 2:
        pitsa()
    elif son == 3:
        somsa()
    elif son == 4:
        burger()
    elif son == 5:
        menu()
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()

def lavash():
    print("1. Tandir lavash \n2. Lavash \n3. Menuga qaytish")
    raqam = int(input("Kerakli raqamni kiriting: "))
    if raqam == 1:
        narx_lavash1()
    elif raqam == 2:
        narx_lavash2()
    elif raqam == 3:
        menu()
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()
def narx_lavash1():
    print("1 dona tandir lavash 25 ming so'm. ")
    narx = int(input("Nechta tandir lavash olasiz: "))
    if narx >= 1:
        hisob = narx * 25
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")
def narx_lavash2():
    print("1 dona  lavash 21 ming so'm. ")
    narx = int(input("Nechta lavash olasiz: "))
    if narx >= 1:
        hisob = narx * 21
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")

def pitsa():
    print("1.Pishloqli pitsa.  \n2. Kolbasali pitsa. \n3. Salatli pitsa. \n4. Menuga qaytish")
    raqam = int(input("Kerakli raqamni kiriting: "))
    if raqam == 1:
        narx_pitsa1()
    elif raqam == 2:
        narx_pitsa2()
    elif raqam == 3:
        narx_pitsa3()
    elif raqam == 4:
        menu()
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()
def narx_pitsa1():
    print("1 dona pishloqli pitsa 40 ming so'm. ")
    narx = int(input("Nechta pishloqli pitsa olasiz: "))
    if narx >= 1:
        hisob = narx * 40
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")
def narx_pitsa2():
    print("1 dona kolbasali pitsa 42 ming so'm. ")
    narx = int(input("Nechta kolbasali pitsa olasiz: "))
    if narx >= 1:
        hisob = narx * 42
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")
def narx_pitsa3():
    print("1 dona salatli pitsa 37 ming so'm. ")
    narx = int(input("Nechta salatli pitsa olasiz: "))
    if narx >= 1:
        hisob = narx * 37
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")

def somsa():
    print("1. Go'shli somsa \n2. Kartoshkali somsa \n3. Menu ga qaytish")
    raqam = int(input("Kerakli raqamni kiriting: "))
    if raqam == 1:
        narx_somsa1()
    elif raqam == 2:
        narx_somsa2()
    elif raqam == 3:
        menu()
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()
def narx_somsa1():
    print("1 dona go'shli somsa 10 ming so'm. ")
    narx = int(input("Nechta go'shli somsa olasiz: "))
    if narx >= 1:
        hisob = narx * 10
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")
def narx_somsa2():
    print("1 dona  kartoshkali somsa 5 ming so'm. ")
    narx = int(input("Nechta kartoshkali somsa olasiz: "))
    if narx >= 1:
        hisob = narx * 5
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")

def burger():
    print("1.Chizburger.  \n2. Doner. \n3. Big burger. \n4. Menuga qaytish")
    raqam = int(input("Kerakli raqamni kiriting: "))
    if raqam == 1:
        narx_burger1()
    elif raqam == 2:
        narx_burger2()
    elif raqam == 3:
        narx_burger3()
    elif raqam == 4:
        menu()
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()
def narx_burger1():
    print("1 dona chizburger 20 ming so'm. ")
    narx = int(input("Nechta chizburger olasiz: "))
    if narx >= 1:
        hisob = narx * 20
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")
def narx_burger2():
    print("1 dona doner 25 ming so'm. ")
    narx = int(input("Nechta doner olasiz: "))
    if narx >= 1:
        hisob = narx * 25
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")
def narx_burger3():
    print("1 dona big burger 28 ming so'm. ")
    narx = int(input("Nechta big burger olasiz: "))
    if narx >= 1:
        hisob = narx * 28
        print("Siz", hisob, "ming so'm to'lashingiz kerak")
        raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting. \nHisob raqamimizni olish uchun 1 ni bosing."))
        if raqam1 == 7:
            menu()
        else:
            print("Menyudagi raqamlardan birini kiriting")
            menu()
        if raqam1 == 1:
            print("5860456495786595")

def manzil():
    print("Bizning manzilimiz: Toshkent shahri, Uchtepa tumani.")
    raqam1 = int(input("Menu ga qaytish uchun 7 raqamini kiriting."))
    if raqam1 == 7:
        menu()
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()
def aloqa():
    print("1. Bizning saytimiz  \n2. Bizning aloqa raqamimiz \n3. Menuga qaytish")
    raqam = int(input("Kerakli raqamni kiriting:"))
    if raqam == 1:
        print("www.dostafka.com")
    else:
        print("Menyudagi raqamlardan birini kiriting")
        menu()
    if raqam == 2:
        print("+998(77)741-75-74")





menu()



