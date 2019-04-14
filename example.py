from Src.KtpReader import KtpReader
import sys

reader = KtpReader()
isStop = 0
stop = "stop"

image = input("Input Image path = ")
res = reader.scan(image)

while(isStop == 0):
    key = input("Masukkan data yang akan di ambil = ")
    if key == stop:
        isStop = 1
    else:
        print(key)
