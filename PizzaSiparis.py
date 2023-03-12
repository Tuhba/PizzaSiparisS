#Gerekli kitaplıkları içeri akratıyoruz.
import csv
import datetime
#Menü dosyası açıp içine menüyü yazdırdık.
with open("Menu.txt", "w") as menu:
    menu.write("""* Lütfen Pizzanızı Seçiniz:
1: Klasik Pizza      40
2: Margarita         50
3: Türk Pizza        50
4: Sade Pizza        35
5: Bol Sucuklu Pizza 55
* Seçmek İstediğiniz Ekstra Malzemeler:
11: Zeytin     3
12: Mantar     5
13: Peynir     8
14: Et         15
15: Soğan      4
16: Mısır      8
* Seçiminiz İçin Teşekkür Ederiz!\n""")

#Menü için döngü
with open("Menu.txt") as menu:
    menu_dict = {}
    for line in menu:
        if "*" in line:
            continue
        (key, val) = line.split(": ")
        val = val[:-1]
        menu_dict[int(key)] = val
4

# Üst pizza sınıfını get methodlarıyla tanımkadık.
class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost


# Pizzalar için alt sınıf oluşturma
class Klasik(Pizza):
    cost = 40.0
    def __init__(self):
        self.description = " Salam, sosis, mısır, zeytin, mantar, yeşilbiber." #içindekileri yazdırmak için.
        print(self.description + "\n")

class Margarita(Pizza):
    cost = 50.0
    def __init__(self):
        self.description = "İçindekiler: Domates, mozarella, fesleğen"
        print(self.description + "\n")

class TurkPizza(Pizza):
    cost = 50.0
    def __init__(self):
        self.description = "İçindekiler: Sucuk, pastırma, biber, ve mantar."
        print(self.description + "\n")

class SadePizza(Pizza):
    cost = 35.0
    def __init__(self):
        self.description = "İçindekiler: Domates sosu."
        print(self.description + "\n")

class BolSucukluPizza(Pizza):
    cost = 55.0
    def __init__(self):
        self.description = "Domates sosu, sucuk, biber."
        print(self.description + "\n")


# Malzemeler için üst sınıf oluşturma
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
            ' : ' + Pizza.get_description(self)


# Malzemeler için alt sınıf oluşturma
class Zeytin(Decorator):
    cost = 3

    def __init__(self, topping):
        Decorator.__init__(self, topping)

class Mantar(Decorator):
    cost = 5

    def __init__(self, topping):
        Decorator.__init__(self, topping)

class Peynir(Decorator):
    cost = 8

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 15

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 4

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 8

    def __init__(self, topping):
        Decorator.__init__(self, topping)


def main():
    with open("Menu.txt") as cust_menu:
        for l in cust_menu:
            print(l, end="")

    class_dict = {1: Klasik,
                  2: Margarita,
                  3: TurkPizza,
                  4: SadePizza,
                  5: BolSucukluPizza,
                  11: Zeytin,
                  12: Mantar,
                  13: Peynir,
                  14: Et,
                  15: Sogan,
                  16: Misir}

    code = input("İstediğiniz pizzanın rakamını giriniz: ")
    while code not in ["1", "2", "3", "4", "5"]:
        code = input("Üzgünüm, yanlış seçim yaptınız.")

    order = class_dict[int(code)]()

    while code != "Evet":
        code = input("Ekstra malzeme ister misiniz? (Siparişinizi onaylamak için 'Evet' yazınız.): ")
        if code in ["11", "12", "13", "14", "15", "16"]:
            order = class_dict[int(code)](order)

    print("\n" + order.get_description().strip() +
          ", ₺" + str(order.get_cost()))
    print("\n")

    print("Sipariş bilgilerinizi giriniz.\n")
    name = input("İsim giriniz: ")
    ID = input("TC kimlik numarası giriniz: ")
    credit_card = input("Kredi kartı numaranısı giriniz: ")
    credit_pass = input("Kredi kartı şifresi giriniz: ")
    kullanıcı_no = input("Numaranızı giriniz: ")
    kullanıcı_adres = input("Adres bilgilerinizi giriniz: ")

    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, ID, credit_card, credit_pass, order.get_description(), time_of_order])
        print("Siparişiniz onaylandı, teşekkür ederiz.")
        print("Siparişinizi en kısa sürede adresinize teslim edeceğiz.")
        print(f" Eğer bir sorun olursa, sizinle iletişime geçeceğiz. ")
        print("İyi günler dileriz.")

if __name__ == '__main__':
    main()
