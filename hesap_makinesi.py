print("İşlem numarası seçiniz :", 
    "1. Toplama",
    "2. Bölme")
islem = input("İşlem numarası: ")
num1 = int(input("İlk sayı : "))
num2 = int(input("İkinci sayı : "))



if islem == "1":
   print("{} + {} = {}".format(num1,num2,num1+num2))   
elif islem == "2":
	try:    
		print("{} / {} = {}".format(num1,num2,num1/num2))
    except ZeroDivisionError:
        print("Sayı 0'a bölünemez.")