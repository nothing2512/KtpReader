from KtpReader import KtpReader
import sys

reader = KtpReader()
isStop = 0

image = input("Input Image path = ")
res = reader.scan(image)

if res == False:
    print("Error")
else:
    while(isStop == 0):
        key = input("Masukkan data yang akan di ambil = ")
        if key == "stop":
            isStop = 1
        else:
            print(reader.get(key))
