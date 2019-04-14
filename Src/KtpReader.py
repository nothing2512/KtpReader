import cv2
import numpy
import re
import pytesseract
from matplotlib import pyplot
from Src.KtpResponse import KtpResponse

class KtpReader(object):

    __result = {}
    __data = {}
    __globalText = {}
    __needle = ["NIK", "Nama", "Tempat/Tgl Lahir", "Jenis Kelamin", "Alamat", "RT/RW", "Kel/Desa", "Kecamatan", "Agama", "Status Perkawinan", "Pekerjaan", "Kewarganegaraan"]

    # reading images
    def __readImage(self, path):

        image = cv2.imread(path)
        image = cv2.cvtColor(image, 6)

        result = pytesseract.image_to_string(image)

        return result
    
    def __getPhoto(self, image):
        pass

    # removing unwanted char
    def __lexChar(self, x, i = 0):
        if re.match(".*" + self.__needle[i], self.__globalText[x]) != None:
            value = self.__globalText[x].split(self.__needle[i])[-1]
            if self.__needle[i] == "Jenis Kelamin":
                value = value.split("Gol. Darah")
                self.__data["Gol.Darah"] = re.sub("[^a-zA-Z0-9 \\ \/]", "", value[-1])
                self.__data[self.__needle[i]] = re.sub("[^a-zA-Z0-9 \\ \/]", "", value[0])
            else:
                self.__data[self.__needle[i]] = re.sub("[^a-zA-Z0-9 \\ \/]", "", value)
        if i < len(self.__needle) - 1:
            self.__lexChar(x, i + 1)

    # scanning text value
    def __scan(self, x = 0):
        self.__lexChar(x)
        if x < len(self.__globalText) - 1:
            self.__scan(x+1)

    # normalize ktp data
    def __normalize(self, x, tok = "", i = 0):
        data = self.__data[x].split(" ")
        if data[i] != "":
            if tok == "":
                tok += data[i]
            elif x == "Kewarganegaraan":
                pass
            else:
                tok += " " + data[i]
        if i < len(data) - 1:
            self.__normalize(x, tok, i + 1)
        self.__result[x] = tok

    # getting data drom images
    def __getData(self, text):
        
        self.__globalText = text.split("\n")

        self.__scan()
        
        for x in self.__data:
            self.__normalize(x)

    # scanning image method
    # params: Str
    def scan(self, image):
        textData = self.__readImage(image)
        self.__getData(textData)
        
        return len(self.__result) == 13

    # getting data value
    def __get(self, key):
        if key in self.__data:
            return self.__data[key]
        else:
            return ""

    # get nik
    def getNik(self):
        return self.__get("NIK")

    # get Name
    def getName(self):
        return self.__get("Nama")
    
    # get dob
    def getDob(self):
        return self.__get("Tempat/Tgl Lahir")
    
    # get gender
    def getGender(self):
        return self.__get("Jenis Kelamin")
    
    # get blood type
    def getBlood(self):
        return self.__get("Gol. Darah")
    
    # get address
    def getAddress(self):
        return self.__get("Alamat")
    
    # get RT/RW
    def getRtRw(self):
        return self.__get("RT/RW")

    # get Kelurahan
    def getKelurahan(self):
        return self.__get("Kel/Desa")

    # get Kecamatan
    def getKecamatan(self):
        return self.__get("Kecamatan")
    
    # get religion
    def getReligion(self):
        return self.__get("Agama")

    # get Married
    def getMarried(self):
        return self.__get("Status Perkawinan")
    
    # get work
    def getWork(self):
        return self.__get("Pekerjaan")

    # get nationally
    def getNationally(self):
        return self.__get("Kewarganegaraan")

    # get all data
    def getAll(self):
        return KtpResponse(self.__data)